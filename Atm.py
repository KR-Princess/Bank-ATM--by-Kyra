class ATM:
    def __init__(self, card_no, pin_no):
        self.card_no= card_no
        self.pin_no= pin_no

    def CheckBalance(self):
            print("You have a balance of 100000 in your card!!")

    def CashWithdrawl(self, amount):
            new_amount= 100000- amount
            print("You have withdrawn $ " + str(amount) + ".  Your remaining balance is $ "+ str(new_amount) +" !!")

def main():
   card_no= input("Enter your card number: ") 
   pin_no= input("Enter your pin: ")
   User_1= ATM(card_no, pin_no)

   print("Choose your activity- ")
   choice= int(input("Enter 1 for Checking your balance, and 2 for Cash Withdrawl"))
   if choice==1:
       User_1.CheckBalance()
   elif choice==2:
       amount_choice= int(input('How much money do you want to withdraw?'))
       if amount_choice > 100000:
           print("Insufficient Balance!!")
       else:
           User_1.CashWithdrawl(amount_choice)


main()