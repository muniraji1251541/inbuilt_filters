from django.shortcuts import render
import datetime
# Create your views here.


def inbuilt_filter(request):
    da=datetime.datetime.now()
    d={'data':'tHis iS dJAngO cLaSs','da':da,'fa':2}
    return render(request,'inbuilt_filter.html',d)