---
title: DAO Treasury Governance Lab
emoji: 🗳️
colorFrom: blue
colorTo: indigo
sdk: static
pinned: false
---

# DAO Treasury Governance Lab

Behavioral-science artifact for COMSCI/ECON 206 PS2.

**Project:** Governing the DAO Treasury: Token-Weighted vs. Square-Root Voting under Whale Concentration and Sybil Attacks  
**Author:** Zhou Zimu  
**Course instructor:** Professor Luyao Zhang

## What this Space does

- Presents the same 8-actor DAO treasury setting used by the computational project.
- Compares token-weighted voting (TWV) with square-root voting (SRV).
- Randomizes rule order and whether the Sybil-splitting incentive is made salient.
- Records only the current browser session; there is no backend or server-side participant database.
- Lets a user export a JSON record for self-play or structured peer-play reflection.
- Clearly separates human exploratory choices from the separate synthetic Python simulation.

## Evidence boundary

The Space is an exploratory behavioral artifact, not a population-level experiment. The displayed numerical benchmark is synthetic computational evidence from the accompanying Python simulation (seed 206, 1,000 valuation profiles per condition), not human-participant data.

## Before final submission

Open `index.html` and fill in these two constants near the top of the script once the artifacts are published:

```js
const GITHUB_URL = "";
const COLAB_URL = "";
```

No Gradio, Python backend, tracking library, or external dependency is required.
