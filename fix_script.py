with open("script.js", "r") as f:
    content = f.read()

# Replace the locations array
old_locations = """const locations = [
    {
        name: "Langtang Lirung Glacier",
        coords: [28.2933, 85.5254], // Updated to exactly match the end of your traced path
        desc: "Suspected source of the Glacial Lake Outburst Flood (GLOF).",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Rasuwa Gadhi / Gyirong Port",
        coords: [28.270, 85.380], // Waiting for your new coordinates!
        desc: "Major border crossing heavily damaged by the sudden deluge.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Chinese Immigration Office", // Replaced Syaphrubesi placeholder
        coords: [28.163, 85.337], // Waiting for your new coordinates!
        desc: "Location of the Chinese Immigration office impacted by the flood.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        name: "Trisuli / Bidur",
        coords: [27.9221, 85.1488], // Updated to exactly match the start of your traced path
        desc: "Downstream settlements where the floodwaters expanded and inundated hydropower projects.",
        video: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
];"""

new_locations = """const locations = [
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

content = content.replace(old_locations, new_locations)

# Truncate at "init();" to remove the drawing logic
init_index = content.find("init();")
if init_index != -1:
    content = content[:init_index + 7] + "\n"

with open("script.js", "w") as f:
    f.write(content)
