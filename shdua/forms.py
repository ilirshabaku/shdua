from django import forms
from .models import Ushtari, Titullari, Firmat



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

    suffix_nr = forms.CharField(
        max_length=20,
        label='Mbrapashtesa e kodit',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'})
    )

    field_order = [
        'name',
        'father_name',
        'family_name',
        'dob',
        'pob',
        'district_code',  # first instance desired place
        'suffix_nr',      # second instance's desired place
        # other fields will remain as ordered in the model
    ]

    class Meta:
        model = Ushtari
        exclude = ['personal_sign']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'family_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'dob': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'pob': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'unit_nr_1st_time': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'shdua_start_date_1': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'shdua_finish_date_1': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'unit_nr_2nd_time': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'shdua_start_date_2': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'shdua_finish_date_2': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'unit_nr_3rd_time': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'shdua_start_date_3': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'shdua_finish_date_3': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'speciallity': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'physical_exam': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'nr_act_physical_exam': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'date_of_act_physical_exam': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'epicrize': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'nr_act_paguar': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'date_of_act_paguar': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'dd.mm.yyyy',
                    'class': 'form-control',
                    'style': 'width: 220px;',
                    'autocomplete': 'off',
                }
            ),
            'chapter_of_law_paguar': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'nr_of_law_paguar': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            # NOTE: this is Select, so it's probably not a true DateField
            'date_of_law_paguar': forms.Select(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Shkruani shkurtimisht ndonjë koment.',
                'rows': 3,
                'maxlength': '450',
                'pattern': '[A-Za-z0-9.,!?;:\'\"()\\-\\s]+',
                'title': '......',
                'autocomplete': 'off',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        date_fields = [
            'dob',
            'shdua_start_date_1',
            'shdua_finish_date_1',
            'shdua_start_date_2',
            'shdua_finish_date_2',
            'shdua_start_date_3',
            'shdua_finish_date_3',
            'date_of_act_physical_exam',
            'date_of_act_paguar',
            # Only keep this here if the model field is actually a DateField
            # 'date_of_law_paguar',
        ]

        for name in date_fields:
            field = self.fields.get(name)
            if field:
                field.input_formats = ['%d.%m.%Y']

        # 2) Pre-fill district_code and suffix_nr from instance.personal_sign
        personal_sign = getattr(self.instance, 'personal_sign', '')  # e.g. "H-123"

        if personal_sign:
            try:
                d_code, s_nr = personal_sign.split('-', 1)  # split only on first '-'
            except ValueError:
                d_code, s_nr = '', ''
            self.fields['district_code'].initial = d_code
            self.fields['suffix_nr'].initial = s_nr                

    def save(self, commit=True):
        instance = super().save(commit=False)

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

class FirmatForm(forms.ModelForm):
    class Meta:
        model = Firmat
        fields = ['hartoi', 'kontrolloi', 'miratoi']
        widgets = {
                'hartoi': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'kontrolloi': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
                'miratoi': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 220px;'}),
        }
    

