from django import forms
from .models import User

class RegistForm(forms.ModelForm):
    """
    定义一个注册表单类用于生成html表单
    """
    password2 = forms.CharField(widget=forms.PasswordInput,label="重复密码")
    class Meta:
        model = User
        fields = ["username","password"]
        labels = {
            'username': '用户名',
            'password': '密码'
        }
        help_texts = {
            'username': '大于3小于15',
            'password': '大于3小于15'
        }
        widgets = {
            'password': forms.PasswordInput

        }
