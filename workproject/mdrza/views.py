# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone
from .models import woche, radler, team

from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import WochenForm, RadlerForm, TeamForm

from django.contrib.auth.forms import UserCreationForm

from .einstellungen import startweek, mdrzajahr, endweek 

from datetime import date
def get_week():
	jetzt = date.today()
	week = jetzt.isocalendar()[1]
	return week

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/mdrza/accounts/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def calc_woche(woche):
	tage = 0
	extras = 0 
	for tag in ("mo", "di", "mi", "do", "fr"):
		if (woche.__dict__[tag] == True):
			tage = tage + 1
			tag_extra = tag + '_extra'
			if (woche.__dict__[tag_extra] > 0):
				extras = extras + woche.__dict__[tag_extra]
	basis_km = woche.user.km
	km = basis_km * tage
	km = km + extras
	return (km, tage)

def calc_radler(Radler):
	wochen = woche.objects.filter(user=Radler)
	weeks = {}
	gesamt_km = 0
	gesamt_tage = 0
	for w in wochen:
		(woche_km, woche_tage) = calc_woche(w)
		kw = w.pk
		weeks[kw] = woche_km
		gesamt_km = gesamt_km + woche_km
		gesamt_tage = gesamt_tage + woche_tage
	Radler.gesamtkm = gesamt_km
	Radler.gesamttage = gesamt_tage
	Radler.save()
	return(weeks, gesamt_km, gesamt_tage)

def calc_team(Team):
	radlers = radler.objects.filter(team=Team)
	gesamt_km = 0
	for r in radlers:
		(w,k,t) = calc_radler(r)
		gesamt_km = gesamt_km + k
	Team.gesamtkm = gesamt_km
	Team.save()
	return(gesamt_km)

def calc_gesamtkm():
	Teams = team.objects.all()
	gesamt_km = 0
	for t in Teams:
		km = calc_team(t)
		gesamt_km = gesamt_km + km
	return(gesamt_km)

def team_list(request):
    teams = team.objects.order_by('-gesamtkm')
    gesamt_km = calc_gesamtkm()
    return render(request, 'mdrza/team_list.html', {'teams': teams, 'km': gesamt_km })

def team_detail(request, pk):
        Team = get_object_or_404(team, pk=pk)
	gesamt_km = calc_team(Team)
	return render(request, 'mdrza/team_detail.html', {'team': Team, 'gesamt_km': gesamt_km })

def radler_list(request):
	alleradler = radler.objects.order_by('-gesamtkm')
	return render(request, 'mdrza/radler_list.html', { 'radler' : alleradler, })

def radler_detail(request, pk):
        Radler = get_object_or_404(radler, pk=pk)
	(weeks, gesamt_km, gesamt_tage) = calc_radler(Radler)
	return render(request, 'mdrza/radler_detail.html', {'radler': Radler, 'wochen' : weeks, 'gesamt_km': gesamt_km, 'gesamt_tage': gesamt_tage })

@login_required
def radler_new(request):
    if request.method == "POST":
        form = RadlerForm(request.POST)
        if form.is_valid():
            Radler = form.save(commit=False)
	    Radler.user = request.user
            Radler.save()
            return redirect('radler_detail', pk=Radler.pk)
    else:
        form = RadlerForm()
    return render(request, 'mdrza/radler_new.html', {'form': form})

def radler_edit(request, pk):
	    Radler = get_object_or_404(radler, pk=pk)
	    if Radler.pk == request.user.radler.pk:
		    if request.method == "POST":
			form = RadlerForm(request.POST, instance=Radler)
			if form.is_valid():
			    Radler = form.save(commit=False)
			    #Woche.user = request.user
			    Radler.save()
			    return redirect('radler_detail', pk=Radler.pk)
		    else:
			form = RadlerForm(instance=Radler)
		    return render(request, 'mdrza/radler_new.html', {'form': form})
	    else: 
		    return redirect('radler_detail', pk=Radler.pk)

def check_woche(Woche):
	if Woche.kwnr >= startweek and Woche.kwnr <= endweek:
		fine = True
		msg =""
	else:
		fine = False
		msg = 'KW liegt außerhalb des Aktionszeitraums!'
	return (fine, msg)

def check_woche_neu(Woche):
	msg = ''
	w = Woche.kwnr
	n = Woche.user.pk
	userweeks = woche.objects.filter(user=n).filter(kwnr=w)
	if (len(userweeks) > 0) and (Woche.pk != userweeks[0].pk):
		fine = False
		msg = 'Die Woche existiert bereits, bitte die KW bearbeiten!'
	else:
		fine = True
		mgs = ''
	return(fine, msg)

def woche_detail(request, pk):
        Woche = get_object_or_404(woche, pk=pk)
	(woche_km, woche_tage) = calc_woche(Woche)
	return render(request, 'mdrza/woche_detail.html', {'woche': Woche, 'woche_km' : woche_km, 'woche_tage': woche_tage })

def woche_edit(request, pk):
    Woche = get_object_or_404(woche, pk=pk)
    week = get_week()
    if Woche.user.pk == request.user.radler.pk: 
	    if request.method == "POST":
		form = WochenForm(request.POST, instance=Woche)
		if form.is_valid():
		    Woche = form.save(commit=False)
		    (fine, error_msg) = check_woche(Woche)
		    (fine2, error_msg2) = check_woche_neu(Woche)
		    if fine == True and fine2 == True:
		    	#Woche.user = request.user
		    	Woche.save()
		    	return redirect('woche_detail', pk=Woche.pk)
		    else:
			error_msg = error_msg + " " + error_msg2
			return render(request, 'mdrza/error.html', { 'error_msg': error_msg })
	    else:
		form = WochenForm(instance=Woche)
	    return render(request, 'mdrza/woche_edit.html', {'form': form, 'week': week })
    else:
	    return redirect('woche_detail', pk=pk)

@login_required
def woche_new(request):
    week = get_week()
    if request.method == "POST":
        form = WochenForm(request.POST)
        if form.is_valid():
            Woche = form.save(commit=False)
	    Woche.user = request.user.radler
	    (fine, error_msg) = check_woche(Woche)
	    (fine2, error_msg2) = check_woche_neu(Woche)
	    if fine == True and fine2 == True:
		Woche.save()
            	return redirect('woche_detail', pk=Woche.pk)
	    else:
		error_msg = error_msg + ' ' + error_msg2
		return render(request, 'mdrza/error.html', { 'error_msg': error_msg })
    else:
        form = WochenForm()
    return render(request, 'mdrza/woche_edit.html', {'form': form , 'week': week })

@login_required
def team_new(request):
	if request.method == 'POST':
		form = TeamForm(request.POST)
		if form.is_valid():
			Team = form.save(commit=False)
			Team.save()
			return redirect('team_list')
	else:
		form = TeamForm()
	return render(request, 'mdrza/team_edit.html', { 'form' : form})

