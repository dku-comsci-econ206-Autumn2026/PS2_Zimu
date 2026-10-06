# Governing the DAO Treasury

**Computational-science artifact for COMSCI/ECON 206 PS2.**  
**Project:** Token-Weighted vs. Square-Root Voting under Whale Concentration and Sybil Attacks  
**Author:** Zhou Zimu (FP11) · **Instructor:** Professor Luyao Zhang

## Research question

When one actor owns 60% of a DAO treasury's tokens, does square-root voting (SRV) improve the outcome for ordinary holders relative to token-weighted voting (TWV), and does splitting the whale's stake across eight wallets undo that effect?

## Model overview

Eight actors choose one of three mutually exclusive treasury proposals A, B, and C. One whale owns 0.60 of tokens; seven ordinary holders split 0.40 equally. Each actor has an independently drawn valuation in [0, 1) for each proposal and sincerely votes for their highest-valued option. Every mechanism sees **the same 1,000 profiles**, generated with Python's `random.Random(206)`. Weighted plurality picks the proposal with the highest sum of votes; exact ties favor A, then B, then C.

TWV uses token shares as weights. SRV uses the square root of **each wallet's** share. In the Sybil condition the whale splits 0.60 equally over eight wallets, which all vote for the whale's same preferred proposal; there are still eight economic actors, although there are fifteen voting wallets. Identities and valuations do not multiply. There are no bids, payments, abstentions, strategic reports, Sybil costs, or empirical human responses in this model.

The scarce resource is one treasury allocation. This is a voting mechanism comparison with an allocation interpretation, not a literal auction.

## Repository structure

| Path | Purpose |
| --- | --- |
| `inputs/parameters.json` | Seed, actor counts, token shares, profile count and assumptions |
| `src/simulation.py` | Deterministic generation, voting, welfare metrics, CSV/JSON export |
| `dao_treasury_simulation.ipynb` | Executed, top-to-bottom notebook walkthrough |
| `outputs/simulation_results.csv` | 3,000 condition-profile rows with winners, voting power and metrics; valuations regenerate from seed |
| `outputs/mechanism_comparison.csv` | One averaged row per mechanism |
| `outputs/summary.json` | Parameters, definitions and numerical results |
| `VERIFICATION.md` | Reproduction, checks, benchmark comparison and final audit |
| `index.html` | Separate browser-only behavioral self-play interface |
| `requirements.txt` | Dependency declaration |

## Dependencies and setup

Python 3.10 or later and its standard library suffice. The requirements file has no pip dependencies. To use the notebook interface locally, install Jupyter separately, or run it in an environment with notebook support. In a terminal from a **complete checkout** of this repository:

```bash
python -m pip install -r requirements.txt
python -m src.simulation
```

The GitHub repository is private; opening its Colab link may require an authorized GitHub session. The notebook runs from a complete checkout using `src/` and `inputs/`. When opened alone in Colab, its first cell initializes an embedded copy of the **same** source and parameters in the notebook working directory. The subsequent cells execute and save the same outputs. The canonical editable source remains `src/simulation.py`.

## Exact run order and shortest reproducible run

1. Clone or download the complete repository, enter `PS2_Zimu`, and check Python 3.10+.
2. Run `python -m pip install -r requirements.txt` (no third-party dependencies).
3. Run `python -m src.simulation` to regenerate all three outputs.
4. Open `dao_treasury_simulation.ipynb` and choose **Run All**. It reads the same inputs (or initializes the bundled copy in an isolated Colab session), reruns the model, saves the outputs, checks invariants and prints the comparison. The notebook has committed execution outputs for immediate inspection.

**Shortest reproducible run:** from the repository root, `python -m src.simulation`. No hosted service, Colab, or participant data is needed. Run the notebook after or instead of this command to see each calculation and its interpretation.

## Parameters

| Parameter | Value |
| --- | ---: |
| Economic actors | 8: one whale, seven ordinary |
| Whale stake | 0.60 |
| Ordinary stake | 0.40 total; 0.40 / 7 each |
| Proposals | A, B, C |
| Sybil wallets | 8 equal whale-controlled wallets under SRV |
| Random seed | 206 |
| Profiles | 1,000 **shared** profiles per condition |
| Valuations | Independent continuous uniform [0, 1) for each actor-proposal pair |

## Expected and actual verified outputs

The expected structure is 3,000 detail rows (plus header), three comparison rows, and a JSON summary. Values below were obtained by actually running `python -m src.simulation` with the committed inputs; the notebook independently executes the same entry points. The ratios are means of each profile's realized welfare divided by the best possible welfare under the specified objective. Whale success and ordinary representation are fractions of profiles, rather than welfare ratios.

| Condition | Holder efficiency | Stake efficiency | Whale success | Non-whale representation |
| --- | ---: | ---: | ---: | ---: |
| TWV, one whale wallet | 0.899065 | 0.991097 | 1.000 | 0.321 |
| SRV, one whale wallet | 0.927781 | 0.977076 | 0.896 | 0.417 |
| SRV, eight whale wallets | 0.899065 | 0.991097 | 1.000 | 0.321 |

**Metric meanings:** holder efficiency uses the sum of all eight valuations; stake efficiency weights valuations by each actor's token stake. Whale success means the whale's favorite wins. Non-whale representation means the winner maximizes the **sum** of the seven ordinary actors' valuations. This last measure is not a protected minority metric. See `outputs/summary.json` for machine-readable definitions and full precision.

## Relationship to the Hugging Face behavioral artifact

The HF static interface asks a participant to make choices under two voting rules and reflect on fairness and splitting. `index.html` retains that behavioral flow and now links to this computation and its notebook. Its displayed benchmark and exported JSON quote the verified numbers here. Its fixed four self-play value scenarios and projected other votes are **not** sampled from this simulation; participant choices are not evidence for the computational benchmark. This repository supplies the synthetic baseline, not a server-side participant database.

## Limitations

Results depend on independent uniform valuations, sincere voting, three alternatives, equal ordinary stakes, costless coordinated Sybil wallets, fixed 60% concentration, and the finite seed-206 sample. No strategic equilibrium, security or identity-verification mechanism, uncertainty interval, real DAO data, or causal behavioral effect is established. The older page numbers had no generating code or valuation specification in the two-file repository, so they cannot be reconstructed as a verified benchmark; see `VERIFICATION.md` for the numerical reconciliation.
