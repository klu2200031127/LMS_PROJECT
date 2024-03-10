from django.shortcuts import redirect,render

def BASE(requerst):
    return render(requerst,'base.html')

def HOME(requerst):
    return render(requerst,'home.html')

def ABOUT(requerst):
    return render(requerst,'about.html')