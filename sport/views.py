from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Sport
from django.urls import reverse, reverse_lazy
from django.views import generic


# Create your views here.
def error_404(request, exception):
    return render(request, 'error.html', {'error_message': 'Eroare'})

class SportsView(generic.ListView):
    template_name = 'all_sports.html'
    context_object_name = 'sports'

    def get_queryset(self):
        return Sport.objects.all()


class SportDetailView(generic.DetailView):
    model = Sport
    template_name = 'sport_detail.html'


class SportCreateView(generic.CreateView):
    model = Sport
    fields = ['name', 'type', 'gender', 'shape']
    success_url = reverse_lazy('sports:all_sports')

    def form_invalid(self, form):
        print(form)
        return HttpResponseRedirect(reverse_lazy('sports:all_sports'))
