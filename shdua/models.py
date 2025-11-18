from django.db import models

PHYSIC_EXAM_CHOICES = [
        ('----', '----'),    
        ('afte', 'I aftë'),
        ('pa_afte', 'I paaftë'),
    ]

SPECIALITETI_CHOICES = [
    ('0', '----'),
    ('1', 'Këmbësori'),
    ('2', 'Zbulim'),
    ('3', 'Mortaja 60, 82, 107, 120, 160 mm'),
    ('4', 'Artileri pa sbrapsje 75, 82, 107 mm'),
    ('5', 'Artileri 76, 85, 100, 122, 130, 122 obus, 152 mm top obuz'),
    ('6', 'Artileri reaktive 107, 130, 132 mm'),
    ('7', 'Artileri bregdetare 100, 130 mm TM 130 mm stac'),
    ('8', 'Raketë e drejturar kundër tanke'),
    ('9', 'Raketë e drejtuar kundërajrore'),
    ('10', 'Specialistë drejtimi të raketave'),
    ('12', 'Mitraloza kundërajorë 12.7, 14.5 mm'),
    ('13', 'Artileri kundërajrore 20, 25, 37, 57, 85, 100 mm'),
    ('14', 'Specialist të aparaturës së drejtimit të AKA-së'),
    ('15', 'Radiolokatore (p-8, p-10, p-11, e të tjerë), SDT dhe radiolokatorë të ndryshëm'),
    ('16', 'Zbulues të AKA-së'),
    ('17', 'Radiolokatorë për ABD'),
    ('18', 'Zbulues të artilerisë tokësore e bregdetare'),
    ('19', 'Topografë dhe topollogaritës'),
    ('20', 'Meteorologji'),
    ('21', 'Telementristë'),
    ('22', 'Projektoristë (specialist ndriçimi)'),
    ('23', 'Fotografi'),
    ('24', 'Teknik armatimi'),
    ('25', 'Teknik municioni'),
    ('26', 'Tanke dhe AVL'),
    ('27', 'Rregullues lëvizje'),
    ('28', 'Shoferë'),
    ('29', 'Motoçiklist'),
    ('30', 'Traktoristë, buldozerë, tërheqës'),
    ('31', 'Eskavatoristë'),
    ('32', 'Automekanikë'),
    ('33', 'Xhenerikë'),
    ('34', 'Axhustatorë'),
    ('35', 'Frezatorë'),
    ('36', 'Tornitorë'),
    ('37', 'Saldatorë, oksigjenistë'),
    ('38', 'Kovaç, llamarinistë'),
    ('39', 'Elektriçistë'),
    ('40', 'Elektroauto, akumulatoristë'),
    ('41', 'Motoristë'),
    ('42', 'Specialistë karburanti'),
    ('43', 'Xhenierë'),
    ('44', 'Muratorë'),
    ('45', 'Marangozë'),
    ('46', 'Kompresorë'),
    ('47', 'Hidraulikë'),
    ('48', 'Elektromagnetik'),
    ('49', 'Telefonistë-çentralistë'),
    ('50', 'Sinjalistë'),
    ('51', 'Radiofonistë, radiorelistë'),
    ('52', 'Radiotelegrafistë'),
    ('53', 'Telegrafistë'),
    ('54', 'Teknikë ndërlidhje'),
    ('55', 'Ekspeditor'),
    ('56', 'Mekanikë avioni helikopterë'),
    ('57', 'Mekanikë për armatimin e avionit'),
    ('58', 'Mekanikë për pajimet elektrike e radiopajimet'),
    ('59', 'Mekanikë për pajimet speciale të avionit dhe instrumentet'),
    ('60', 'Mekanikë për oksigjen'),
    ('61', 'Parashutistë'),
    ('62', 'Radiopelengatorë'),
    ('63', 'Teknikë për mjetet optike'),
    ('66', 'Kimi'),
    ('67', 'Flakëhedhës'),
    ('68', 'Sanitarë'),
    ('69', 'Shëndetësi'),
    ('70', 'Veterinari'),
    ('71', 'Laborantë'),
    ('72', 'Farmacistë'),
    ('73', 'Dentistë'),
    ('74', 'Nallbanë'),
    ('75', 'Këpucarë, berberë'),
    ('76', 'Rrobaqepës'),
    ('77', 'Shërbim prapavije'),
    ('78', 'Kuzhinierë, bukëpjekës, mullixhi'),
    ('79', 'Administratë'),
    ('80', 'Kompjutër (ordinator)'),
    ('81', 'Tipografistë'),
    ('82', 'Polici Ushtarake'),
    ('83', 'Muzikantë (fanarë)'),
    ('84', 'Këngëtarë, koristë, valltarë'),
    ('85', 'Përgjegjës kuverte'),
    ('86', 'Timonierë'),
    ('87', 'Elektroshturman'),
    ('88', 'Hidroakustikë'),
    ('89', 'Detar, minjor'),
    ('90', 'Siluristë'),
    ('91', 'Hidrografë'),
    ('92', 'Hamburistë'),
    ('93', 'radiometristë'),
    ('94', 'Kaldaistë'),
    ('95', 'Komando (forca speciale)'),
    ('96', 'Paqeruajtës'),
    ('97', 'Të pastërvitur'),
    ('98', 'Me veçori shërbimi'),
]

