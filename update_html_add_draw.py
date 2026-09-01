with open("index.html", "r") as f:
    content = f.read()

draw_html = """
    <div id="draw-panel" style="position: absolute; top: 20px; right: 20px; z-index: 1000; background: #111; padding: 15px; border: 1px solid #333; color: white;">
        <h3 style="margin:0 0 10px 0; font-size:14px;">Marker Coordinate Tool</h3>
        <button id="clear-draw-btn" style="padding: 5px; cursor: pointer;">Clear Output</button>
        <p style="font-size: 12px; max-width: 200px;">Click exactly where you want the new markers to be. The coordinates will appear below:</p>
        <textarea id="draw-output" rows="5" cols="25" style="background: #222; color: #0f0; width: 100%; font-family: monospace;"></textarea>
    </div>
"""

content = content.replace('<div id="map"></div>', draw_html + '\n    <div id="map"></div>')

with open("index.html", "w") as f:
    f.write(content)
