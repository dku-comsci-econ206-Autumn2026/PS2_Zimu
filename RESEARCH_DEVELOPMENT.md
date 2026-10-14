# PS2 research-development record — October 14, 2026

**Project:** Governing the DAO Treasury: Token-Weighted vs. Square-Root Voting under Whale Concentration and Sybil Splitting  
**Author:** Zimu Zhou (FP11, solo team)  
**Status convention:** Verified = from executed committed simulation; Planned = proposed work; Pending = requires partner, reviewer, professor or author confirmation.

## Part 1 — Intellectual merits

**Verified benchmark:** 1,000 shared seeded valuation profiles, eight economic actors, one whale owning 60% of stake, three allocation alternatives, sincere voting, and three conditions: TWV (1 wallet), SRV (1 whale wallet), and SRV (8 coordinated whale wallets). Mean non-whale representation rises from 0.321 under TWV to 0.417 under unsplit SRV but returns to 0.321 under eight-wallet SRV. TWV and split SRV choose the same winner profile-by-profile. This is not an estimated treatment effect, equilibrium or real-world DAO prediction. See [VERIFICATION.md](VERIFICATION.md) and [outputs/summary.json](outputs/summary.json).

**Three closest research strands to compare and verify in the written paper** (the sources below are already cited in the current poster; their bibliographic accuracy should be rechecked before submission):

1. Lalley, S. P., and E. G. Weyl. 2018. “Quadratic Voting: How Mechanism Design Can Radicalize Democracy.” *AEA Papers and Proceedings* 108: 33–37. https://doi.org/10.1257/pandp.20181002 — mechanism-design foundation. Our rule is square-root wallet weighting, **not** a full implementation of quadratic voting.
2. Douceur, J. R. 2002. “The Sybil Attack.” *IPTPS*, 251–260. https://doi.org/10.1007/3-540-45748-8_24 — identity-multiplication threat model.
3. Fritsch, R., M. Müller, and R. Wattenhofer. 2024. “Analyzing Voting Power in Decentralized Governance: Who Controls DAOs?” *Blockchain: Research and Applications* 5(3): 100208. https://doi.org/10.1016/j.bcra.2024.100208 — DAO voting-power concentration.

**Intellectual contribution:** paired synthetic stress test distinguishing wallet-based voting power from economic ownership, a reproducible welfare comparison, and a separately bounded behavioral self-play interface. **Planned paper location:** named Intellectual Merits paragraph and annotated model diagram in main text (exact final page/figure number pending). **Planned poster location:** left/center Research Design and Results panels, plus a clearly titled Intellectual Merits block (position pending poster revision). Author responsible: Zimu Zhou.

## Priority self-challenge — research hypothesis, not proven resolution

**Claim to challenge:** SRV improves non-whale representation in the specified one-wallet, sincere-voting synthetic baseline. **Limitation:** eight costless, coordinated whale wallets eliminate this improvement in the benchmark; we have not modeled positive Sybil costs, imperfect coordination, strategic behavior, identity safeguards, or real participant data. **Discriminating test:** vary Sybil wallet count, whale stake, Sybil cost, identity constraints, valuation distributions, and random seeds; compare representation, holder welfare, stake welfare, and participation cost. A partner's suggested solution must be recorded after investigation, not as a confirmed result.

## Practical impacts

**Prospective stakeholder:** DAO treasury members, smaller token holders, governance designers, and communities relying on grants. **Illustrative context:** Uniswap governance; no Uniswap causal effect or live on-chain measurement was performed.

**Candidate SDG targets to assess (not demonstrated impact):** SDG 16, target **16.6** (effective, accountable, transparent institutions) and SDG 16, target **16.7** (responsive, inclusive, participatory decision-making). Candidate indicators: non-whale representation, concentration of effective voting weight, auditability, excluded/failed legitimate voters, privacy burden and identity verification costs. **Baseline:** TWV condition in the same synthetic sample; additional external baselines have not been established. **Safeguard hypothesis:** independently audited identity checks with appeals, minimal data collection and opt-out/rollback conditions, subject to feasibility and exclusion-risk study.

**Planned paper location:** named Practical Impacts subsection and stakeholder-outcome diagram in the two-page main body, detail in appendix. **Planned poster location:** right-side Practical Impacts block. Add **official SDG icons and target codes directly to the impact diagram** in the next poster revision. Current poster does not satisfy this new visual requirement. Author responsible: Zimu Zhou.

## Future Research Roadmap (new diagram required)

