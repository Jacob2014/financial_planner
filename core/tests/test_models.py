from django.test import TestCase
from core.models import Income, Expense

class IncomeModelTest(TestCase):

    def setUp(self):
        Income.objects.create(date='2024-01-01', amount=100.00, source='Salary')

    def test_income_creation(self):
        income = Income.objects.get(source='Salary')
        self.assertEqual(income.amount, 100.00)

class ExpenseModelTest(TestCase):

    def setUp(self):
        Expense.objects.create(date='2024-01-01', amount=50.00, category='Groceries')

    def test_expense_creation(self):
        expense = Expense.objects.get(category='Groceries')
        self.assertEqual(expense.amount, 50.00)
