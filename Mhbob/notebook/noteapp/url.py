from django.urls import path
from .views import NoteView , NoteDetail , AddNote



urlpatterns = [
    path('' , NoteView.as_view()),
    path('note/<pk>' , NoteDetail.as_view() , name='detail'),
    path('newnote' , AddNote , name='newnote'),
]