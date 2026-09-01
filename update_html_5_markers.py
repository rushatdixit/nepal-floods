import re

with open("index.html", "r") as f:
    content = f.read()

# Update the locations-panel buttons
new_panel = """
    <div id="locations-panel">
        <h3>Key Locations</h3>
        <button class="loc-btn" data-index="0">1. Trisuli / Bidur</button>
        <button class="loc-btn" data-index="1">2. Syaphrubesi</button>
        <button class="loc-btn" data-index="2">3. Rasuwa Gadhi</button>
        <button class="loc-btn" data-index="3">4. Gyirong Port (China)</button>
        <button class="loc-btn" data-index="4">5. Langtang Lirung Glacier</button>
    </div>
"""

content = re.sub(r'<div id="locations-panel">.*?</div>', new_panel, content, flags=re.DOTALL)

# Remove the draw panel
content = re.sub(r'<div id="draw-panel".*?</div>', '', content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
