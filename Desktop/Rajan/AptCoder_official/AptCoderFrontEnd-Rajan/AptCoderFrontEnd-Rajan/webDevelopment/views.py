from django.shortcuts import render

# Create your views here.


def homepage(request):
    print("Reached homepage")
    return render(request, 'webDevelopment/homepage.html')
    
def homepage2(request):
    print("Reached homepage2")
    return render(request, 'webDevelopment/homepage2.html')

def buddy2(request):
    print("Reached homepage2")
    return render(request, 'webDevelopment/buddy2.html')

def aboutpage(request):
    print("Reached aboutpage")
    return render(request, 'webDevelopment/about.html')


def blogpage(request):
    print("Reached blogpage")
    return render(request, 'webDevelopment/blog.html')


def contactpage(request):
    print("Reached contactpage")
    return render(request, 'webDevelopment/contact.html')


def coursespage(request):
    print("Reached coursespage")
    return render(request, 'webDevelopment/cource.html')


def singleblogpage(request):
    print("Reached singleblogpage")
    return render(request, 'webDevelopment/singleblog.html')


def elementspage(request):
    print("Reached elementspage")
    return render(request, 'webDevelopment/elements.html')


def coursedetailspage(request):
    print("Reached coursedetailspage")
    return render(request, 'webDevelopment/courseDetails.html')

def kiddopage(request):
    print("Reached kiddopage")
    return render(request, 'webDevelopment/kiddo.html')

def buddypage(request):
    print("Reached buddypage")
    return render(request, 'webDevelopment/buddy.html')

def propage(request):
    print("Reached propage")
    return render(request, 'webDevelopment/pro.html')

def trialpage(request):
    print("Reached trialpage")
    return render(request, 'webDevelopment/trialpage.html')

def chartpage(request):
    print("Reached chartpage")
    return render(request, 'webDevelopment/charts.html')


def dashboard(request):
    print("Reached dashboard")
    return render(request, 'webDevelopment/dashboard.html')