from django import forms


from personal.models import Event 


class CreateEvent(forms.ModelForm):

	class Meta:
		model = Event
		fields = ['title', 'image', 'location','time' ]

