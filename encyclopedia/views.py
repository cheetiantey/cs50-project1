from django.shortcuts import render

from . import util

import random
import markdown2
from django import forms
# from django.http import HttpResponse

class searchForm(forms.Form):
    entry = forms.CharField(label="Search Form")

class createForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={
        'style' : 'width:100%'}))

class editForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={
        'style' : 'width:100%'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def greet(request, name):
    entry = markdown2.markdown(util.get_entry(name))
    return render(request, "encyclopedia/greet.html", {
        "title": name, 
        "entry": entry
    })


def search (request):
    searchQuery = request.GET.get('query')
    results = []

    for entry in util.list_entries():
        if (str.lower(searchQuery) in str.lower(entry)):
            results.append(entry)

    return render(request, "encyclopedia/search.html", {
        "entries": results
    })


def create(request):
    if request.method == "POST":
            form = createForm(request.POST)

            if form.is_valid():
                title = form.cleaned_data["title"]

                content = form.cleaned_data["content"]

                if title in util.list_entries():
                    return render(request, "encyclopedia/error.html", {
                        "title": title
                    })
                util.save_entry(title, content)
                
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries()
                })
            
            else:
                return render(request, "encyclopedia/create.html", {
                    "form": form
                })

    return render(request, "encyclopedia/create.html", {
        "form": createForm()
    })

def edit(request, name):
    return render(request, "encyclopedia/edit.html", {
        "form": editForm(initial={'title': name, 'content': util.get_entry(name)}),
        "title": name
    })

def submit(request):
    if request.method == "POST":
        form = editForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]

            content = form.cleaned_data["content"]

            util.save_entry(title, content)
        
        return render(request, "encyclopedia/greet.html", {
                    "title": title,
                    "entry": markdown2.markdown(util.get_entry(title))
                })   

        
def randomPage(request):
    length = len(util.list_entries())
    entries = list(util.list_entries())
    title = entries[random.randrange(0, length)]
    return render(request, "encyclopedia/greet.html", {
        "title": title,
        "entry": markdown2.markdown(util.get_entry(title))
    })

# def foobar(request):
#     return HttpResponse("Hello, world")

