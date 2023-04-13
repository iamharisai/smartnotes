from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView,DetailView
# Create your views here.


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes' #By default object_list will be passed
    template_name = 'notes/notes_list.html'


# def list(request):
#     all_notes = Notes.objects.all()
#     return render (request,'notes/notes_list.html',{'notes': all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_detail.html'

#This will return details of single notes http://127.0.0.1:8000/smart/notes/3
# def details(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
        
#     except Notes.DoesNotExist:
#         raise Http404
#     return render(request,'notes/notes_details.html',{'note':note})