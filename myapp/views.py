from django.shortcuts import render
from .forms import Studentregi
# Create your views here.
def student(request):
    fm = Studentregi()
    return render(request,'myapp/addstudent.html',{'form':fm})