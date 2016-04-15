from django import forms

from .models import radler, woche, team

class WochenForm(forms.ModelForm):

    class Meta:
        model = woche
        fields = ('kwnr', 'mo', 'di', 'mi', 'do', 'fr',
			'mo_extra', 'di_extra', 'mi_extra', 'do_extra', 'fr_extra')


class RadlerForm(forms.ModelForm):
	class Meta:
		model = radler
		fields = ('vname', 'nname', 'email', 'team', 'km')

class TeamForm(forms.ModelForm):
	class Meta:
		model = team
		fields = ( 'name', )
