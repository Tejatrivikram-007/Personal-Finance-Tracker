from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    SOURCE_CHOICES = [
        ('Salary', 'Salary'),
        ('Freelance', 'Freelance'),
        ('Investments', 'Investments'),
        ('Loan',"Loan"),
        ('Other', 'Other'),
    ]
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)

    def _str_(self):
        return f"{self.source} - {self.amount}"

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Housing', 'Housing'),
        ('EMI','EMI'),
        ('Transportation', 'Transportation'),
        ('Food', 'Food'),
        ('Entertainment', 'Entertainment'),
        ('Hospital','Hospital'),
        ('Other', 'Other'),

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=200, blank=True)

    def _str_(self):
        return f"{self.category} - {self.amount}"

class Savings(models.Model):
    CATEGORY_CHOICES=[
        ('Emergency Fund', 'Emergency Fund'),
        ('Long-term Savings', 'Long-term Savings'),
        ('Short-term Savings', 'Short-term Savings'),
        ('LIC','LIC'),
        ('Other', 'Other'),

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()   
    description = models.CharField(max_length=200, blank=True)

    def _str_(self):
        return f"{self.category} - {self.amount}"
    
