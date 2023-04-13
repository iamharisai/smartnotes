from django.shortcuts import render
from .models import Notes
from .forms import NotesForm
from django.http import Http404,HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes' #By default object_list will be passed
    template_name = 'notes/notes_list.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


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

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'