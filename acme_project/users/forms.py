# users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Получаем модель пользователя:
User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')  # Укажите необходимые поля вашей модели

