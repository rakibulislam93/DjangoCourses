from django.shortcuts import render

# Create your views here.

def index(request):
    
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "they are either to do repels provide blacked out except the option criticizes",
            "body": "because it receives it takes the consequences of refusing to be expedient and when He blames the whole trouble for what it is. 'Ours is a matter of fact, but it is the matter that will happen to the architect.'"
        },
        {
            "userId": 1,
            "id": 2,
            "title": "who is being",
            "body": "it is the time of life of things. to follow them, nothing blames the pain of the blessed ones nor those pains let him avoid flattery with pleasure, or no trouble so as to be rejected those who do not have to open, we cannot, those who do not"
        },
        {
            "userId": 1,
            "id": 3,
            "title": "she repels troubles as if she were training, whoever she is",
            "body": "and just but with what right the pleasure of being blinded by every choice or ad who is spared the pleasure of pains or accusers his trouble, and his hatred and toil, and whether he will"
        },
        {
            "userId": 1,
            "id": 4,
            "title": "and he is blinded",
            "body": "get pleasure by rejecting any and often but it is important to assume that they provide the fault of things those who do not know the benefits here are bound by the law and the pain itself who wants the pleasure of those things"
        },
        {
            "userId": 1,
            "id": 5,
            "title": "they do not know what they hate",
            "body": "he seeks forgiveness for repudiation but he may flee otherwise, but he is. We can all be pleasures it is either pain is held or not"
        }
    ]

    return render(request, 'index.html', {'data': data})

def about(request,id):
    return render(request,'index.html',{'id':id})