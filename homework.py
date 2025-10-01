#Check if the given word is an email
import re

email = "drjohn@gmail.com"
email_pattern = r"^[\w\.-]+@[\w\.-]+\.+\w+$"
if re.match(email_pattern, email):
    print("This string is an email")
else:
    print("This string isn't an email")