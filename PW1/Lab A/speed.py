import time
from decay import simulate, simulate_loop

N0, LAM = 200_000, 0.4

t0 = time.perf_counter()
simulate_loop(N0, LAM)
t1 = time.perf_counter()

t2 = time.perf_counter()
simulate(N0, LAM)
t3 = time.perf_counter()

print(f"loop  : {t1-t0:.4f} s")
print(f"numpy : {t3-t2:.4f} s")
print(f"speed-up: {(t1-t0)/(t3-t2):.1f}x faster")
