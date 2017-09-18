from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("book index")


def detail(request,p1,p2,p3):
    return HttpResponse("year:%s month:%s day:%s" % (p1,p2,p3))


def gettest(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1= request.GET['c']
    dlist = request.GET.getlist('d')
    context = {'a':a1,'b':b1,'c':c1,'d':dlist}
    return render(request,'test1.html',context)


def index2(request):
    return JsonResponse({'key':"出来",'key1':232})
