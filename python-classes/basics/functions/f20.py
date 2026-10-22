def f1(l):
    def f2(w):
        def f3(h):
            return l * w * h
        return f3
    return f2


# f2 = f1(2)
# f3 = f2(3)
# result = f3(4)
result = f1(2)(3)(4) # Chained function call
print(f"Result : {result}")