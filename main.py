import re
#Search for only numbers inside the string
our_numbers = "12345"
number_pattern = r"^\d+$"
if re.match(number_pattern, our_numbers):
    print("Our string contains only numbers")
else:
    print("Our string doesn't only contain numbers")

#Search for only letters inside the string
our_letters = "I love Python"
letter_pattern = r"^[a-zA-Z ]+$"
if re.match(letter_pattern, our_letters):
    print("Our string contains only letters")
else:
    print("Our string doesn't only contain letters")

#Search for capital letter at the start of the string
our_sentence = "Today will rain"
capital_pattern = r"^[A-Z]"
if re.match(capital_pattern, our_sentence):
    print(f"The sentence '{our_sentence}.' starts with a capital letter.")
else:
    print(f"The sentence '{our_sentence}.' doesn't start with a capital letter.")


#See if phone number starts with exactly '381'
phone_number = "38165533422"
phone_pattern = r"^381"
if re.match(phone_pattern, phone_number):
    print("The number starts with 381")
else:
    print("The number doesn't start with 381")

#Balkan countries have (381, 382, 385, 389), we can try to find for all of these with one pattern
other_phone_number = "38569787923"
balkan_pattern = r"^38(1|2|5|9)"
phone_match = re.match(balkan_pattern, other_phone_number)
phone_map = {
    "381" : "Serbia",
    "382" : "Montenegro",
    "385" : "Bosnia and Herzegovina",
    "389" : "Croatia"
}
if phone_match:
    prefix = "38" + phone_match.group(1)
    country = phone_map[prefix]
    print(f"The number is from {country} and it starts with {prefix}")




