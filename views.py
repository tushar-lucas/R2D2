from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render
from .forms import personmodel
from .models import person

def save(request):
    c=personmodel(request.POST)
    if c.is_valid():
        c.save()
    c=personmodel()
    return render(request,'DemoApp/first.html',{'b':c})
def search(request):
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:

            match = person.objects.filter(Q(name__icontains=srch)|Q(rating__icontains=srch))
            if match:
                return render(request, 'DemoApp/index.html',{'obj':match})
        else:
            return HttpResponseRedirect('search')
    return  render(request,'DemoApp/index.html')


