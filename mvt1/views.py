
from contextvars import Context
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Context, Template, loader
from people.forms import PersonF
from people.models import Person
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def Home(request):
    template = loader.get_template('Home.html')
    render_template = template.render({})
    return HttpResponse(render_template)

def view_person(request):
    persona = Person.objects.all()
    template = loader.get_template('ver_personas.html')
    render_template = template.render({'persona': persona})
    return HttpResponse(render_template)

def listado_personas(request):
    listado_personas = Person.objects.all()
    return render(
        request, "ver_personas.html",
        {'listado_personas': listado_personas}
    )

@login_required
def crear_persona(request):
    if request.method == 'POST':
        formulario = PersonF(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            personan = Person(
                nombre=data['nombre'], 
                apellido=data['apellido'],
                Nrofav=data['Nrofav'],
                fecha_nac=data['fecha_nac']
            )
            personan.save()
            return redirect('listado_persona')
            
            
    formulario = PersonF()
    return render(
        request, 'create_person.html', 
        {'formulario': formulario}
    )
