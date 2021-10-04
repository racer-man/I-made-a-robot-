class Student(object):
    def __init__(self, name, age, cardnum, pin, ):
        self.name = name
        self.age = age
        self.cardnum = cardnum
        self.pin = pin
    def CashWithdrawl (self, cashOut):
        self.cashOut = cashOut
    
#Now we do the Magic bit.Now Now, you don't need to mess it up or else it will malfunction
#please type this: Hi, can i check the balance in my bank account?
print("Hello I am Python AI, How Can I help you?")
input("User: ")
print("Python AI: Your current balance is ___.___$")
input("User: ")
print("Python AI: You are welcome")
input("Python AI: Enter the ammount of money you want to withdraw: ")
print("Python AI: The money you wanted is now going to come out from the box please take it before you leave. Good bye, Come again soon!")
input("User: ")
