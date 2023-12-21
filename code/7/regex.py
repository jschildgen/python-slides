import re
text = "Ich studiere Mathe im 2. Semester"
print(re.findall(r"\w+e\w*", text))   # ['studiere', 'Mathe', 'Semester']
print(re.split(r"\s", text))  # ['Ich', 'studiere', 'Mathe', 'im', '2.', 'Semester']
print(re.sub(r"[aeiou]", "u", text))  # Ich studuuru Muthu um 2. Sumustur
if re.search(r"\d", text):
    print("Zahl gefunden")