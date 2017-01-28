from .models import Name

def build_table():

    month_expense = {}

    for instance in Name.objects.all():
        year_month = str(instance.date.year) + "/" + str(instance.date.month)
        if month_expense.get(year_month) is not None:
            month_expense[year_month] += instance.tax_amount + instance.pre_tax_amount
        else:
            month_expense[year_month] = instance.tax_amount + instance.pre_tax_amount
    return month_expense
