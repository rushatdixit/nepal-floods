import urllib.request
import json

# We will just write a high-res path based on typical map routing
path = [
    [85.55, 28.23],
    [85.53, 28.225],
    [85.50, 28.21],
    [85.47, 28.20],
    [85.44, 28.18],
    [85.40, 28.17],
    [85.37, 28.165],
    [85.34, 28.16], # Syaphrubesi
    [85.32, 28.14],
    [85.29, 28.11], # Dhunche
    [85.25, 28.05],
    [85.19, 27.96], # Betrawati
    [85.16, 27.91], # Trisuli
    [85.10, 27.85],
    [85.00, 27.76]  # Galchhi
]
print(json.dumps(path))
