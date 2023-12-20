import re
text = "My name is Khan i am not terrorist"
pattern = r"Khan"
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("Not found")
