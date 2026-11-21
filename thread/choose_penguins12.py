"""Chooses the twelve penguins once and writes data/penguins12.csv. Run from the course repo's root
(labs/mathematics/ on the site), with NumPy installed:
    python thread/choose_penguins12.py
Rule: for seed = 0, 1, 2, ...: draw 12 of the 342 rows without replacement with np.random.default_rng(seed),
sort by flipper length (then mass); take the first seed whose twelve have no two birds sharing both values and a
least-squares slope above zero."""
import numpy as np

species = np.loadtxt("data/penguins.csv", delimiter=",", skiprows=1, usecols=0, dtype=str)
x, y = np.loadtxt("data/penguins.csv", delimiter=",", skiprows=1, usecols=(1, 2), unpack=True)
for seed in range(100):
    pick = np.random.default_rng(seed).choice(len(x), size=12, replace=False)
    pick = pick[np.lexsort((y[pick], x[pick]))]
    pairs = set(zip(x[pick], y[pick]))
    slope = np.polyfit(x[pick], y[pick], 1)[0]
    print(f"seed {seed}: distinct pairs {len(pairs)}, slope {slope:.3f}")
    if len(pairs) == 12 and slope > 0:
        break
with open("data/penguins12.csv", "w") as f:
    f.write("species,flipper_length_mm,body_mass_g\n")
    for i in pick:
        f.write(f"{species[i]},{int(x[i])},{int(y[i])}\n")
print("seed used:", seed)
