
#class user to store user name & password as a list
class User:
    def __init__(self, user_name, password):
        self.users = []
        self.current_user = None
        self.user_name = user_name
        self.user_password = password
        self.properties = []

#get prompts from person
    def run(self):
        response = input("What would you like to do? To add user [1], to change user [2], to add property [3], delete property [4], quit [5]: ")
        if response == "1":
            self.add_user()
        
        elif response == "2":
            self.change_user()

        elif response == "3":
            self.add_property()
        
        elif response == "4":
            self.remove_property()
        
        elif response == "5":
            print("Thank you for your time. Have a nice day!")
            
        else:
            print("Please enter a valid response.")


#loop through responses and have it store user info in a list with append 
    def add_user(self):
        user_name = input("What is your user name? ")
        user_password = input("What is your password? ")
        new_user = User(user_name, user_password)
        self.users.append(new_user)
        print(f"You have added {self.user_name} new user.")
    
    def change_user(self):
        pass

    def add_property(self):
        new_prop = Property()
        new_prop.run()
        self.properties.append(new_prop)
        new_prop.show()
        print(f"You have added {new_prop.name} to your properties.")

    def remove_property(self):
        del_prop = input("What property would you like to remove?")
        if del_prop in self.properties.remove(del_prop):
            pass
        else:
            print("Please enter a property on the list.")


#second class gathering info of the property and expenses/income, etc
#wanting to store the value in a dictionary to I can add the input together
class Property:
    def __init__(self):
        
        self.invest = 0
        self.rent = 0
        self.loss = 0
    
    def get_invest(self):
        down_pay = int(input("What is your down payment for this property?"))
        closing = int(input("What is your closing cost for this property?"))
        rehab = int(input("What was your budget to rehab this property?"))
        misc = int(input("Please input other costs not included above. "))

        self.invest = down_pay + closing + rehab + misc
    
    def get_income(self):
        rent = int(input("How much is rent?"))
        parking = int(input("How much do you charge for parking?"))
        laundry = int(input("How much do you collect for laundry?"))
        extra = int(input("Do you have additional income?"))

        self.rent = rent + parking + laundry + extra

    def get_expenses(self):
        mort = int(input("How much will your mortage be?"))
        add_tax = int(input("How much will your property taxes be?"))
        add_ins = int(input("How much will your propert insurance be?"))
        add_exp = int(input("How much are your other expenses?"))
        self.loss = mort + add_exp + add_tax + add_ins
    
    def show(self):
        print(f"Net profit equals{self.net_profit}and your roi is{self.roi}")


#ROI calc
    def calc_roi(self):
        # def ROI (invest, rent, loss):)
        self.net_profit = self.rent * 12 - self.loss
        self.roi = (self.net_profit/self.invest) * 100
        self.name = input("What would you like to call your property?")

    def run(self):
        self.get_invest()
        self.get_income()
        self.get_expenses()
        self.calc_roi()
x= User(1, 2)
x.run()        
