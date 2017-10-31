from django import forms

class RegisterForm(forms.Form):
    UserName = forms.CharField(label='用户名', max_length=100)
    Email = forms.EmailField(label='邮箱', max_length=100)
    password = forms.CharField(label='密码', max_length=100)