Proposed diagram: `Observed wallet-splitting vulnerability → economics incentive study → computer-science attack/cost study → behavioral-science fairness/salience study → validated governance design`. All stages below are **planned**, not executed.

| Stage | Research question | Method/data | Potential collaborator | Progress criterion | Proposed milestone |
| --- | --- | --- | --- | --- | --- |
| Economics | At what stake concentration, wallet cost and strategic preferences would splitting be worthwhile? | Game-theoretic best responses; parameter grid; equilibrium checks where tractable | Economics/mechanism-design collaborator (unconfirmed) | Reproducible threshold and clearly specified equilibrium assumptions | Next prototype after Oct 21 |
| Computer science | Can identity constraints limit Sybils without unacceptable false exclusions? | Synthetic adversarial wallet simulations, identity-cost sensitivity, fairness/error trade-off | Security/identity researcher (unconfirmed) | Attack-resilience curve with false-positive and privacy cost estimates | Follow-on study |
| Behavioral science | Do fairness and disclosed Sybil incentives change individual rule preferences? | Preregistered randomized vignette/self-play experiment with real consented participants | Behavioral researcher (unconfirmed) | Predefined sample/analysis plan and interpretable uncertainty | Future pilot |

**Planned paper location:** Future Research Roadmap subsection after Practical Impacts, expanded diagram and source notes in appendix (numbering to be confirmed). **Planned poster location:** new lower-right Future Research Roadmap panel. The revised diagram must show the **official SDG icon(s) and target codes** beside proposed social outcomes, not as standalone decoration. Partner input is pending and must be reflected accurately after the duet.

## Part 2 — named contributions and acknowledgments

**Zimu Zhou:** solo researcher responsible for research question, mechanism specification, synthetic model, simulation code, outputs, verification, self-play record, manuscript, poster and verification of claims. This statement describes existing artifacts, not independent external review.

**To verify against actual course interactions before submitting:** Prof. Luyao Zhang; Prof. Kenneth S. (Ken) Rogerson; Han Zhang; **every formal reviewer by full name**; discussion contributors; Tencent's Shanghai office; Shanghai Science and Technology Museum; COMSCI/ECON 206 classroom community. Name the specific contribution accurately and do not attribute unverified individual feedback or endorsements. Preserve disclosures for Python, GitHub, Colab, HF, adapted template material, and permitted AI drafting/debugging/layout assistance.

**Planned paper location:** Author Notes → Team Contributions and Acknowledgments following the two-page main text. **Planned poster location:** footer Contributions / Acknowledgments blocks. Full names and detailed contribution descriptions still need confirmation.

## Part 3 — feedback and verified integration

See [FEEDBACK_RESPONSE.md](FEEDBACK_RESPONSE.md). Include instructor feedback, Oct 12–13 self-tests, formal peer reviews and Oct 14 partner investigation **only if actually received**. For each, record date, full source, affected claim, Keep/Revise/Investigate decision, evidence, change location, responsible author, and verification/next test.

**Planned paper location:** appendix titled Response to Feedback (final appendix letter to follow manuscript). **Planned poster location:** new Revision after Feedback block near the Roadmap and with link to full feedback record. The final Ed post should explicitly state completed/planned status and exact page/figure/panel after layout is finalized.

## Oct 14 duet award / interview / final Ed record

**Pending actual classroom events:** partner team ID and names, investigation, author integration, two-minute presentation, award certificate/citation, interviews, collaboration idea, individual handwritten reflection and uploaded photograph. The Ed final post should include Parts 0–3 and the exact paper and poster locations for each, then the partner email should be sent with an actual screenshot of the *published* Ed post.

## October 21 delivery check

- [x] Reproducible baseline simulation, parameters, CSV and JSON outputs, notebook and CLI instructions exist.
- [x] Existing Oct 6 editable A0 poster and PDF now included in the repository.
- [x] Current poster preview and GitHub PDF link at top of README; HF URL in README.
- [ ] Rework A0 poster with **new** Roadmap and SDG target icons; synchronize main paper and appendices.
- [ ] Verify actual instructor/partner feedback and named acknowledgments.
- [ ] Verify HF behavior and deployment in browser.
- [ ] Set GitHub About → Website to the HF URL via repository details (metadata edit not available to this connector).
- [ ] Submit two-page paper, source ZIP, latest A0 editable/PDF, code/reproducibility, feedback response, contributions, acknowledgments, and AI disclosure before October 21, 23:00 Shanghai time.
