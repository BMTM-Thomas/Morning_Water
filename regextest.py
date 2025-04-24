import re

credit = "v= 10.46 TB11504277035398 10.78"
match = re.findall(r'(\d+\.\d+)\s*([TGMK]B)', credit)
unit = match[0][1]
credit = match[0][0]

print(credit)
print(f"zabbix: {credit} {unit}")