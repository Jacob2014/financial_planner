from django.test import TestCase
from django.urls import reverse

class CoreViewsTest(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Financial Planner")

    def test_add_income_view(self):
        response = self.client.get(reverse('add_income'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Income")

    def test_add_expense_view(self):
        response = self.client.get(reverse('add_expense'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Expense")

    def test_report_view(self):
        response = self.client.get(reverse('report'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Financial Report")

    def test_predict_view(self):
        response = self.client.get(reverse('predict'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Financial Prediction")
