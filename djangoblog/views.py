from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
   # return HttpResponse('hello masi , you are successfully')
   return render(request, 'About.html')
def Home(request):
  #  return HttpResponse('به صفحه اصلی خوش آمدید...')
     return render(request, 'Home.html')
