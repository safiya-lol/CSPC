"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    # Negative decay rate is unphysical: simulate must raise ValueError.
    # pytest tool: pytest.raises
    with pytest.raises(ValueError):
        simulate(1000, -0.1)


def test_matches_law():
    # Average over many seeds should approach N0 * exp(-lam * t).
    # pytest tool: pytest.approx  (compares floats with a tolerance)
    N0, lam = 1000, 0.4
    dt = 0.05
    t_index = 50            # physical time t = t_index * dt = 2.5
    runs = 200

    samples = [simulate(N0, lam, dt=dt, seed=s)[t_index] for s in range(runs)]
    expected = N0 * np.exp(-lam * t_index * dt)

    assert np.mean(samples) == pytest.approx(expected, rel=0.1)
