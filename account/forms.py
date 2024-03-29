from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2', )


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Account
        fields = ('email', 'username', 'profile_photo','social_media_link','position')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            Account.objects.exclude(pk=self.instance.pk).get(email=email)
            raise forms.ValidationError('Email "%s" is already in use.' % email)
        except Account.DoesNotExist:
            return email

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Account.objects.exclude(pk=self.instance.pk).get(username=username)
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        except Account.DoesNotExist:
            return username

    def save(self, commit=True):
        account = super().save(commit=False)
        if self.cleaned_data['profile_photo']:
            account.profile_photo = self.cleaned_data['profile_photo']
        if commit:
            account.save()
        return account

















