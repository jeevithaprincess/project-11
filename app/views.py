from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *


# Create your views here.
def register(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessRecordsForm()

    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
       tfd=TopicForm(request.POST)
       wfd=WebpageForm(request.POST)
       afd=AccessRecordsForm(request.POST)
       if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
          ntfd=tfd.save(commit=False)
          ntfd.save()
          nwfo=wfd.save(commit=False)
          nwfo.tname=ntfd
          nwfo.save()
          nafo=afd.save(commit=False)
          nafo.name=nwfo
          nafo.save()
          return HttpResponse('data is registered successfully')
       else:

            return HttpResponse('data is invalid')


    return render(request,'register.html',d)
