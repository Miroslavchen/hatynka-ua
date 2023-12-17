from .models import Status, Buy
from django.forms import ModelForm, TextInput, TimeInput, CharField, PasswordInput, FileInput, ModelChoiceField, CheckboxInput, ChoiceField, HiddenInput


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['Name', 'X', 'Y', 'Z', 'Time', 'Cost', 'Img1', 'Img2', 'Img3', 'Img4']
        widgets = {
            'Name': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': "Назва"
            }),
            'X': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Ширина'
            }),
            'Y': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Дожина'
            }),
            'Z': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Висота'
            }),
            'Time': TimeInput(attrs={
                'type': 'date',
                'class': 'form-control buff',
                'placeholder': 'Термін придатності'
            }),
            'Cost': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Коштує'
            }),
            'Img1': FileInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Фото',
                'accept': '.png, .jpg'
            }),
            'Img2': FileInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Фото',
                'accept': '.png, .jpg'
            }),
            'Img3': FileInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Фото',
                'accept': '.png, .jpg'
            }),
            'Img4': FileInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Фото',
                'accept': '.png, .jpg'
            })
        }

class BuyForm(ModelForm):
    class Meta:
        # hatka_choice = ((f'option{i}', f'{Status.objects.values("Name")[i]}') for i in range(len(Status.objects.values('Name'))))
        # my_choices = ((f'option{j}', f'{j}') for j in range(5))
        model = Buy
        fields = ['Name', 'Phone', 'url', 'Email']
        widgets = {
            'Name': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': "Ім'я"
            }),
            'Phone': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Номер телефону'
            }),
            'url': HiddenInput(),
            'Email': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Електрона Адреса'
            }),
        }
