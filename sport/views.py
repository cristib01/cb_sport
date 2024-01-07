from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Sport
from django.urls import reverse, reverse_lazy
from django.views import generic


# Create your views here.

# def index(request):
#     return HttpResponse('Sport says hello!')


# def sports(request):
#     sports_list = Sport.objects.all()
#     return render(request, template_name='all_sports.html', context={'sports': sports_list})
#
#
# def sport_detail(request, sport_id):
#     sport = get_object_or_404(Sport, pk=sport_id)
#     return render(request, 'sport_detail.html', {'sport': sport})


def error_404(request, exception):
    return render(request, 'error.html', {'error_message': 'Eroare'})


# def sport_add(request):
#     sport_details = request.POST.dict()
#     try:
#         sport = Sport(name=sport_details['name'], type=sport_details['type'], gender=sport_details['gender'],
#                       shape=sport_details['shape'])
#         sport.save()
#     except KeyError:
#         return render(request, 'error.html', {'error_message': 'Invalid sport details'})
#     return HttpResponseRedirect(reverse('sports:all_sports'))

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
