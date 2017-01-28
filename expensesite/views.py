from django.shortcuts import render
from django.views.generic import ListView
from .models import Name
from .CSV_import import CSVopener
from django.http import HttpResponseRedirect, HttpRequest
from .table_creater import build_table


class NameList(ListView):
    queryset = Name.objects.all()
    template_name = 'expensetemplates/upload.html'

def ImportCsv(request):
    if request.method == "POST":
        CSVopener(request.FILES['CSV'])
        return HttpResponseRedirect('/expense/table')
    else:
        return HttpRequest("Nope")

def Table(request):
    context = build_table()
    return render(request,'expensetemplates/table.html',{'contextt': context})