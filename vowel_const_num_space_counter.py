para = input("Enter Paragraph :").lower()

vowel = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
num = "1234567890"
space = " "

vowel_count = 0
consonants_count = 0
num_count = 0
space_count = 0
syambol_count = 0

num_box = ""

for char in para:
    if char in vowel:
        vowel_count += 1
    elif char in consonants:
        consonants_count += 1
    elif char in num:
        num_count += 1
        num_box += char
    elif char in space:
        space_count += 1
    else:
        syambol_count += 1

print("In This Paragraph")
print(f"Vowel Count is: {vowel_count}")
print(f"Consonant Count is: {consonants_count}")
print(f"Number Count is: {num_count}")
print(f"Space Count is: {space_count}")
print(f"Special Symbol is: {syambol_count}")

print()

longest_sentence = ""
words = para.split(" ")
for word in words:
    if len(word) > len(longest_sentence):
        longest_sentence = word

print("In This Paragraph The Longest Sentence is: ")
print(f">> {longest_sentence}")
print(f">> Length Of String is: {len(longest_sentence)}")

print()

print("In This Paragraph The Number Used: ")
if num_box:
    for n in num_box:
        print(n)
else:
    print(f">> Number Not Found")

print()
print("This is reverse paragraph: ")
reverse_str = ""
for char in para:
    reverse_str = char + reverse_str
print(f">> {reverse_str}")