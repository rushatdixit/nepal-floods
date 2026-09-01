# Nepal Floods 2026: Sentinel-2 Satellite Imagery Analysis

An interactive web mapping application visualizing the devastating flash floods and Glacial Lake Outburst Flood (GLOF) of August 26, 2026, in the Nepal-Tibet border region (Rasuwa District / Gyirong Port). 

## Overview
This tool dynamically queries the **Microsoft Planetary Computer STAC API** in real-time to fetch, mosaic, and render high-resolution **Sentinel-2 L2A optical satellite imagery**. By comparing cloud-free baseline imagery (Before) with the immediate aftermath (After), the application exposes the massive geological scarring and infrastructure damage left behind by the debris flow.

## Features
- **Dynamic Satellite Imagery**: Connects directly to the Planetary Computer to retrieve seamless Sentinel-2 map tiles using anonymous SAS tokens.
- **Smart Cloud-Filtering**: Scans orbital passes using a strict cloud-cover threshold to automatically select and render the clearest day to use as a baseline and aftermath comparison.
- **Interactive Measurement Tool**: A custom-built distance and width measurement tool utilizing Leaflet's Haversine formula engine for true Earth-curvature accuracy. Measurements drop permanent segment labels and dynamically color-code themselves (Green for Before imagery, Red for After imagery) for direct visual comparisons of river expansion.
- **Interactive River Tracing**: A precise, glowing path traces the exact route of the destruction down the Lhende Khola and Trishuli River valleys.
- **Cinematic Location Teleportation**: Users can fly to 4 critically impacted waypoints (including the Langtang Lirung Glacier source and the Gyirong Port border crossing) via an interactive control panel.
- **Embedded Footage**: Location markers feature popups with embedded YouTube Shorts showcasing verified on-the-ground footage of the devastation.
- **Refined Minimalist UI**: Features collapsible information panels with custom SVG toggle icons, an integrated map scale, dynamic loading HUDs, explicit API rate-limit error handling, and map legends.

## Technologies Used
* **HTML/CSS/JavaScript (Vanilla)**: No heavy frameworks, purely static files.
* **Leaflet.js**: For interactive map rendering, panning, and cinematic `flyTo` animations.
* **Microsoft Planetary Computer (STAC API)**: For spatial-temporal querying and dynamic tile generation of open-source Sentinel-2 data.
* **Esri World Dark Gray Base**: Provides a stark, undistracting canvas that allows the raw satellite data to stand out.

## Local Development
Since the application consists entirely of client-side code, no build step or backend is required. 
1. Clone the repository.
2. Serve the directory using any basic HTTP server (e.g., `python3 -m http.server 8080`).
3. Open `http://localhost:8080` in your browser.

## Deployment
This project is designed to be fully compatible with **GitHub Pages**. Simply push the repository to GitHub and enable Pages deployment from the `main` branch to host it globally for free. Cache-busting URL parameters are actively maintained to ensure users always receive the latest UI updates.
