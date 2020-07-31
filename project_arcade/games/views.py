from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from subprocess import run, PIPE
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTERNAL_FILES = os.path.join(BASE_DIR, 'external_files')
ROCK_PAPER_SCISSORS = os.path.join(EXTERNAL_FILES, 'rock-paper-scissors')
HANGMAN = os.path.join(EXTERNAL_FILES, 'hangman')

print(BASE_DIR)
# Create your views here.

def index(request):
    return render(request, 'games/index.html')

def rock_paper_scissors(request):
    run([sys.executable, os.path.join(ROCK_PAPER_SCISSORS,'play_rps.py')], shell=False, stdout=PIPE)
    return render(request, 'games/index.html')

def hangman(request):
    run([sys.executable, os.path.join(HANGMAN, 'play_hangman.py')], shell = False, stdout=PIPE)
    return render(request, 'games/index.html')