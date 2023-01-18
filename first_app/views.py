from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import random
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from .models import Person

from django.template import loader

def list_people(request):
    all_people = Person.objects.all()
    template = loader.get_template('first_app/index.html')
    context = {
        "all_people": all_people
    }
    return HttpResponse(template.render(context, request))

def create_random_name(length):
    output = ""
    choices = "zxcvbnmasdfghjklqwertyuiop"
    for _ in range(length):
        output += random.choice(choices)
    return output
        

def add_new_person_template(request):
    template = loader.get_template('first_app/add_person.html')
    context = {}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def add_new_person(request):
    name = request.POST.get('name')
    Person.objects.create(name=name)
    return redirect("/list")

def delete_person(request, pk):
    Person.objects.get(id=pk).delete()
    return redirect("/list")

def edit_person_template(request, pk):
    person = Person.objects.get(id=pk)
    context = {"person": person}
    template = loader.get_template('first_app/edit_person.html')
    return HttpResponse(template.render(context, request))

@csrf_exempt
def edit_person(request, pk):
    person = Person.objects.filter(id=pk)
    person.update(name=request.POST.get('name'))
    return redirect("/list")