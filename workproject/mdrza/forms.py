from django import forms

from .models import radler, woche, team

class WochenForm(forms.ModelForm):

	class Meta:
		model = woche
		fields = (
			'kwnr',
			'mo',
			'mo_extra',
			'di',
			'di_extra',
			'mi',
			'mi_extra',
			'do',
			'do_extra',
			'fr',
			'fr_extra'
		)
		labels = {
			'kwnr': ('Kalenderwoche'),
			'mo': ('Montag'),
			'di': ('Dienstag'),
			'mi': ('Mittwoch'),
			'do': ('Donnerstag'),
			'fr': ('Freitag'),
			'mo_extra': ('Extra'),
			'di_extra': ('Extra'),
			'mi_extra': ('Extra'),
			'do_extra': ('Extra'),
			'fr_extra': ('Extra'),
		}


class RadlerForm(forms.ModelForm):
	class Meta:
		model = radler
		fields = ('vname', 'nname', 'email', 'team', 'km')
		labels = {
			'vname': ('Vorname'),
			'nname': ('Nachname'),
			'email': ('E-Mail'),
			'team': ('Team'),
			'km': ('Tages-KM'),
		}

class TeamForm(forms.ModelForm):
	class Meta:
		model = team
		fields = ( 'name', )
		labels = {
			'name': ('Team'),
		}
