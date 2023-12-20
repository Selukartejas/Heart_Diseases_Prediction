from django.shortcuts import render
import joblib
# Create your views here.
def homes(request):
    return render(request, 'heart/homes.html')

def login(request):
    return render(request, 'heart/login.html')

def signup(request):
    return render(request, 'heart/signup.html')

def input(request):
    return render(request, 'heart/input.html')

def feedback(request):
    return render(request, 'heart/feedback.html')

def result(request):
    cls =joblib.load('finalmodel1.sav')
    lis = []
    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['cp'])
    lis.append(request.GET['trestbps'])
    lis.append(request.GET['chol'])
    lis.append(request.GET['thalach'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['ca'])
    lis.append(request.GET['thal'])
    print(lis)

    ans = cls.predict([lis])
    return render(request, 'heart/result.html',{'ans':ans})
    #
