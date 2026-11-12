class J5:
    def receiving_call(self):
        print("Call received...")
    def rejecting_call(self):
        print("Call rejected...")

class J7(J5):
    def camera(self):
        print("camera is onn..")

j7 = J7()
j7.receiving_call()
j7.rejecting_call()
j7.camera()        