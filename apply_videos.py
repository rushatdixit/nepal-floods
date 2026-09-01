with open("script.js", "r") as f:
    content = f.read()

# Replace the locations array
old_locations = """const locations = [
    {
        name: "Langtang Lirung Glacier",
        coords: [28.2933, 85.5254],
        desc: "Suspected source of the Glacial Lake Outburst Flood (GLOF).",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Gyirong Port (China)",
        coords: [28.2797, 85.3779],
        desc: "Chinese Immigration Office completely inundated during the flash flood.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Rasuwa Gadhi",
        coords: [28.2645, 85.3745],
        desc: "Nepal-side major border crossing heavily damaged by the sudden deluge.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Syaphrubesi",
        coords: [28.163, 85.337],
        desc: "Confluence of the Langtang Khola and Bhote Koshi. Extensive infrastructure damage.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Trisuli / Bidur",
        coords: [27.9221, 85.1488],
        desc: "Downstream settlements where the floodwaters expanded and inundated hydropower projects.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
];"""

new_locations = """const locations = [
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
];"""

content = content.replace(old_locations, new_locations)

old_popup = """    const popupContent = `
        <div style="font-family: Arial, sans-serif; max-width: 200px;">
            <h3 style="margin: 0 0 5px 0; font-size: 14px; color: #333;">${index + 1}. ${loc.name}</h3>
            <p style="margin: 0 0 10px 0; font-size: 12px; color: #666;">${loc.desc}</p>
            <a href="${loc.video}" target="_blank" style="display: inline-block; background: #ff3333; color: #fff; text-decoration: none; padding: 5px 10px; border-radius: 3px; font-size: 12px;">▶ Watch Video</a>
        </div>
    `;"""

new_popup = """    let videoLinksHTML = loc.videos.map((vid, i) => 
        `<a href="${vid}" target="_blank" style="display: block; background: #ff3333; color: #fff; text-decoration: none; padding: 5px 10px; border-radius: 3px; font-size: 12px; margin-bottom: 5px; text-align: center;">▶ Watch Video ${loc.videos.length > 1 ? i+1 : ''}</a>`
    ).join('');

    const popupContent = `
        <div style="font-family: Arial, sans-serif; max-width: 200px;">
            <h3 style="margin: 0 0 5px 0; font-size: 14px; color: #333;">${index + 1}. ${loc.name}</h3>
            <p style="margin: 0 0 10px 0; font-size: 12px; color: #666;">${loc.desc}</p>
            ${videoLinksHTML}
        </div>
    `;"""

content = content.replace(old_popup, new_popup)

with open("script.js", "w") as f:
    f.write(content)
