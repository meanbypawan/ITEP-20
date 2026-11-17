from abc import ABC,abstractmethod

# Developer
class MakePayment(ABC):
    @abstractmethod
    def payment(self):
        pass

# Programmer - 1
class NetBanking(MakePayment):
    def payment(self,payment):
        print(f"Payment using NetBanking : {payment}")

# Programmer - 2
class UPI(MakePayment):
    def payment(self,payment):
        print(f"Payment using UPI : {payment}")

# Programmer - 3
class CreditCard(MakePayment):
    def payment(self,payment):
        print(f"Payment using Credit Card : {payment}")

# End user
print("1 for using NetBanking")
print("2 for using UPI")
print("3 for Credit card\nEnter choice : ")
choice = int(input())
pay = None
if choice == 1:
    pay = NetBanking()
elif choice == 2:
    pay = UPI()
    
elif choice == 3:
    pay = CreditCard()

pay.payment(5000)