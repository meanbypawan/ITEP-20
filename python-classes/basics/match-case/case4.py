n = int(input("Enter a number : "))
match n:
    case n if n > 0: print("Positive")
    case n if n < 0: print("Negative")
    case n if n == 0: print("Neither +ve nor -ve")