from core.models import Income, Expense

def add_income(date, amount, source):
    income = Income(date=date, amount=amount, source=source)
    income.save()

def add_expense(date, amount, category):
    expense = Expense(date=date, amount=amount, category=category)
    expense.save()

def get_incomes():
    return Income.objects.all()

def get_expenses():
    return Expense.objects.all()
