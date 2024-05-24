from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
  peoples = [
    {'name': 'abid', 'age': 21},
    {'name': 'jaun', 'age': 10},
    {'name': 'muneer', 'age': 20},
    {'name': 'talha yunus', 'age': 26},
    {'name': 'faris shafi', 'age': 32},


  ]
  fruits = ['apple', 'mango', 'banana']
  return render(request , "index.html", context = {'page': 'django' , 'peoples': peoples, 'fruits' : fruits})
def about(request):
  context = {'page': 'About'}
  return render(request, "about.html", context)
def contact(request):
  context = {'page': 'Contact'}
  return render(request, "contact.html", context)
def success_page(request):
  return HttpResponse("<h1>Nahin toh<h1>")