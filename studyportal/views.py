import uuid

import requests
import wikipedia
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from youtubesearchpython import VideosSearch
from django.contrib.auth.decorators import login_required
import random


def index(request):
    return render(request, "home.html")


def home(request):
    return render(request, "home.html")


@login_required()
def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], desc=request.POST['desc'])
            notes.save()
        name = request.user.username
        name = name.title()
        messages.success(request, f"{name} Your Notes Have Been Added Successfully!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, "notes.html", context)


@login_required()
def delete_notes(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


def youtube(request):
    if request.method == "POST":
        form = PanelForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=20)
        results = []
        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            results.append(result_dict)
            context = {'form': form,
                       'results': results}
        return render(request, "youtube.html", context)
    else:
        form = PanelForm()
    context = {'form': form}
    return render(request, "youtube.html", context)


@login_required()
def todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todos = Todo(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            todos.save()
            name = request.user.username
            name = name.title()
            messages.success(request, f"{name} Your Todo Has Been Added!!")
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False
    context = {'todos': todo, 'form': form, 'todos_done': todos_done}
    return render(request, "todo.html", context)


@login_required()
def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect("todo")


@login_required()
def delete_todo(request, pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect("todo")


def books(request):
    if request.method == "POST":
        form = PanelForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q=" + text
        r = requests.get(url)
        answer = r.json()
        results = []
        for i in range(10):
            result_dict = {
                'title': answer['items'][i]['volumeInfo']['title'],
                'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                'description': answer['items'][i]['volumeInfo'].get('description'),
                'count': answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories': answer['items'][i]['volumeInfo'].get('categories'),
                'rating': answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail': answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview': answer['items'][i]['volumeInfo'].get('previewLink'),
            }
            results.append(result_dict)
            context = {'form': form,
                       'results': results}
        return render(request, "books.html", context)
    else:
        form = PanelForm()
    context = {'form': form}
    return render(request, "books.html", context)


@login_required()
def dictionary(request):
    if request.method == "POST":
        form = PanelForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + text
        r = requests.get(url)
        answer = r.json()
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context = {
                'form': form,
                'input': text,
                'phonetics': phonetics,
                'audio': audio,
                'definition': definition,
                'example': example,
                'synonyms': synonyms
            }
        except:
            context = {
                'form': form,
                'input': ''
            }
        return render(request, "dictionary.html", context)
    else:
        form = PanelForm()
        context = {'form': form}
    return render(request, "dictionary.html", context)


@login_required()
def wiki(request):
    if request.method == "POST":
        text = request.POST['text']
        form = PanelForm(request.POST)
        try:
            search = wikipedia.page(text)
        except wikipedia.exceptions.DisambiguationError as e:
            s = random.choice(e.options)
            print(s)
            search = wikipedia.page(s)
        context = {
            'form': form,
            'title': search.title,
            'link': search.url,
            'details': search.summary
        }
        return render(request, 'wiki.html', context)
    else:
        form = PanelForm()
        context = {'form': form}
    return render(request, 'wiki.html', context)


def registerUser(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = username
            name = name.title()
            messages.success(request, f"{name} Your Account Has Been Created Successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@login_required()
def profile(request):
    todos = Todo.objects.filter(is_finished=False, user=request.user)
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    context = {
        'todos': todos,
        'todos_done': todos_done
    }
    return render(request, 'profile.html', context)
