from django.forms import UserCreationForm

class Cadastro_Usuario(UserCreationForm):
    class Meta:
        model = Aluno
        fields = ['username', 'email', 'password1', 'password2']
        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user
class Cadastro_Professor(UserCreationForm):
    class Meta:
        model = Professor
        fields = ['username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user