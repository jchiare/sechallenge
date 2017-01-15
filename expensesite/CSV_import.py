import csv
from .forms import ItemModelForm


def import_csv(filename):
    rows = open(filename)

    # Generate a dict per row, with the first CSV row being the keys.
    for row in csv.DictReader(rows, delimiter=","):

        # Bind the row data to the ItemModelForm
        form = ItemModelForm(row)
        if form.is_valid():
            model_instance = form.save()
            model_instance.save()
        else:
            pass

    return