ch = input("Enter a character : ")
match ch:
    case "a"|"e"|"i"|"o"|"u": print("Vowel")
    case _: print("Not vowel")