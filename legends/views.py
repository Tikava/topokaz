from django.shortcuts import render
from .models import Legend

def index(request):
    legends = Legend.objects.all()
    return render(request, 'legends/index.html', {'legends': legends})

def legend_detail(request, legend_id):
    legend = Legend.objects.get(id=legend_id)
    return render(request, 'legends/legend_detail.html', {'legend': legend})
