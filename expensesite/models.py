from django.db import models

# date, category, employee name, employee address, expense description, pre-tax amount, tax name, and tax amount.

class MonthlyExpense(models.Model):
    year_month = models.CharField(max_length=7,default='')
    monthly_total = models.DecimalField(max_digits = 20, decimal_places = 2,null=True)

    def  __str__(self):
        return self.year_month

class Name(models.Model):
    monthlyexpense = models.ForeignKey(MonthlyExpense,on_delete=models.CASCADE, null=True)
    date = models.DateField()
    category = models.CharField(max_length = 150,default='')
    employee_name = models.CharField(max_length = 50,default='')
    employee_address = models.CharField(max_length = 200,default='')
    expense_description = models.CharField(max_length = 200,default='')
    pre_tax_amount = models.DecimalField(max_digits = 20, decimal_places = 2,null=True)
    tax_name = models.CharField(max_length = 30,default='')
    tax_amount = models.DecimalField(max_digits = 10, decimal_places = 2,null=True)

    def __str__(self):
        return self.employee_name

