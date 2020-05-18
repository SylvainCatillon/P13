from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from plannings.forms import PlanningCreationForm
from plannings.models import GuestMail


@login_required
def create_planning(request):
    if request.method == 'POST':
        form = PlanningCreationForm(request.POST)
        if form.is_valid():
            planning = form.save()
            if planning.protected:
                guest_mails = request.POST.getlist('guest_mail')
                for mail in guest_mails:
                    try:
                        planning.guest_mails.add(GuestMail.objects.get(mail=mail))
                    except GuestMail.DoesNotExist:
                        planning.guest_mails.create(mail=mail)
            return HttpResponseRedirect(reverse(
                'plannings:created',kwargs={'planning_ekey': planning.ekey}))
    else:
        form = PlanningCreationForm(initial={'creator': request.user.pk})
    return render(request, 'plannings/create_planning.html', {'form': form})


def planning_created(request, planning_ekey): # Remplacer par TemplateView en créant link dans create??
    link = request.build_absolute_uri(reverse(
        'plannings:display', args=(planning_ekey,)))  # security hole? Remplacer par link = get_current_site(request) ou gestion desite framework: https://docs.djangoproject.com/en/3.0/ref/contrib/sites/#getting-the-current-domain-for-full-urls
    return render(request, 'plannings/created.html', {'link': link,})


def display_planning(request, planning_ekey):
    pass