from django.shortcuts import render
from . forms import contactForm
from . forms import studentForm,passwordProject
# Create your views here.

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')

        return render(request,'contact.html',{'name': name , 'email': email , 'select':select })
    return render(request,'contact.html')

def submit_form(request):
    
    return render(request,'form.html')


def DjangoForm(request):
    if request.method=='POST':
        form = contactForm(request.POST,request.FILES)

        if form.is_valid():
        #     file = form.cleaned_data['file']
        #     with open('./first_app/upload/' + file.name, 'wb+')as destination:
        #         for chunck in file.chunks():
        #             destination.write(chunck)

            print(form.cleaned_data)
        # return render(request,'django_form.html',{'form':form})
    
    else:
        form = contactForm()
    return render(request,'django_form.html',{'form':form})



def djangoStudentForm(request):
    if request.method == 'POST':
        form = studentForm(request.POST,request.FILES)
        if form.is_valid():
            
            print(form.cleaned_data)
    else:
        form = studentForm()
        
    return render(request,'student_form.html',{'form': form})

def passwordValidation(request):
    if request.method == 'POST':
        form = passwordProject(request.POST)
        if form.is_valid():
            
            print(form.cleaned_data)
    else:
        form = passwordProject()
        
    return render(request,'student_form.html',{'form': form})