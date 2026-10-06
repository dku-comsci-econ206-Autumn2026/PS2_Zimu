# Verification and reproducibility audit

## Executed run

From the repository root, `python -m src.simulation` wrote `outputs/simulation_results.csv`, `outputs/mechanism_comparison.csv`, and `outputs/summary.json`. The notebook was executed cell by cell in order using the Python standard library, and its recorded outputs were checked against the CLI. An additional isolated-directory Run All initialized the bundled source and inputs and produced all three outputs byte-identically. It can also be run with a standard notebook interface using **Run All** from the checkout root or standalone in Colab.

The detail file has 3,000 data rows, 1,000 per condition. `profile_id` aligns the **same** valuation draws across all three conditions. The file includes outcomes, effective weights and per-profile contributions to each metric. The eight-by-three synthetic values regenerate exactly from the committed seed, generator, and source code; they are not duplicated in the CSV.

## Definitions and checks

- All actors vote sincerely for their highest of A/B/C; exact ties use proposal order.
- Holder efficiency is the mean of `total valuation for winning proposal / maximal total valuation` per profile.
- Stake efficiency is the mean of `stake-weighted valuation for winner / maximal stake-weighted valuation` per profile.
- Whale success is the fraction in which the winner is the whale's top-valued proposal.
- Non-whale representation is the fraction in which the winner maximizes the seven ordinary actors' total valuation. This is an aggregate outcome proxy, not individual participation or a minority-rights guarantee.
- Whale SRV weight is `sqrt(0.60) = 0.774597` with one wallet and `8 * sqrt(0.60/8) = 2.190890` with eight. Ordinary total SRV weight is `7 * sqrt(0.40/7) = 1.673320`.
- TWV whale weight 0.60 exceeds all ordinary weight 0.40. Split SRV whale weight 2.190890 exceeds all ordinary weight 1.673320. Thus both conditions always pick the whale's sincere favorite (barring a whale valuation tie, which does not occur in this sample), and their results coincide **profile by profile**, not merely after rounding.
- Rows, seed, ties, winner equivalence, output schemas, summary/CSV agreement, rerun determinism, and notebook results were checked during finalization.

## Old page claims versus the executed model

| Condition / metric | Old page | Verified | Change |
| --- | ---: | ---: | ---: |
| TWV and split SRV holder efficiency | 0.9057 | 0.899065 | -0.006635 |
| TWV and split SRV stake efficiency | 0.9924 | 0.991097 | -0.001303 |
| TWV and split SRV whale success | 1.000 | 1.000 | 0 |
| TWV and split SRV non-whale representation | 0.325 | 0.321 | -0.004 |
| Single-wallet SRV holder efficiency | 0.9370 | 0.927781 | -0.009219 |
| Single-wallet SRV stake efficiency | 0.9764 | 0.977076 | +0.000676 |
| Single-wallet SRV whale success | 0.885 | 0.896 | +0.011 |
| Single-wallet SRV non-whale representation | 0.416 | 0.417 | +0.001 |

The old repository had only `README.md` and `index.html`: no source code, valuation distribution, random-number generator, welfare formula or stored sample. Therefore the old exact values cannot be verified or attributed to a particular model. The new results specify independent uniform valuations, sincere voting, Python's seeded generator, ratio-of-realized-to-best welfare per profile, and paired draws. The difference could arise from a different generator, valuation distribution or metric implementation; its precise historical cause is unknown. No code was tuned to reproduce the old table. The page table and exported JSON now cite the computed numbers.

## PS2 computational artifact audit

| Requirement | Location / status |
| --- | --- |
| README, research question, setup and exact run order | `README.md` |
| Code and meaningful mechanism comparison | `src/simulation.py`, three paired conditions |
| Dependencies and inputs | `requirements.txt`, `inputs/parameters.json` |
| Expected and actual outputs | `README.md`, committed `outputs/` |
| Runnable notebook / equivalent baseline | `dao_treasury_simulation.ipynb`, executed; CLI equivalent `python -m src.simulation` |
| Behavioral artifact consistent with results and links | `index.html` table, export, GitHub and Colab links |
| Exact final commit | See final GitHub commit SHA reported with the submission; the commit records all files together. |

This audit verifies the **repository deliverables** listed in the prompt. It does not by itself certify the rest of the PS2 paper, poster, or course submission.
