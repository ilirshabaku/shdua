

from django import forms
from .models import Ushtari, Titullari



class UshtariForm(forms.ModelForm):
    
    DISTRICT_CODE_CHOICES = [
        ('', '----'),
        ('A', 'A- Tropojë'),
        ('Ç', 'Ç- Malësi e Madhe'),
        ('D', 'D- Shkodër'),
        ('B', 'B- Kukës'),
        ('NJ', 'NJ- Has'),
        ('C', 'C- Pukë'),
        ('F', 'F- Mirditë'),
        ('O', 'O- Bulqizë'),
        ('G', 'G- Dibër'),
        ('H', 'H- Mat'),
        ('E', 'E- Lezhë'),
        ('K', 'K- Kurbin'),
        ('Q', 'Q- Durrës'),
        ('I', 'I- Krujë'),
        ('U', 'U- Tiranë (qyteti)'),
        ('UU', 'UU- Tiranë (rrethinat)'),
        ('LL', 'LL- Elbasan'),
        ('W', 'W- Lushnjë'),
        ('X', 'X- Kuçovë'),
        ('XH', 'XH- Peqin'),
        ('SH', 'SH- Librazhd'),
        ('P', 'P- Berat'),
        ('R', 'R- Gramsh'),
        ('RR', 'RR- Pogradec'),
        ('N', 'N- Kolonjë'),
        ('S', 'S- Skrapar'),
        ('T', 'T- Korçë'),
        ('ZH', 'ZH- Fier'),
        ('Z', 'Z- Vlorë'),
        ('Y', 'Y- Mallakastër'),
        ('M', 'M- Tepelenë'),
        ('V', 'V- Sarandë'),
        ('TH', 'TH- Gjirokastër'),
]
    # compound instances that will form the 'personal_sign' field in db.
    district_code = forms.ChoiceField(
        choices=DISTRICT_CODE_CHOICES, 
        label='Kodi i rrethit', 
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'})
        )
    
    suffix_nr = forms.CharField(max_length=20, 
        label='Mbrapashtesa e kodit', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'})
        )
    
    field_order = [
        'name',
        'father_name',
        'family_name',
        'dob',
        'pob',
        'district_code',   # first instance desired place  
        'suffix_nr',       # second instance's desird place
        # ather fields will remain as ordered in the model
    ]
    class Meta:
        model = Ushtari
        exclude = ['id', 'personal_sign']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'father_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'family_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'dob': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'pob': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
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
                'nr_act_paguar': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'date_of_act_paguar': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'dd.mm.yyyy', 'class': 'form-control', 'style': 'width: 220px;'}),
                'chapter_of_law_paguar': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'nr_of_law_paguar': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'date_of_law_paguar': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
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

    def save(self, commit=True):
        instance  = super().save(commit=False)

        d_code = self.cleaned_data.get('district_code')
        s_nr = self.cleaned_data.get('suffix_nr')

        instance.personal_sign = f'{d_code}-{s_nr}'

        if commit:
            instance.save()
        return instance



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