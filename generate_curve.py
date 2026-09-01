import json
import numpy as np
from scipy.interpolate import splprep, splev

# Control points based on the user's drawing (roughly)
# [lon, lat]
points = np.array([
    [85.57, 28.20], # Glacier
    [85.52, 28.28],
    [85.47, 28.33],
    [85.42, 28.35], # Top of arch
    [85.37, 28.33],
    [85.33, 28.27],
    [85.31, 28.20],
    [85.29, 28.10],
    [85.25, 28.00],
    [85.20, 27.90],
    [85.10, 27.82],
    [84.95, 27.75]  # Bottom left
])

x = points[:, 0]
y = points[:, 1]

tck, u = splprep([x, y], s=0)
unew = np.linspace(0, 1, 100)
out = splev(unew, tck)

curve_points = [[round(lon, 4), round(lat, 4)] for lon, lat in zip(out[0], out[1])]
print(json.dumps(curve_points))