POB_CHOICES = [
        ('----', '----'),
        ('A', 'Tropojë'),
        ('Ç', 'Malësi e Madhe'),
        ('D', 'Shkodër'),
        ('B', 'Kukës'),
        ('NJ', 'Has'),
        ('C', 'Pukë'),
        ('F', 'Mirditë'),
        ('O', 'Bulqizë'),
        ('G', 'Dibër'),
        ('H', 'Mat'),
        ('E', 'Lezhë'),
        ('K', 'Kurbin'),
        ('Q', 'Durrës'),
        ('I', 'Krujë'),
        ('U', 'Tiranë (qyteti)'),
        ('UU', 'Tiranë (rrethinat)'),
        ('Ll', 'Elbasan'),
        ('W', 'Lushnjë'),
        ('X', 'Kuçovë'),
        ('XH', 'Peqin'),
        ('SH', 'Librazhd'),
        ('P', 'Berat'),
        ('R', 'Gramsh'),
        ('RR', 'Pogradec'),
        ('N', 'Kolonjë'),
        ('S', 'Skrapar'),
        ('T', 'Korçë'),
        ('ZH', 'Fier'),
        ('Z', 'Vlorë'),
        ('Y', 'Mallakastër'),
        ('M', 'Tepelenë'),
        ('V', 'Sarandë'),
        ('TH', 'Gjirokastër'),
]

PO_JO_CHOICES = [
    ('----', '----'),
    ('Po', 'Po'),
    ('Jo', 'Jo'),
]

class Ushtari(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,  default= '', verbose_name='Emri')
    father_name = models.CharField(max_length=50, null=False, blank=False,  default= '', verbose_name='Atësia')
    family_name = models.CharField(max_length=50, null=False, blank=False,  default= '', verbose_name='Mbimri')
    dob = models.DateField(null=True, blank=True, verbose_name='Datëlindja')  
    pob = models.CharField(max_length=30, null=False, blank=False, choices=POB_CHOICES,  default= '', verbose_name='Vendlindja') 
    personal_id = models.CharField(primary_key=True, max_length=30, null=False, blank=False, editable=True, verbose_name='Shenja personale') 
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
    nr_act_epicrize = models.CharField(max_length=30, null=True, blank=True,  default= '', verbose_name='Nr. i mandatit')
    date_of_act_epicrize = models.DateField(null=True, blank=True, verbose_name='Data e mandat arkëtimit')
    chapter_of_law = models.CharField(max_length=30, null=True, blank=True,  default= '', verbose_name='Neni i ligjit')
    nr_of_law = models.CharField(max_length=30, null=True, blank=True,  default= '', verbose_name='Numri i ligjit')
    date_of_law = models.DateField(null=True, blank=True, verbose_name='Data e ligjit')
    paguar = models.CharField(max_length=30, null=False, blank=False,  choices=PO_JO_CHOICES, default= 'Jo', verbose_name='A e ka shlyer me pagesë detyrin e SHDUA (po ose jo)?')
    notes = models.TextField(blank=True, null=True, verbose_name='Shënime')


    def __str__(self):
        return f"{self.name} ({self.family_name} {self.family_name} - {self.pob})"



class Titullari(models.Model):
    funksioni = models.CharField(max_length=50, null=False, blank=False, verbose_name='Funksioni')
    grada = models.CharField(max_length=50, null=False, blank=False, verbose_name='Grada')
    emri = models.CharField(max_length=50, null=False, blank=False, verbose_name='Emri')
    mbiemri = models.CharField(max_length=50, null=False, blank=False, verbose_name='Mbiemri')
    is_active = models.BooleanField(default=False, verbose_name="Titullari aktiv")
    
    
    def __str__(self):
        return f'{self.funksioni} {self.grada} {self.emri} {self.mbiemri}'