import numpy as np

def logistic_map(r, x):
    return r * x * (1 - x)

def compute_period(r, tol=1e-4, transient=2000, iterations=1000):
    """
    Iterates the logistic map at parameter r, discarding a transient,
    and then records an orbit to determine the period. We return the smallest
    integer p such that the maximum difference between orbit[i] and orbit[i+p]
    (over the available window) is less than tol.
    """
    x = 0.5
    for _ in range(transient):
        x = logistic_map(r, x)
    orbit = []
    for _ in range(iterations):
        x = logistic_map(r, x)
        orbit.append(x)
    orbit = np.array(orbit)
    
    # Test possible periods from 1 up to half the orbit length
    for p in range(1, iterations // 2):
        if np.max(np.abs(orbit[:iterations-p] - orbit[p:])) < tol:
            return p
    return None

def find_bifurcation_auto(r_start, target_period, r_max=4.0, step=1e-4):
    """
    Starting at r_start (where the period is target_period), scan upward
    in steps until the detected period changes. Then use bisection to pinpoint
    the bifurcation point.
    """
    r = r_start
    # Scan until a change in period is observed
    while r < r_max:
        p = compute_period(r)
        if p is not None and p != target_period:
            # A change is detected. Use the previous r value as the lower bound.
            r_low = r - step
            r_high = r
            if compute_period(r_low) == target_period:
                break
        r += step
    else:
        return None  # No bifurcation found in [r_start, r_max]

    # Use bisection to refine the bifurcation point
    for _ in range(50):
        r_mid = (r_low + r_high) / 2.0
        p_mid = compute_period(r_mid)
        if p_mid is None:
            r_low = r_mid  # shift bracket if period detection fails
            continue
        if p_mid == target_period:
            r_low = r_mid
        else:
            r_high = r_mid
    return (r_low + r_high) / 2.0

# Automatically locate several bifurcation points
bif_points = []
# Start in the period-1 region (stable fixed point). r_start should lie in that region.
r_start = 2.5 
target_period = 1

num_bifurcations = 5  # How many bifurcations to locate

for i in range(num_bifurcations):
    bif_point = find_bifurcation_auto(r_start, target_period)
    if bif_point is None:
        print("Could not find further bifurcation.")
        break
    bif_points.append(bif_point)
    detected_period = compute_period(bif_point)
    print(f"Bifurcation {i+1} at r = {bif_point:.6f}, detected period: {detected_period}")
    # Move just above the found bifurcation to search for the next one.
    r_start = bif_point + 0.001
    new_period = compute_period(r_start)
    if new_period is None or new_period <= target_period:
        # Fallback: assume the period has doubled.
        new_period = target_period * 2
        print("Could not determine new period after bifurcation; assuming period doubling to", new_period)
    target_period = new_period

bif_points = np.array(bif_points)
print("\nBifurcation points:", bif_points)

if len(bif_points) >= 2:
    intervals = np.diff(bif_points)
    print("Intervals between bifurcations:", intervals)
    if len(intervals) >= 2:
        delta_estimates = intervals[:-1] / intervals[1:]
        print("Feigenbaum constant estimates:", delta_estimates)
        feigenbaum_estimate = np.mean(delta_estimates)
        print("Estimated Feigenbaum constant:", feigenbaum_estimate)
    else:
        print("Not enough intervals to estimate the Feigenbaum constant.")
else:
    print("Not enough bifurcation points found.")
