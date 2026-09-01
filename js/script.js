// Define the focused bounds of the affected river valley (Langtang down to Galchhi)
const RIVER_BOUNDS = [
    [27.7, 84.9], // South-West corner (downstream past Galchhi)
    [28.45, 85.65]  // North-East corner (upstream glacier)
];

// Initialize Map with maxBounds to keep the user focused on the affected area
const map = L.map('map', { 
    zoomControl: false,
    maxBounds: RIVER_BOUNDS,
    maxBoundsViscosity: 1.0,
    minZoom: 10
}).setView([28.05, 85.25], 10);

L.control.zoom({ position: 'topright' }).addTo(map);

// Add Dark Base Map (Esri World Dark Gray Base - No API key required)
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',
    maxZoom: 16
}).addTo(map);

// Important Locations
const locations = [
    {
        name: "Langtang Lirung Glacier",
        coords: [28.2933, 85.5254],
        desc: "Suspected source of the Glacial Lake Outburst Flood (GLOF).",
        videos: ["https://youtube.com/shorts/5486SRhhrIE?si=DuXaTG274Tp_m6qs"]
    },
    {
        name: "Gyirong Port (China)",
        coords: [28.2797, 85.3779],
        desc: "Chinese Immigration Office completely inundated during the flash flood.",
        videos: ["https://youtu.be/FFYBmDYQqoA?si=uF6myzjvYWxF6n73"]
    },
    {
        name: "Rasuwa Gadhi",
        coords: [28.2645, 85.3745],
        desc: "Nepal-side major border crossing heavily damaged by the sudden deluge.",
        videos: [
            "https://youtube.com/shorts/S6IUJirhZdE?si=CKwNzEHRIw3e3KR7",
            "https://youtube.com/shorts/wyylHGVuSrs?si=xXheHISs-V3ubr0d"
        ]
    },
    {
        name: "Trisuli / Bidur",
        coords: [27.9221, 85.1488],
        desc: "Downstream settlements where the floodwaters expanded and inundated hydropower projects.",
        videos: ["https://youtube.com/shorts/5XqdU14IXEM?si=OThxo7gxzbWAsu24"]
    }
];

// Smart River Trace (Connecting the key locations with a subtle, glowing line)
const pathCoords = [
  [27.9221, 85.1488],
  [27.9351, 85.1543],
  [27.9559, 85.1633],
  [27.9651, 85.1734],
  [27.9745, 85.1837],
  [27.9847, 85.1799],
  [27.9933, 85.1841],
  [28.0084, 85.1841],
  [28.0139, 85.1845],
  [28.0408, 85.1955],
  [28.0539, 85.2062],
  [28.0686, 85.2052],
  [28.0814, 85.2215],
  [28.0874, 85.2297],
  [28.0933, 85.252],
  [28.0994, 85.2647],
  [28.108, 85.2745],
  [28.1172, 85.2839],
  [28.1356, 85.3052],
  [28.1578, 85.3322],
  [28.1651, 85.3396],
  [28.1648, 85.3419],
  [28.17, 85.3426],
  [28.1815, 85.3424],
  [28.1875, 85.3461],
  [28.2043, 85.3538],
  [28.2154, 85.355],
  [28.2219, 85.3602],
  [28.2364, 85.3593],
  [28.2422, 85.3586],
  [28.2508, 85.3657],
  [28.2567, 85.3657],
  [28.2687, 85.3769],
  [28.2791, 85.3774],
  [28.2874, 85.3882],
  [28.2938, 85.3968],
  [28.2973, 85.3969],
  [28.3079, 85.4106],
  [28.3141, 85.413],
  [28.3224, 85.4132],
  [28.327, 85.4158],
  [28.3301, 85.429],
  [28.3345, 85.4366],
  [28.3352, 85.4476],
  [28.3346, 85.4671],
  [28.3323, 85.4805],
  [28.3313, 85.486],
  [28.3236, 85.4867],
  [28.3204, 85.4882],
  [28.3159, 85.4879],
  [28.3131, 85.4937],
  [28.3079, 85.5002],
  [28.2998, 85.5056],
  [28.2906, 85.5112],
  [28.2903, 85.5214],
  [28.2933, 85.5254]
];
L.polyline(pathCoords, {
    color: '#00ffff',
    weight: 4,
    opacity: 0.6,
    dashArray: '10, 10',
    lineCap: 'round'
}).addTo(map);

// Add interactive, highly visible custom markers
const markers = [];
locations.forEach((loc, index) => {
    // Custom DivIcon for maximum clarity
    const customIcon = L.divIcon({
        className: 'custom-marker',
        html: `<div class="custom-marker-label">${index + 1}. ${loc.name.split(' ')[0]}</div>`,
        iconSize: [20, 20],
        iconAnchor: [10, 10],
        popupAnchor: [0, -10]
    });

    const marker = L.marker(loc.coords, { icon: customIcon }).addTo(map);
    markers.push(marker);

    let videoLinksHTML = loc.videos.map((vid, i) => 
        `<a href="${vid}" target="_blank" style="display: block; background: #ff3333; color: #fff; text-decoration: none; padding: 5px 10px; border-radius: 3px; font-size: 12px; margin-bottom: 5px; text-align: center;">▶ Watch Video ${loc.videos.length > 1 ? i+1 : ''}</a>`
    ).join('');

    const popupContent = `
        <div style="font-family: Arial, sans-serif; max-width: 200px;">
            <h3 style="margin: 0 0 5px 0; font-size: 14px; color: #333;">${index + 1}. ${loc.name}</h3>
            <p style="margin: 0 0 10px 0; font-size: 12px; color: #666;">${loc.desc}</p>
            ${videoLinksHTML}
        </div>
    `;
    
    marker.bindPopup(popupContent);
});

