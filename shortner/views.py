from django import shortcuts
from django.core.checks import messages
from django.shortcuts import render, redirect
import random
from .models import urls

lcase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ucase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9','0']
lcase.extend(ucase)

lcase.extend(num)
b = lcase
n = 12

def verify(urlso):
    print(urlso)
    if urlso in urls.objects.all():
            return False
    return True

def geturl():
    while(True):
        url = random.sample(b,n)
        if verify("".join(url)):
            #print(url)
            return "".join(url)


def main(request):
    if request.method == 'POST':
        a = urls()
        #print(geturl())
        temp = request.POST.get('url')
        if('https://'in temp or 'http://'in temp):
            a.actual = temp
        else:
            temp2 = 'https://'+temp
            a.actual = temp2
        a.short = geturl()
        a.save()

        context = {
            'data' : a
        }
        return render(request,'success.html',context)
        return render(request,'form.html')
    return render(request,'form.html')

def forward(request,url):
    a = urls.objects.get(short = url)
    b = a.actual
    print(b)
    return redirect(b)