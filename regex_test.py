import re
text = "446.51 MB / 50 GB"
match = re.findall(r'([\d.]+)(?:\s*([MGK]B))?', text)

print("demo",match[0][1],"demo")

# match = 