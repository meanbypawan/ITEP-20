class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C):
    pass

class F(D,E):
    pass
print(f"A MRO : {A.mro()}")
print(f"B MRO : {B.mro()}")
print(f"C MRO : {C.mro()}")
print(f"D MRO : {D.mro()}") # B,A,Object
print(f"E MRO : {E.mro()}")
print(f"F MRO : {F.mro()}")