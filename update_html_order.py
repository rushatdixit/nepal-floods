import re

with open("index.html", "r") as f:
    content = f.read()

new_panel = """
    <div id="locations-panel">
        <h3>Key Locations</h3>
        <button class="loc-btn" data-index="0">1. Langtang Lirung Glacier</button>
        <button class="loc-btn" data-index="1">2. Gyirong Port (China)</button>
        <button class="loc-btn" data-index="2">3. Rasuwa Gadhi</button>
        <button class="loc-btn" data-index="3">4. Syaphrubesi</button>
        <button class="loc-btn" data-index="4">5. Trisuli / Bidur</button>
    </div>
"""

content = re.sub(r'<div id="locations-panel">.*?</div>', new_panel, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
