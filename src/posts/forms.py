#from django import forms
# from django.contrib.auth import authenticate, get_user_model

# User = get_user_model()

# class UserLoginForm(forms.Form):
# 	username = forms.CharField()
# 	password = forms.CharField(widget=forms.PasswordInput)

# 	def clean(self, *args, **kwargs):
# 		username = self.cleaned_data.get('username')
# 		password = self.cleaned_data.get('password')

# 		if username and password:
# 			user = authenticate(username = username, password=password)
# 			if not user:
# 				raise forms.ValidationError("incorrect username or password")
# 			if not user.check_passwordd(password):
# 				raise forms.ValidationError("incorrect username or password")
# 			if not user.is_active:
# 				raise forms.ValidationError("incorrect username or password")
# 		return super(UserLoginForm, self).clean(*args, **kwargs)


# class UserRegisterForm(forms.ModelForm):
# 	email = forms.EmailField(label='Email Address')
# 	email2 = forms.EmailField(label='Confirm email')
# 	password = forms.CharField(widget=forms.PasswordInput)

# 	class Meta:
# 		model = User
# 		fields = [

# 			'username'.
# 			'email',
# 			'email2',
# 			'password',

# 		]

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email2 = self.cleaned_data.get('email2')

# 		if email != email2:
# 			raise forms.ValidationError("Email does not match")

# 		if email_qs.exist():
# 			raise forms.ValidationError("Email is already in use")
# 			return email



