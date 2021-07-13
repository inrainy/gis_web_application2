from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import NewModel


def hi_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:hi_world'))
    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hi_world.html',
                      context={'data_list':data_list})

