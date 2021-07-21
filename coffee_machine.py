class CoffeeMachine:
    coffee_ingredients = {'1': {'water': 250, 'milk': 0, 'beans': 16, 'money': 4},
                          '2': {'water': 350, 'milk': 75, 'beans': 20, 'money': 7},
                          '3': {'water': 200, 'milk': 100, 'beans': 12, 'money': 6}}

    def __init__(self, ml_water, ml_milk, no_beans, cups, money):
        self.ml_water = ml_water
        self.ml_milk = ml_milk
        self.no_beans = no_beans
        self.cups = cups
        self.money = money
        self.state = 0

    def __check_supplies(self, coffee_selection):
        ingredients = self.coffee_ingredients[coffee_selection]
        have_supplies = False
        if self.ml_water < ingredients['water']:
            print("Sorry, not enough water!")
        elif self.ml_milk < ingredients['milk']:
            print("Sorry, not enough milk!")
        elif self.no_beans < ingredients['beans']:
            print("Sorry, not enough coffee beans!")
        elif self.cups == 0:
            print("Sorry, not enough coffee cups!")
        else:
            have_supplies = True
        return have_supplies

    def __brew_some_coffee(self, coffee_selection):

        ingredients = self.coffee_ingredients[coffee_selection]

        if self.__check_supplies(coffee_selection):
            print("I have enough resources, making you a coffee!")
            self.ml_milk -= ingredients['milk']
            self.ml_water -= ingredients['water']
            self.no_beans -= ingredients['beans']
            self.cups -= 1
            self.money += ingredients['money']

    def __refill_machine(self, user_input):
        if self.state == 2:
            self.ml_water += user_input
            self.state = 3
        elif self.state == 3:
            self.ml_milk += user_input
            self.state = 4
        elif self.state == 4:
            self.no_beans += user_input
            self.state = 5
        elif self.state == 5:
            self.cups += user_input
            self.state = 0

    def display_prompt(self):
        if self.state == 0:  # Initial state
            return "Write action (buy, fill, take, remaining, exit):\n"
        if self.state == 1:  # prompt for type of coffee
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"
        if self.state == 2:
            return "Write how many ml of water you want to add:\n"
        if self.state == 3:
            return "Write how many ml of milk you want to add:\n"
        if self.state == 4:
            return "Write how many grams of coffee beans you want to add:\n"
        if self.state == 5:
            return "Write how many disposable coffee cups you want to add:\n"

    def process_user_input(self, user_input):
        if self.state == 0:
            if user_input == "buy":
                self.state = 1
            elif user_input == "remaining":
                self.__status()
            elif user_input == "fill":
                self.state = 2
            elif user_input == "take":
                self.__take_money()
            elif user_input == "exit":
                exit()

        elif self.state == 1:
            if user_input in ['1', '2', '3']:
                self.__brew_some_coffee(user_input)
            self.state = 0
        elif self.state > 1:
            self.__refill_machine(int(user_input))

    def __status(self):
        print(f"\nThe coffee machine has:\n"
              f"{self.ml_water} of water\n"
              f"{self.ml_milk} of milk\n"
              f"{self.no_beans} of coffee beans\n"
              f"{self.cups} of disposable cups\n"
              f"${self.money} of money\n")

    def __take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    user_selection = input(coffee_machine.display_prompt())
    coffee_machine.process_user_input(user_selection)
