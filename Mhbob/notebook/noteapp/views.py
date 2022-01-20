from re import template
from django.http import HttpResponse
from django.shortcuts import render
from .models import NoteModel
from .forms import NoteForm
from django.views import generic


class NoteView(generic.ListView):
    template_name = 'Note.html'
    context_object_name = 'notebook'

    def get_queryset(self):
        return NoteModel.objects.all()


class NoteDetail(generic.DeleteView):
    model = NoteModel
    template_name = 'notedetail.html'



def AddNote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            note = NoteModel.objects.create(title = title , content = content)
            note.save()
            return HttpResponse('A note was created')

    else:
        form = NoteForm()
        note = NoteModel.objects.all()

    context = {'form':form}
    return render(request , 'additem.html', context)


