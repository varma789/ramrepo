from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime

date1=datetime.datetime.now()

def main_page(request):
    return render(request,'base.html')


def home_page(request):
    return render(request,'home.html' )


def contact_page(request):
    return render(request,'contact.html')


def courses_page(request):
    return render(request,'courses.html')


def feddback_page(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get("name",'')
            rating=request.POST.get("rating",'')
            feedback=request.POST.get("feedback",'')
            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform=FeedbackForm()
            fdata=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse("Invali data")
    else:
        fform = FeedbackForm()
        fdata = FeedbackData.objects.all()
        return render(request, 'feedback.html', {'fform': fform, 'fdata': fdata})



def team_page(request):
    return render(request,'team.html')


def gallery_page(request):
    return render(request,'gallery.html')


