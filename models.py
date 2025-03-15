class User:
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

class Expense:
    def __init__(self, amount, date, category, description, user_email):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.user_email = user_email