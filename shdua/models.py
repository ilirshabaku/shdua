from django.db import models

PHYSIC_EXAM_CHOICES = [ 
        ('pa_afte', 'I paaftë'),
    ]

SPECIALITETI_CHOICES = [
    ('1', '1- Këmbësori'),
    ('2', '2- Zbulim'),
    ('3', '3- Mortaja 60, 82, 107, 120, 160 mm'),
    ('4', '4- Artileri pa sbrapsje 75, 82, 107 mm'),
    ('5', '5- Artileri 76, 85, 100, 122, 130, 122 obus, 152 mm top obuz'),
    ('6', '6- Artileri reaktive 107, 130, 132 mm'),
    ('7', '7- Artileri bregdetare 100, 130 mm TM 130 mm stac'),
    ('8', '8- Raketë e drejturar kundër tanke'),
    ('9', '8- Raketë e drejtuar kundërajrore'),
    ('10', '10- Specialistë drejtimi të raketave'), # mungon 11-ta
    ('12', '12- Mitraloza kundërajorë 12.7, 14.5 mm'),
    ('13', '13- Artileri kundërajrore 20, 25, 37, 57, 85, 100 mm'),
    ('14', '14- Specialist të aparaturës së drejtimit të AKA-së'),
    ('15', '15- Radiolokatore (p-8, p-10, p-11, e të tjerë), SDT dhe radiolokatorë të ndryshëm'),
    ('16', '16- Zbulues të AKA-së'),
    ('17', '17- Radiolokatorë për ABD'),
    ('18', '18- Zbulues të artilerisë tokësore e bregdetare'),
    ('19', '19- Topografë dhe topollogaritës'),
    ('20', '20- Meteorologji'),
    ('21', '21- Telementristë'),
    ('22', '22- Projektoristë (specialist ndriçimi)'),
    ('23', '23- Fotografi'),
    ('24', '24- Teknik armatimi'),
    ('25', '25- Teknik municioni'),
    ('26', '26- Tanke dhe AVL'),
    ('27', '27- Rregullues lëvizje'),
    ('28', '28- Shoferë'),
    ('29', '29- Motoçiklist'),
    ('30', '30- Traktoristë, buldozerë, tërheqës'),
    ('31', '31- Eskavatoristë'),
    ('32', '32- Automekanikë'),
    ('33', '33- Xhenerikë'),
    ('34', '34- Axhustatorë'),
    ('35', '35- Frezatorë'),
    ('36', '36- Tornitorë'),
    ('37', '37- Saldatorë, oksigjenistë'),
    ('38', '38- Kovaç, llamarinistë'),
    ('39', '39- Elektriçistë'),
    ('40', '40- Elektroauto, akumulatoristë'),
    ('41', '41- Motoristë'),
    ('42', '42- Specialistë karburanti'),
    ('43', '43- Xhenierë'),
    ('44', '44- Muratorë'),
    ('45', '45- Marangozë'),
    ('46', '46- Kompresorë'),
    ('47', '47- Hidraulikë'),
    ('48', '48- Elektromagnetik'),
    ('49', '49- Telefonistë-çentralistë'),
    ('50', '50- Sinjalistë'),
    ('51', '51- Radiofonistë, radiorelistë'),
    ('52', '52- Radiotelegrafistë'),
    ('53', '53- Telegrafistë'),
    ('54', '54- Teknikë ndërlidhje'),
    ('55', '55- Ekspeditor'),
    ('56', '56- Mekanikë avioni helikopterë'),
    ('57', '57- Mekanikë për armatimin e avionit'),
    ('58', '58- Mekanikë për pajimet elektrike e radiopajimet'),
    ('59', '59- Mekanikë për pajimet speciale të avionit dhe instrumentet'),
    ('60', '60- Mekanikë për oksigjen'),
    ('61', '61- Parashutistë'),
    ('62', '62- Radiopelengatorë'),
    ('63', '63- Teknikë për mjetet optike'),
    ('66', '66- Kimi'),
    ('67', '67- Flakëhedhës'),
    ('68', '68- Sanitarë'),
    ('69', '69- Shëndetësi'),
    ('70', '70- Veterinari'),
    ('71', '71- Laborantë'),
    ('72', '72- Farmacistë'),
    ('73', '73- Dentistë'),
    ('74', '74- Nallbanë'),
    ('75', '75- Këpucarë, berberë'),
    ('76', '76- Rrobaqepës'),
    ('77', '77- Shërbim prapavije'),
    ('78', '78- Kuzhinierë, bukëpjekës, mullixhi'),
    ('79', '79- Administratë'),
    ('80', '80- Kompjutër (ordinator)'),
    ('81', '81- Tipografistë'),
    ('82', '82- Polici Ushtarake'),
    ('83', '83- Muzikantë (fanarë)'),
    ('84', '84- Këngëtarë, koristë, valltarë'),
    ('85', '85- Përgjegjës kuverte'),
    ('86', '86- Timonierë'),
    ('87', '87- Elektroshturman'),
    ('88', '88- Hidroakustikë'),
    ('89', '89- Detar, minjor'),
    ('90', '90- Siluristë'),
    ('91', '91- Hidrografë'),
    ('92', '92- Hamburistë'),
    ('93', '93- radiometristë'),
    ('94', '94- Kaldaistë'),
    ('95', '95- Komando (forca speciale)'),
    ('96', '96- Paqeruajtës'),
    ('97', '97- Të pastërvitur'),
    ('98', '98- Me veçori shërbimi'),
]

