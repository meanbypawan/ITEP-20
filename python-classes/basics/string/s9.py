s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not Anagram")
else:
    d1 = {}
    d2 = {}
    for ch in s1:
        d1[ch] = d1.get(ch,0)+1
         
    for ch in s2:
        d2[ch] = d2.get(ch,0)+1

    print(f"d1 : {d1}")
    print(f"d2 : {d2}")
    if d1 == d2:
        print("Anagram")
    else:
        print("Not Anagram")                