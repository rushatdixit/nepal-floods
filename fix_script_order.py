with open("script.js", "r") as f:
    content = f.read()

old_locations = """const locations = [
    {
        name: "Trisuli / Bidur",
        coords: [27.9221, 85.1488],
        desc: "Downstream settlements where the floodwaters expanded and inundated hydropower projects.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Syaphrubesi",
        coords: [28.163, 85.337],
        desc: "Confluence of the Langtang Khola and Bhote Koshi. Extensive infrastructure damage.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Rasuwa Gadhi",
        coords: [28.2645, 85.3745],
        desc: "Nepal-side major border crossing heavily damaged by the sudden deluge.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Gyirong Port (China)",
        coords: [28.2797, 85.3779],
        desc: "Chinese Immigration Office completely inundated during the flash flood.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Langtang Lirung Glacier",
        coords: [28.2933, 85.5254],
        desc: "Suspected source of the Glacial Lake Outburst Flood (GLOF).",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
];"""

new_locations = """const locations = [
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

content = content.replace(old_locations, new_locations)

with open("script.js", "w") as f:
    f.write(content)
