from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self,*args,**kwargs):
        super(UserLoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Ведите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Ведите  пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'



class UserRegisterForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name', 'password1','password2')


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Ведите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Ведите  адрес эл.почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ведите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ведите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ведите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
