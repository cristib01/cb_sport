from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Sport
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required


# Create your views here.
def error_404(request, exception):
    return render(request, 'error.html', {'error_message': 'Eroare'})

@login_required(login_url='/logare')
def sports(request):
    sports_list = Sport.objects.filter(user=request.user)
    return render(request, template_name='all_sports.html', context={'sports': sports_list})

@login_required(login_url='/logare')
def sport_detail(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    return render(request, 'sport_detail.html', {'sport': sport})

@login_required(login_url='/logare')
def logged_in_user(request):
    user = request.user
    return render(request,'logged_on.html', {'user': user})
@login_required(login_url='/logare')
def sport_add(request):
    if request.method == 'POST':
        try:
            user = request.user
            sport = Sport(
                user=user,
                name=request.POST['name'],
                type=request.POST['type'],
                gender=request.POST['gender'],
                shape=request.POST['shape']
            )
            sport.save()

        except KeyError:
            return render(request, 'error.html', {'error_message': 'Invalid sport details'})

    return HttpResponseRedirect(reverse('sports:all_sports'))

# @login_required(login_url='/logare') - non functional
# class SportsView(generic.ListView):
#     template_name = 'all_sports.html'
#     context_object_name = 'sports'
#
#     def get_queryset(self):
#         return Sport.objects.all()

# @login_required() - non functional
# class SportDetailView(generic.DetailView):
#     model = Sport
#     template_name = 'sport_detail.html'
#
# @login_required() - non functional
# class SportCreateView(generic.CreateView):
#     model = Sport
#     fields = ['name', 'type', 'gender', 'shape']
#     success_url = reverse_lazy('sports:all_sports')
#
#     def form_invalid(self, form):
#         print(form)
#         return HttpResponseRedirect(reverse_lazy('sports:all_sports'))
