import csv
from .models import Name, MonthlyExpense
import io
from decimal import Decimal

def CSVopener(file):
    new_file = io.StringIO(file.read().decode('utf-8')) # (mostly) black magic

    with new_file as f:
        reader = csv.reader(f)
        next(reader,None)

        for row in reader:

            date_seperator = row[0].split('/') # horrible hack to avoid using a modelform
            item_date = date_seperator[2] + "-" + date_seperator[0]

            row[5] = row[5].replace(",","") # fuck commas
            row[7] = row[7].replace(",","")
            item_total = Decimal(row[5]) + Decimal(row[7])

            # create Name object
            Name.objects.create(
                date= item_date + "-01",
                category=row[1],
                employee_name=row[2],
                employee_address= row[3],
                expense_description= row[4],
                pre_tax_amount= row[5],
                tax_name= row[6],
                tax_amount= row[7],
            )

            # create MonthlyExpense object or add amount to monthly total
            instance, month_does_not_exist = MonthlyExpense.objects.get_or_create(year_month=item_date)
            if month_does_not_exist:
                instance.monthly_total = item_total
                instance.save()
            else:
                instance.monthly_total += item_total
                instance.save()

    return


