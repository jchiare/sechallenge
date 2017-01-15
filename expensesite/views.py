from django.shortcuts import render
from .models import Item
from .CSV_import import import_csv
# Create your views here.

def mainpage(request):
    if request.method == 'POST':
        import_csv(request.FILES['file'])
    else:
        pass
    return render(request, 'expensetemplates/upload.html')
