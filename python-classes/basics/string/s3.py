s = "Indore MP"
#vowel = "aeiouAEIOU"
vowel = {'a','e','i','o','u','A','E','I','O','U'}
vowel_count = consonent_count = 0

for ch in s:
    if ch in vowel:
        vowel_count += 1
    elif ch.isalpha():
        consonent_count += 1
print(f"Vowel count : {vowel_count}")
print(f"Consonent Count : {consonent_count}")             
