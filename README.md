# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/

## Setup

Create the environment for a given lab:

conda env create -f PW<n>/Lab <X>/environment.yml
conda activate cspc

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A CSPC repo with a conda environment, a decay simulation (pure-Python loop and NumPy versions), three pytest tests, and a speed comparison.

**Speed comparison (loop vs NumPy):**
- loop  : 3.7648 s
- numpy : 0.0004 s
- speed-up: 10258x faster

**Tests:** all passing? yes — 3 passed under `pytest -v`
(`test_starts_at_N0`, `test_rejects_negative_rate`, `test_matches_law`).

**Conclusion:**
- I learned how to install git and conda. Now I feel more comfortable working with terminal. This PW demonstrated the importance of vectorisation - it showcased a difference between a loop and Numpy version of simulation, that is 10000x times faster.

## Pw1 — Lab B

The observed decay counts (left panel of `figure.png`) fall off exponentially
with time. The analytical curve `N0 * exp(-LAMBDA * t)` (right panel) tracks
the observed points closely, so the data follows the expected exponential
decay law.

The Snakemake pipeline (`Snakefile`) automates figure generation: it runs
`plot_STUDENT.py` to build `figure.png` from `decay_observed.csv`, and only
reruns when the input data or the script changes.
