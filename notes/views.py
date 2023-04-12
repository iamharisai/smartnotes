from django.shortcuts import render
from .models import Notes
from django.http import Http404
# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render (request,'notes/notes_list.html',{'notes': all_notes})

#This will return details of single notes http://127.0.0.1:8000/smart/notes/3
def details(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
        
    except Notes.DoesNotExist:
        raise Http404
    return render(request,'notes/notes_details.html',{'note':note})