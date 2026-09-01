with open("script.js", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if line.strip() == "init();":
        break

draw_code = """
// --- TEMPORARY DRAWING TOOL LOGIC ---
const drawOutput = document.getElementById('draw-output');
let drawCoords = [];
const drawGroup = L.layerGroup().addTo(map);
const drawPolyline = L.polyline([], {color: '#ffff00', weight: 4, dashArray: '5, 5'}).addTo(drawGroup);

map.on('click', function(e) {
    const lat = parseFloat(e.latlng.lat.toFixed(4));
    const lng = parseFloat(e.latlng.lng.toFixed(4));
    
    drawCoords.push([lat, lng]);
    drawPolyline.setLatLngs(drawCoords);
    
    L.circleMarker([lat, lng], {
        radius: 4, fillColor: '#ffff00', color: '#000', weight: 1, fillOpacity: 1
    }).addTo(drawGroup);
    
    drawOutput.value = JSON.stringify(drawCoords, null, 2);
});

document.getElementById('clear-draw-btn').addEventListener('click', () => {
    drawCoords = [];
    drawPolyline.setLatLngs([]);
    drawGroup.clearLayers();
    drawGroup.addLayer(drawPolyline);
    drawOutput.value = '';
});
"""

with open("script.js", "w") as f:
    f.writelines(new_lines)
    f.write(draw_code)
