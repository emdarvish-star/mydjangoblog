from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def singup_view(request):
    form = UserCreationForm()
    return render(request,'account/singup.html',{'form':form})
