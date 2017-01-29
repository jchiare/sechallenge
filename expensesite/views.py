from django.views.generic import ListView, TemplateView
from .models import MonthlyExpense
from .CSV_import import CSVopener
from django.http import HttpResponseRedirect, HttpRequest


class HomePage(TemplateView):
    template_name = 'expensetemplates/upload.html'

class MonthlyExpenseList(ListView):
    queryset = MonthlyExpense.objects.all()
    template_name = 'expensetemplates/table.html'

def ImportCsv(request):
    if request.method == "POST":
        CSVopener(request.FILES['CSV'])
        return HttpResponseRedirect('/expense/table')
    else:
        return HttpRequest("Nope")
