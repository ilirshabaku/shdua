

from django import forms
from .models import Ushtari, Titullari

class UshtariForm(forms.ModelForm):
    class Meta:
        model = Ushtari
        fields = '__all__'
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'father_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'family_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'dob': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'pob': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'personal_id': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'unit_nr_1st_time': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'shdua_start_date_1': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'shdua_finish_date_1': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'unit_nr_2nd_time': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'shdua_start_date_2': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'shdua_finish_date_2': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'unit_nr_3rd_time': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'shdua_start_date_3': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'shdua_finish_date_3': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'speciallity': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'physical_exam': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'nr_act_physical_exam': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'date_of_act_physical_exam': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'epicrize': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'nr_act_epicrize': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'date_of_act_epicrize': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'chapter_of_law': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'nr_of_law': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'date_of_law': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'paguar': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'notes': forms.Textarea(attrs={
                    'class': 'form-control',       # Bootstrap styling
                    'placeholder': 'Shkruani shkurtimisht ndonjë koment.',
                    'rows': 3,
                    'maxlength': '450',             # HTML max length
                    'pattern': '[A-Za-z0-9.,!?;:\'\"()\\-\\s]+',        # Accept letters, number, puctuation and spaces
                    'title': 'Motivi që ju shtyn të shërbeni në Forcat e Armatosura.',
                    'autocomplete': 'off',         # Disable browser autocomplete                 
                }),

        }


class TitullariForm(forms.ModelForm):
    class Meta:
        model = Titullari
        fields = ['funksioni', 'grada', 'emri', 'mbiemri']
        widgets = {
                'funksioni': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'grada': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'emri': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'mbiemri': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                
        }

class TitullariSelectForm(forms.Form):
    titullari = forms.ModelChoiceField(
        queryset=Titullari.objects.all(),
        label="Zgjidh titullarin aktual",
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'width: 420px;'})
    )