from django.db import models

# date, category, employee name, employee address, expense description, pre-tax amount, tax name, and tax amount.

class Item(models.Model):
    date = models.DateField()
    category = models.CharField(max_length = 150)
    employee_name = models.CharField(max_length = 50)
    employee_address = models.CharField(max_length = 200)
    expense_description = models.CharField(max_length = 200)
    pre_tax_amount = models.DecimalField(max_digits = 20, decimal_places = 2)
    tax_name = models.CharField(max_length = 30)
    tax_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
