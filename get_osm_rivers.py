import urllib.request
import json

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
(
  way["waterway"="river"]["name"~"Trishuli|Bhote Koshi|Langtang|Kerung"](27.7,84.9,28.5,85.7);
);
out geom;
"""

req = urllib.request.Request(overpass_url, data=overpass_query.encode('utf-8'))
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        features = []
        for element in data['elements']:
            if 'geometry' in element:
                coords = [[node['lon'], node['lat']] for node in element['geometry']]
                feature = {
                    "type": "Feature",
                    "properties": {"name": element.get('tags', {}).get('name', 'River')},
                    "geometry": {
                        "type": "LineString",
                        "coordinates": coords
                    }
                }
                features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        
        with open('rivers.geojson', 'w') as f:
            json.dump(geojson, f)
        
        print(f"Saved {len(features)} river segments.")
except Exception as e:
    print(f"Error: {e}")
