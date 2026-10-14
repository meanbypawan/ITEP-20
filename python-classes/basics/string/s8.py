s1 = "aaba"
s2 = "aabaa"

if len(s1) != len(s2):
    print("String not equals")
else:
    for i in range(len(s1)):
        if ord(s1[i]) - ord(s2[i]):
            print("Not equals")
            break
    else:
        print("Equals")               


