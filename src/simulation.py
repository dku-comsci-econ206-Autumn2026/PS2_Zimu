"""Reproducible, paired Monte Carlo comparison of DAO treasury voting rules.

Run from repository root: python -m src.simulation
No third-party packages are required.
"""

import csv
import json
import math
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PARAMETERS = ROOT / "inputs" / "parameters.json"
OUTPUT = ROOT / "outputs"
CONDITIONS = (("TWV_m1", "TWV", 1), ("SRV_m1", "SRV", 1),
              ("SRV_m8", "SRV", 8))
METRICS = ("holder_efficiency", "stake_efficiency", "whale_success",
           "nonwhale_representation")


def load_parameters(path=PARAMETERS):
    with open(path, encoding="utf-8") as f:
        p = json.load(f)
    assert p["total_actors"] == p["ordinary_holders"] + p["whale_holders"]
    assert p["whale_holders"] == 1 and p["ordinary_holders"] > 0
    assert math.isclose(p["whale_token_share"] + p["ordinary_collective_share"], 1)
    assert p["profiles"] > 0 and p["sybil_wallets"] > 1
    assert p["proposals"] == ["A", "B", "C"]
    return p


def profiles(p):
    """Generate one shared sequence of valuation profiles for all conditions."""
    rng = random.Random(p["seed"])
    for number in range(1, p["profiles"] + 1):
        yield number, [[rng.random() for _ in p["proposals"]]
                       for _ in range(p["total_actors"])]


def best(values):
    """Index of maximum; earliest proposal wins exact ties."""
    return max(range(len(values)), key=lambda i: values[i])


def evaluate(valuations, rule, wallets, p):
    """Actor 0 is whale. Sybil wallets cast the same sincere vote as their owner."""
    n = len(p["proposals"])
    whale_stake = p["whale_token_share"]
    ordinary_stake = p["ordinary_collective_share"] / p["ordinary_holders"]
    if rule == "TWV":
        whale_power = whale_stake
        ordinary_power = ordinary_stake
    elif rule == "SRV":
        whale_power = wallets * math.sqrt(whale_stake / wallets)
        ordinary_power = math.sqrt(ordinary_stake)
    else:
        raise ValueError(rule)

    scores = [0.0] * n
    votes = [best(v) for v in valuations]
    scores[votes[0]] += whale_power
    for vote in votes[1:]:
        scores[vote] += ordinary_power
    winner = best(scores)

    holder_welfare = [sum(v[j] for v in valuations) for j in range(n)]
    stake_welfare = [whale_stake * valuations[0][j] +
                     ordinary_stake * sum(v[j] for v in valuations[1:])
                     for j in range(n)]
    ordinary_welfare = [sum(v[j] for v in valuations[1:]) for j in range(n)]
    # All denominators are positive with probability one for continuous draws.
    return {
        "winner": p["proposals"][winner],
        "whale_vote": p["proposals"][votes[0]],
        "winner_score": scores[winner],
        "whale_power": whale_power,
        "ordinary_total_power": ordinary_power * p["ordinary_holders"],
        "holder_efficiency": holder_welfare[winner] / max(holder_welfare),
        "stake_efficiency": stake_welfare[winner] / max(stake_welfare),
        "whale_success": int(winner == votes[0]),
        "nonwhale_representation": int(winner == best(ordinary_welfare)),
    }


def run(p=None):
    p = load_parameters() if p is None else p
    rows = []
    for number, valuations in profiles(p):
        for name, rule, wallets in CONDITIONS:
            rows.append({"profile_id": number, "condition": name,
                         "rule": rule, "whale_wallets": wallets,
                         **evaluate(valuations, rule, wallets, p)})
    comparison = []
    for name, rule, wallets in CONDITIONS:
        group = [r for r in rows if r["condition"] == name]
        comparison.append({"condition": name, "rule": rule,
                           "whale_wallets": wallets, "profiles": len(group),
                           **{m: sum(r[m] for r in group) / len(group)
                              for m in METRICS}})
    assert len(rows) == p["profiles"] * len(CONDITIONS)
    assert all(r["whale_success"] == 1 for r in rows if r["condition"] != "SRV_m1")
    assert all(a["winner"] == b["winner"] for a, b in
               zip(rows[0::3], rows[2::3]))  # TWV and split SRV coincide here
    return rows, comparison


def save(rows, comparison, p, directory=OUTPUT):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    with open(directory / "simulation_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with open(directory / "mechanism_comparison.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(comparison[0]))
        writer.writeheader()
        writer.writerows(comparison)
    summary = {
        "model": "sincere plurality across three mutually exclusive treasury proposals",
        "parameters": p,
        "metric_definitions": {
            "holder_efficiency": "mean over profiles of winning total actor valuation / maximal total actor valuation",
            "stake_efficiency": "mean over profiles of winning token-share-weighted valuation / maximal token-share-weighted valuation",
            "whale_success": "fraction of profiles where winner is whale's top-valued proposal",
            "nonwhale_representation": "fraction where winner maximizes seven ordinary holders' combined valuation",
        },
        "results": {row["condition"]: {m: row[m] for m in METRICS}
                    for row in comparison},
        "observation": "SRV with eight equal whale wallets yields whale voting power above all ordinary holders combined; TWV and split SRV choose the whale's sincere first choice on every paired profile.",
    }
    with open(directory / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return summary


def main():
    p = load_parameters()
    rows, comparison = run(p)
    save(rows, comparison, p)
    print("condition,holder_efficiency,stake_efficiency,whale_success,nonwhale_representation")
    for row in comparison:
        print(",".join([row["condition"]] + [f"{row[m]:.6f}" for m in METRICS]))
    print(f"Saved {len(rows)} condition-profile rows to {OUTPUT}")


if __name__ == "__main__":
    main()
