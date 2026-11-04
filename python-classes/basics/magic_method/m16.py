import gc
print(f"isEnabled : {gc.isenabled()}") # True
gc.disable()
print(f"isEnabled : {gc.isenabled()}") # False
gc.enable()
print(f"isEnabled : {gc.isenabled()}") # True
# class Test:
#     def __init__(self):
#         print("init called...")

#     def __del__(self):
#         print("del called...")    
