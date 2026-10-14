#Count the number of words in a sentence
'''
s = "Indore is cleanest city of india"
s = s.split() # ["Indore","is","cleanest","city","of","india"]
print(f"Total words : {len(s)}")
'''
s = "Indore is cleanest city of india"
word = 1
for ch in s:
    if ch == " ":
        word += 1
print(f"Total word : {word}")        