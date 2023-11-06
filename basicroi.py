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
        response = input("What do you want to do? Add user press 1, change user press 2, add property 3, delete property 4, quit 5")
        if response == "3":
            self.add_property()


#loop through responses and have it store user info in a list with append 
    def add_user(self):
        user_name = input("What is your user name? ")
        user_password = input("What is your password? ")
        new_user = User(user_name, user_password)
        self.users.append(new_user)
    
    def change_user(self):
        pass

    def add_property(self):
        new_prop = Property()
        new_prop.run()
        self.properties.append(new_prop)
        new_prop.show()
        print(f"You have added {new_prop.name} to your properties.")

    def remove_property(self):
        pass

#second class gathering info of the property and expenses/income, etc
#wanting to store the value in a dictionary to I can add the input together
class Property:
    def __init__(self):
        
        self.invest = 0
        self.rent = 0
        self.loss = 0
    def get_invest(self):
        response = int(input("What is your investment?"))
        self.invest = response
    
    def get_income(self):
        rent = int(input("How much is the rent?"))
        extra = int(input("Other income you collect"))
        self.rent = rent + extra

    def get_expenses(self):
        mort = int(input("How much will your mortage be?"))
        add_exp = int(input("How much are your other expenses?"))
        self.loss = mort + add_exp 
    def show(self):
        print(f"Net profit equals {self.net_profit} and your roi is {self.roi}")


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

        # self.income = {}
        # self.name = " "
        # self.total_expenses = 0
        # self.total_income = 0
        # self.down_payment = 0
        # self.closing_costs = 0 = 
        # self.rehab = 0
        # self.roi = 0
        # self.properties = []


# #ROI calc
#     def calc_roi(self):
#         pass
# #         def ROI (invest, rent, loss):
# #         NetProfit = rent * 12 - loss
# #         ROI = (NetProfit/invest(down pay, closing, rehab)) * 100
    