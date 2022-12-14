from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.timezone import localtime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Avg, Max, Min
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from ..models import CoreModel, MemberModel, GameModel, CoreModel, TeamCalculusModel, EachGameDataModel
from ..forms import SpendingForm

class GameDetail(DetailView, LoginRequiredMixin):
    template_name = 'core_detail_1.html'
    model = GameModel

class GameDelete(DeleteView, LoginRequiredMixin):
    template_name = 'core_delete_1.html'
    model = GameModel
    success_url = reverse_lazy('index')
