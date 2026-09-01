import re

with open("index.html", "r") as f:
    content = f.read()

# Use regex to remove the draw-panel div
pattern = re.compile(r'<div id="draw-panel".*?</div>', re.DOTALL)
content = re.sub(pattern, '', content)

with open("index.html", "w") as f:
    f.write(content)
