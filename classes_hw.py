class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def display_username(self):
        print(self.username)

    def display_email(self):
        print(self.email)

    def change_password(self):
        self.password = "Messi"
        print(self.password)

class Player:
    def __init__(self, username, hp, damage):
        self.username = username
        self.hp = hp
        self.damage = damage

    def display_username(self):
        print(self.username)

    def display_hp(self):
        print(self.hp)

    def display_damage(self):
        print(self.damage)

class BankAccount:
    def __init__(self, username, capital, interest_rate):
        self.username = username
        self.capital = capital
        self.interest_rate = interest_rate

    def display_bank_account_username(self):
        print(self.username)

    def display_bank_account_capital(self):
        print(self.capital)

    def display_bank_account_interest_rate(self):
        print(self.interest_rate)