// Teleport buttons logic
document.querySelectorAll('.loc-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const index = e.target.getAttribute('data-index');
        const loc = locations[index];
        // Teleport to the location and open the popup
        map.flyTo(loc.coords, 14, {
            duration: 1.5 // seconds
        });
        // Wait for flyTo to finish before opening popup
        setTimeout(() => {
            markers[index].openPopup();
        }, 1500);
    });
});

// Define STAC Query parameters
const STAC_API_URL = 'https://planetarycomputer.microsoft.com/api/stac/v1/search';
const TILE_API_URL = 'https://planetarycomputer.microsoft.com/api/data/v1/item/tiles/WebMercatorQuad/{z}/{x}/{y}';
const COLLECTION = 'sentinel-2-l2a';

async function fetchSentinel2Layer(startDate, endDate) {
    try {
        const response = await fetch(STAC_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                collections: [COLLECTION],
                bbox: [84.9, 27.7, 85.65, 28.45],
                datetime: `${startDate}/${endDate}`,
                limit: 100,
                query: {
                    'eo:cloud_cover': { lt: 80 }
                },
                sortby: [{ field: 'properties.datetime', direction: 'desc' }]
            })
        });

        const data = await response.json();
        
        if (!data.features || data.features.length === 0) {
            console.error(`No imagery found for period ${startDate} to ${endDate}`);
            return null;
        }

        const passes = {};
        data.features.forEach(f => {
            const dt = f.properties.datetime;
            if (!passes[dt]) passes[dt] = [];
            passes[dt].push(f);
        });

        let bestPassTime = null;
        let minAvgCloudCover = 100;

        for (const [dt, features] of Object.entries(passes)) {
            const avgCloud = features.reduce((sum, f) => sum + f.properties['eo:cloud_cover'], 0) / features.length;
            if (avgCloud < minAvgCloudCover) {
                minAvgCloudCover = avgCloud;
                bestPassTime = dt;
            }
        }
        
        const relevantFeatures = passes[bestPassTime];
        
        // Single SAS token optimization
        const tokenResponse = await fetch('https://planetarycomputer.microsoft.com/api/sas/v1/token/' + COLLECTION);
        const tokenData = await tokenResponse.json();
        const sasToken = tokenData.token;
        
        const layers = relevantFeatures.map(item => {
            const tileUrl = `${TILE_API_URL}?collection=${COLLECTION}&item=${item.id}&assets=visual&format=png&token=${sasToken}`;
            return L.tileLayer(tileUrl, {
                attribution: 'Sentinel-2 imagery &copy; Microsoft',
                maxZoom: 18,
                bounds: RIVER_BOUNDS
            });
        });

        return L.layerGroup(layers);

    } catch (error) {
        console.error('Error fetching layer:', error);
        return null;
    }
}


// --- Network Loading Indicator Logic ---
const loadingIndicator = document.getElementById('loading-indicator');
const loadingText = document.getElementById('loading-text');

let loadingStates = { before: 0, after: 0 };

function updateLoadingUI() {
    if (loadingStates.after > 0 && loadingStates.before > 0) {
        loadingText.innerText = 'Streaming Before & After...';
        loadingIndicator.style.display = 'flex';
    } else if (loadingStates.after > 0) {
        loadingText.innerText = 'Streaming After Imagery...';
        loadingIndicator.style.display = 'flex';
    } else if (loadingStates.before > 0) {
        loadingText.innerText = 'Streaming Before Imagery...';
        loadingIndicator.style.display = 'flex';
    } else {
        loadingIndicator.style.display = 'none';
    }
}

function attachLoadingEvents(layerGroup, key) {
    layerGroup.eachLayer(layer => {
        layer.on('loading', () => {
            loadingStates[key]++;
            updateLoadingUI();
        });
        layer.on('load', () => {
            loadingStates[key]--;
            updateLoadingUI();
        });
    });
}
// ---------------------------------------

async function init() {

    const toggleBtn = document.getElementById('toggle-btn');
    toggleBtn.innerText = 'Loading Satellite Imagery...';
    toggleBtn.disabled = true;

    // Fetch layers concurrently
    const [beforeLayer, afterLayer] = await Promise.all([
        fetchSentinel2Layer('2026-06-01T00:00:00Z', '2026-08-25T23:59:59Z'),
        fetchSentinel2Layer('2026-08-27T00:00:00Z', '2026-08-31T23:59:59Z')
    ]);

    // Attach network event listeners for the professional loading UI
    if (beforeLayer) attachLoadingEvents(beforeLayer, 'before');
    if (afterLayer) attachLoadingEvents(afterLayer, 'after');

    let currentLayer = 'after';

    if (beforeLayer && afterLayer) {
        afterLayer.addTo(map);
        toggleBtn.innerText = 'Switch to Before (Aug 10-25)';
        toggleBtn.disabled = false;

        toggleBtn.addEventListener('click', () => {
            if (currentLayer === 'after') {
                map.removeLayer(afterLayer);
                beforeLayer.addTo(map);
                toggleBtn.innerText = 'Switch to After (Optical)';
                currentLayer = 'before';
            } else {
                map.removeLayer(beforeLayer);
                afterLayer.addTo(map);
                toggleBtn.innerText = 'Switch to Before (Aug 10-25)';
                currentLayer = 'after';
            }
        });
    } else {
        toggleBtn.innerText = 'Error Loading Imagery';
        toggleBtn.disabled = true;
    }
}

init();
