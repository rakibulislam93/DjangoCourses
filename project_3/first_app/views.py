from django.shortcuts import render

# Create your views here.

def home(request):

    d = {'author' : 'rakib','age' : 25 ,'val': ['python','is','fun'] ,'lst':[1,2,3,4],'courses':[
        {
            'id': 1,
            'name': 'python',
            'fee': 5000
        },
        {
            'id': 2,
            'name': 'Django',
            'fee' : 10000
        },
        {
            'id': 3,
            'name': 'C',
            'fee' : 2000
        }
    ]}

    # context
    return render(request,'home.html',d)