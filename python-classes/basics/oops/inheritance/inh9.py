class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(C,B):
    pass

print(f"A MRO : {A.mro()}")
print(f"B MRO : {B.mro()}")
print(f"C MRO : {C.mro()}")
print(f"D MRO : {D.mro()}") # B,A,Object