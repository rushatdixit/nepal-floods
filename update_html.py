with open("index.html", "r") as f:
    content = f.read()

content = content.replace('<button id="toggle-btn">Switch to Before (Aug 10-25)</button>', 
                          '<button id="toggle-btn">Switch to Before (Aug 10-25)</button>\n        <button id="sar-btn" style="margin-top: 10px;">Load SAR Radar (See through clouds)</button>')

with open("index.html", "w") as f:
    f.write(content)
