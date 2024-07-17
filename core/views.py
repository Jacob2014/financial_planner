from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from machine_learning.predict import make_prediction

def index(request):
    return render(request, 'core/index.html')

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IncomeForm()
    return render(request, 'core/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'core/add_expense.html', {'form': form})

def report(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    return render(request, 'core/report.html', {'incomes': incomes, 'expenses': expenses})

def predict(request):
    prediction = make_prediction()
    return render(request, 'core/predict.html', {'prediction': prediction})
