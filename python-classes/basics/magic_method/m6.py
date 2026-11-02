class Test:
    a = 100
    def __init__(self):
        self.b = 200

obj = Test()
print(f"a : {Test.a}")  # a is static
print(f"b : {obj.b}") # b is instance        