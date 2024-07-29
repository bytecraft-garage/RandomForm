from django.shortcuts import render
from django.http import HttpResponse
from .models import querys

# Create your views here.
def home(request):
    
    if request.POST:
        query = request.POST['text']
        data = querys.objects.create(questions = query)
        data.save()
        print('saved Successfully')
    return render(request,'form.html')

def panel(request):
    data = querys.objects.all()
    context = {'data' : data}
    return render(request,'panel.html',context)

def delete(request,id):
    data = querys.objects.get(id = id)
    data.delete()
    data = querys.objects.all()
    return render(request,'panel.html',{'data':data})