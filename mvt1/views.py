
from contextvars import Context
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader

from people.models import Person

def Home(request):
    template = loader.get_template('Home.html')
    render_template = template.render({})
    return HttpResponse(render_template)

def create_person(request):
    persona1 = Person(nombre="Lujan", apellido="Ortega", edad=24, fecha_consulta=datetime.now())
    persona2 = Person(nombre="Veronica", apellido="Paredes", edad=21, fecha_consulta=datetime.now())
    persona3 = Person(nombre="Beatriz", apellido="Ramirez", edad=60, fecha_consulta=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()
    template = loader.get_template('create_person.html')
    render_template = template.render({})
    return HttpResponse(render_template)

def view_person(request):
    persona = Person.objects.all()
    template = loader.get_template('ver_personas.html')
    render_template = template.render({'persona': persona})
    return HttpResponse(render_template)