from django.shortcuts import render


def home(request):
    return render(request, 'LCP1.html')
def result(request):
    # here machine learning code write
    return render(request,'LCP1.html')