import csv
from .models import Name
import io

def CSVopener(file):
    new_file = io.StringIO(file.read().decode('utf-8')) # (mostly) black magic

    with new_file as f:
        reader = csv.reader(f)
        next(reader,None)

        for row in reader:
            date_seperator = row[0].split('/') # horrible hack to let model.datefield work
            Name.objects.create(
                date= date_seperator[2] + "-" + date_seperator[0] + "-01",
                category=row[1],
                employee_name=row[2],
                employee_address= row[3],
                expense_description= row[4],
                pre_tax_amount= row[5].replace(",",""), # fuck commas
                tax_name= row[6],
                tax_amount= row[7].replace(",",""),
            )

    return