PO_JO_CHOICES = [
    ('----', '----'),
    ('Po', 'Po'),
    ('Jo', 'Jo'),
]

NENI_CHOICES = [
    ('42', '42')
]

NR_LIGJI_CHOICES = [
    ('9047', '9047')
]

DATA_LIGJI_CHOICES = [
    ('10.07.2003', '10.07.2003')
]

class Ushtari(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Primary key (int)')
    name = models.CharField(max_length=50, null=False, blank=False,  default= '', verbose_name='Emri')
    father_name = models.CharField(max_length=50, null=False, blank=False, default= '', verbose_name='Atësia')
    family_name = models.CharField(max_length=50, null=False, blank=False, default= '', verbose_name='Mbimri')
    dob = models.DateField(null=True, blank=True, verbose_name='Datëlindja')  
    pob = models.CharField(max_length=30, null=False, blank=False, default= '', verbose_name='Vendlindja') 
    personal_sign = models.CharField(max_length=40, null=True, blank=True, editable=True, verbose_name='Shenja personale') 
    unit_nr_1st_time = models.CharField(max_length=30, null=True, blank=True,  default= '', verbose_name='RU numri, vendi')
    shdua_start_date_1 = models.DateField(null=True, blank=True, verbose_name='Data e fillimit SHDUA')
    shdua_finish_date_1 = models.DateField(null=True, blank=True, verbose_name='Data e mbarimit SHDUA')
    unit_nr_2nd_time = models.CharField(max_length=30, null=True, blank=True,  default= '', verbose_name='RU numri, vendi (Rimobilizim 1)')
    shdua_start_date_2 = models.DateField(null=True, blank=True, verbose_name='Data e fillimit SHDUA (Rimobilizim 1)')
    shdua_finish_date_2 = models.DateField(null=True, blank=True, verbose_name='Data e mbarimit SHDUA (Rimobilizim 1)')
    unit_nr_3rd_time = models.CharField(max_length=30, null=True, blank=True, default= '', verbose_name='RU numri, vendi (Rimobilizim 2)')
    shdua_start_date_3 = models.DateField(null=True, blank=True, verbose_name='Data e fillimit SHDUA (Rimobilizim 2)')
    shdua_finish_date_3 = models.DateField(null=True, blank=True, verbose_name='Data e mbarimit SHDUA (Rimobilizim 2)')
    speciallity = models.CharField(max_length=30, null=True, blank=True, choices=SPECIALITETI_CHOICES,  default='0', verbose_name='Specialiteti (ESU)')
    physical_exam = models.CharField(max_length=10, null=True, blank=True, choices=PHYSIC_EXAM_CHOICES, default='----', verbose_name='Vlerësimi fizik')
    nr_act_physical_exam = models.CharField(max_length=30, null=True, blank=True,  default= '', verbose_name='Nr. i aktit')
    date_of_act_physical_exam = models.DateField(null=True, blank=True, verbose_name='Data e vendimit')
    epicrize = models.CharField(max_length=130, null=True, blank=True,  default= '', verbose_name='Epikriza e identifikuar (Arti)')
    nr_act_paguar = models.CharField(max_length=30, null=True, blank=True,  default= '', verbose_name='Nr. i mandatit të pagesës')
    date_of_act_paguar = models.DateField(null=True, blank=True, verbose_name='Data e mandatit të pagesës')
    chapter_of_law_paguar = models.CharField(max_length=30, null=True, blank=True, choices=NENI_CHOICES,  default= '', verbose_name='Neni i ligjit')
    nr_of_law_paguar = models.CharField(max_length=30, null=True, blank=True, choices=NR_LIGJI_CHOICES,  default= '', verbose_name='Numri i ligjit')
    date_of_law_paguar = models.CharField(max_length=30, null=True, blank=True, choices=DATA_LIGJI_CHOICES, default= '', verbose_name='Data e ligjit')
    notes = models.TextField(blank=True, null=True, verbose_name='Shënime')


    def __str__(self):
        return f"{self.name} ({self.father_name} {self.family_name} - {self.pob})"



class Titullari(models.Model):
    funksioni = models.CharField(max_length=50, null=False, blank=False, verbose_name='Funksioni')
    grada = models.CharField(max_length=50, null=False, blank=False, verbose_name='Grada')
    emri = models.CharField(max_length=50, null=False, blank=False, verbose_name='Emri')
    mbiemri = models.CharField(max_length=50, null=False, blank=False, verbose_name='Mbiemri')
    is_active = models.BooleanField(default=False, verbose_name="Titullari aktiv")
    
    
    def __str__(self):
        return f'{self.funksioni} {self.grada} {self.emri} {self.mbiemri}'