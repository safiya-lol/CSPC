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

## PW2 - Lab A: Motion from Tracking Data

**Mean acceleration:** -8.57 m/s² (theoretical -9.81)
**Std of acceleration:** 28.7
**Max position error after integrating back:** 0.78 m 

**Why the acceleration is noisy:**
Acceleration is the second derivative of position, the noises stack, that's why it is very noise.

**What integrating back showed:**
I integrated the noisy acceleration to get velocity, then integrated that to get position. The recovered position matched the original within 0.78  m, which shows integration suppresses the noise that differentiation amplified.

## Part 2B: harder function g(x) = x⁴ − 3x² + x + 5

- **Do the methods agree?** On the easy function all three gave x ≈ 3. On g(x) they did not always agree.
- **Did Newton land on a minimum?** Not always. From x0 = 0 it landed on x ≈ 0.17, which is a maximum because g'' < 0. Newton only finds where the slope is zero, so g'' must be checked.
- **Effect of the starting point:** Gradient descent goes to the nearest valley. From x0 = 0 that was the deepest one (−1.30). From x0 = 2 it was a shallower one (1.13).
- **Lesson:** On a simple function the methods agree. On a bumpy function, the starting point and the method change the answer.

