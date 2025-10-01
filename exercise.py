#Check if name is in name, last_name format
import re

name = "Nikola Ticic"
pattern = r"[A-Z][a-z]+ [A-Z][a-z]$"
if re.match(pattern, name):
    print("The text satisfies the first, last name format.")
else:
    print("The name doesn't satisfy the first, last name format.")