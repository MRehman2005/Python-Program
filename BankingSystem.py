class Bank:
    Name = ''
    Address = ''
    Location = ''
    def set_Data_Bank(self,Name,Address,Location):
        self.Name = Name
        self.Address = Address
        self.Location = Location
    def get_Bank_Data(self):
        print(f"Name:{self.Name}")
        print(f"Address:{self.Address}")
        print(f"Location:{self.Location}")
        
    
class Customer:
    Name = ''
    Address = ''
    Cnic = 0
    Total_balance = 0
    def set_Customer_Data(self,Name,Address,Cnic,Total_balance):
        self.Name = Name
        self.Address = Address
        self.Total_balance = Total_balance
        self.Cnic = Cnic
        # Current Blance 
    def get_current_balance(self):
        print(f"Current Balnce:{self.Total_balance}")
        # Width Darw
    def Width_darw_Amount(self,Amount):
        self.Total_balance-=Amount
        print(f"WithDraw Amount :{Amount} Current Blance :{self.Total_balance}" )
        # Add Amount
    def Add_Amount(self,Amount):
        self.Total_balance+= Amount
    def get_Customer_Data(self):
        print(f"Name:{self.Name}")
        print(f"Address:{self.Address}")
        print(f"Cnic:{self.Cnic}")
        print(f"Blance{self.Total_balance}")
class NewCustomer:
    pass

bank = Bank()
customer = Customer()
print("Enter your Choice")
print("1.Implimentaion Of Class Bank")
print("2.Implimentation Of Class Customer")

choice = int(input())
if choice == 1:
    bank.set_Data_Bank("HBL","GT.Road","Lahore")
    print("Data is being Implemented of class Bank")
elif choice == 2:
    print("Enter the Data of the Customer")
    print("-"*30)
    Name = input("Enter The Name of the customer:")
    Address = input("Enter The Address of the customer:")
    Cnic = int(input("Enter The Cnic of the Customer:"))
    Blance = int(input("Enter The Balnce of the Customer:"))
    customer.set_Customer_Data(Name,Address,Cnic,Blance)
    print("Data is Successfully To Save")
else :
    print("Error")

# Get Data
print("1. Display The Data of the Bank")
print("2. Display The Data of the Customer")
choice = int(input())
if choice == 1:
    print("Here Bank Data")
    print("-"*20)
    bank.set_Data_Bank("HBL","GT-Road","Lahore")
    bank.get_Bank_Data()
elif choice == 2:
    print("Here Customer Data")
    print("-"*30)
# For Withdraw Add CurrentAmount
    print("1.For Current Balnce")
    print("2.For Add Balance")
    print("3 For WithDraw Amount")
    print("4 For Customer Data")
    choice = int(input())
if choice == 1:
    customer.get_current_balance()
elif choice == 2:
    amount = int(input("Enter Amount That You Wnat to Add"))
    customer.Add_Amount(amount)
    print("Amount Added")
elif choice == 3:
    amount = int(input("Enter withdraw amount"))
    customer.Width_darw_Amount(amount)
elif choice == 4:
    customer.get_Customer_Data()
else:
    print("SomeThing went's Worng")
    
    

    
    
    
        
        
        
        


