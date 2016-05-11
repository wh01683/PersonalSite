from django.shortcuts import render


# Create your views here.
def contact(request):
    context = {
        'title': "Contact Me",
        'email': 'whowertoniii@gmail.com',
        'mobile_phone': '+1 (478) 390-2179',
    }
    return render(request, 'home/contact.html', context)


def about(request):
    context = {
        'title': 'About Me',
        'p1': "I am a Software Engineer Asc. working for Lockheed Martin in Ashburn, VA. More to come.",
    }
    return render(request, 'home/about.html', context)


def home(request):
    context = {
        'title': "Howerton's Page",
        'p1': "This is a living resume for William Robert Howerton III.",
    }
    return render(request, 'home/home.html', context)
