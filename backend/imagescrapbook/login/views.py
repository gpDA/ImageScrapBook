from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
import django.forms as forms
from django.forms import ModelForm
from django.urls import reverse_lazy, reverse



class Login(LoginView):
    template_name = 'login/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('publicgallery')





class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=123)


    class Meta:
        model = User
        fields = ['username', 'password']


class SignupView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'login/signup.html'

    def form_valid(self, form):
        User.objects.create_user(form.cleaned_data['username'], '', form.cleaned_data['password'])
        print(self.success_url)
        return HttpResponseRedirect(self.success_url)
