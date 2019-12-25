from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login/index.html',{ 'title':'Login'})
def about(request):
    return render(request,'about/about.html',{ 'title':'About_Developers'})