from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="USERAME")
    password = forms.CharField(max_length=10, label="PASSWORD", widget=forms.PasswordInput)
    

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label="USERNAME")
    password = forms.CharField(max_length=10, label="PASSWORD", widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=10, label="PASSWORD CONFIRM", widget = forms.PasswordInput)
    
    def clean(self):
        try:
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            confirm = self.cleaned_data["confirm"]

            if password and confirm and password != confirm:
                raise forms.ValidationError("Şifrələr eyni deyil!")

            values = {
                "username": username,
                "password": password
            }

            return values

        except KeyError as e:
            raise forms.ValidationError(f"Missed Fields: {e.args[0]}")
        except Exception as e:
            raise forms.ValidationError(f"An error occurred: {str(e)}")