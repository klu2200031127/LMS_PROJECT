from django.shortcuts import redirect,render

def BASE(requerst):
    return render(requerst,'base.html')

def HOME(requerst):
    return render(requerst,'home.html')

def ABOUT(requerst):
    return render(requerst,'about.html')

def SIGNUP(requerst):
    return render(requerst,'signup.html')

def COURSE(requerst):
    return render(requerst,'course.html')
def CONTACT(requerst):
    return render(requerst,'contact.html')

def ENROLL(requerst):
    return render(requerst,'enroll.html')
