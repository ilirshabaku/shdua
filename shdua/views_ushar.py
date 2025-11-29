import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.templatetags.static import static
from .forms import UshtariForm
from .models import Ushtari, Titullari, Firmat
from weasyprint import HTML, CSS
from django.core.paginator import Paginator


def flags_helper(request, ushtari):

    pa_kryer = False
    me_pretendim = False 
    kryer_1 = False
    kryer_2 = False
    kryer_3 = False
    paguar = False
    pa_afte = False
    periudha_1 = False
    periudha_2 = False
    periudha_3 = False
    dite_te_kryera_1 = 0
    dite_te_kryera_2 = 0
    dite_te_kryera_3 = 0

    plus = (request.GET.get('plus') or '').strip()

    # --- 1) Paguar ---
    if ushtari.nr_act_paguar and ushtari.date_of_act_paguar:
        paguar = True

    # --- 2) Pa kryer (asnjë periudhë, asnjë pagesë, asnjë paaftësi) ---
    s1 = not ushtari.shdua_start_date_1 or not ushtari.shdua_finish_date_1
    s2 = not ushtari.nr_act_paguar or not ushtari.date_of_act_paguar
    s3 = not ushtari.epicrize or not ushtari.physical_exam == 'pa_afte'

    if s1 and s2 and s3:
        pa_kryer = True

    # Formulari 2+ (me pretendim)
    pretendim = (plus == 'me_pretendim')
    if pa_kryer and pretendim:
        me_pretendim = True

    # --- 3) Periudha e parë ---
    if (
        ushtari.shdua_start_date_1 and ushtari.shdua_finish_date_1
        and ushtari.shdua_start_date_1 <= ushtari.shdua_finish_date_1
    ):
        dite_te_kryera_1 = (ushtari.shdua_finish_date_1 - ushtari.shdua_start_date_1).days + 1
        periudha_1 = True
        print(f"DEBUG: periudha_e_pare {dite_te_kryera_1} ditë")

        if dite_te_kryera_1 >= 350:
            kryer_1 = True

    # --- 4) Periudha e dytë ---
    if (
        periudha_1
        and ushtari.shdua_start_date_2 and ushtari.shdua_finish_date_2
        and ushtari.shdua_start_date_2 <= ushtari.shdua_finish_date_2
    ):
        dite_te_kryera_2 = (ushtari.shdua_finish_date_2 - ushtari.shdua_start_date_2).days + 1
        periudha_2 = True
        print(f"DEBUG: periudha_e_dyte {dite_te_kryera_2} ditë")

        if dite_te_kryera_1 + dite_te_kryera_2 >= 350:
            kryer_2 = True

    # --- 5) Periudha e tretë ---
    if (
        periudha_2
        and ushtari.shdua_start_date_3 and ushtari.shdua_finish_date_3
        and ushtari.shdua_start_date_3 <= ushtari.shdua_finish_date_3
    ):
        dite_te_kryera_3 = (ushtari.shdua_finish_date_3 - ushtari.shdua_start_date_3).days + 1
        periudha_3 = True
        print(f"DEBUG: periudha_e_trete {dite_te_kryera_3} ditë")

        if dite_te_kryera_1 + dite_te_kryera_2 + dite_te_kryera_3 >= 350:
            kryer_3 = True

    # --- 6) Paaftësia fizike ---
    if (
        ushtari.physical_exam == 'pa_afte'
        and ushtari.nr_act_physical_exam
        and ushtari.date_of_act_physical_exam
        and ushtari.epicrize
    ):
        pa_afte = True

    # --- 7) Sigurojmë që vetëm një "kryer_X" të jetë aktiv sipas prioritetit ---
    if kryer_3:
        kryer_2 = False
        kryer_1 = False
    elif kryer_2:
        kryer_1 = False
    # nëse as kryer_3 as kryer_2 nuk janë True, kryer_1 mbetet siç është

    return (
        pa_kryer,
        me_pretendim,
        kryer_1,
        kryer_2,
        kryer_3,
        paguar,
        pa_afte,
        periudha_1,
        periudha_2,
        periudha_3,
        dite_te_kryera_1,
        dite_te_kryera_2,
        dite_te_kryera_3,
    )


def ushtar_create(request):
    if request.method == "POST":
        form = UshtariForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("ushtar_list")
    else:
        form = UshtariForm()
    context = {"form": form}
    template_name = "ushtar/u_create.html"
    return render(request, template_name, context)

def ushar_list(request):
    qs = Ushtari.objects.all()

    firmetaret_aktiv = Firmat.objects.filter(is_active=True).first()
    titullari_aktiv = Titullari.objects.filter(is_active=True).first()

    name_search = (request.GET.get('name_search') or '').strip()
    father_name_search = (request.GET.get('father_name_search') or '').strip()
    family_name_search = (request.GET.get('family_name_search') or '').strip()
    id_search = (request.GET.get('id_search') or '').strip()

    has_search = any([
        name_search,
        father_name_search,
        family_name_search,
        id_search,
    ])

    if name_search:
        qs = qs.filter(name__icontains=name_search)

    if father_name_search:
        qs = qs.filter(father_name__icontains=father_name_search)

    if family_name_search:
        qs = qs.filter(family_name__icontains=family_name_search)

    if id_search:
        qs = qs.filter(personal_sign__icontains=id_search)

    qs = qs.order_by('family_name', 'name', 'personal_sign')

    # 🔹 këtu NUK futim dummy, thjesht shënojmë që nuk ka rezultate
    no_results = has_search and not qs.exists()

    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'qs': qs,
        'page_obj': page_obj,
        'no_results': no_results,
        'has_search': has_search,

        'titullari_aktiv': titullari_aktiv,
        'firmetaret_aktiv': firmetaret_aktiv,

        'name_search': name_search,
        'father_name_search': father_name_search,
        'family_name_search': family_name_search,
        'id_search': id_search,
    }

    template_name = 'ushtar/u_list.html'
    return render(request, template_name, context)

def ushtar_update(request, pk):
    obj = get_object_or_404(Ushtari, pk=pk)
    if request.method == 'POST':
        form = UshtariForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('ushtar_list')
        else:
            # DEBUG: see why it didn't redirect
            print("FORM ERRORS:", form.errors)
    else:
        form = UshtariForm(instance=obj)
    
    context = {'form': form, 'obj': obj} 

    template_name = 'ushtar/u_update.html'
    return render(request, template_name, context)
 
def ushtar_delete(request, pk):

    obj = get_object_or_404(Ushtari, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('ushtar_list')
    
    template_name = 'ushtar/u_delete.html'

    context = {'obj': obj}

    return render(request, template_name, context)

def ushtar_retrieve(request, pk):
    # --- 1) Lexojmë parametrat e kërkimit nga query string ---
    name_search = (request.GET.get('name_search') or '').strip()
    father_name_search = (request.GET.get('father_name_search') or '').strip()
    family_name_search = (request.GET.get('family_name_search') or '').strip()
    id_search = (request.GET.get('id_search') or '').strip()

    plus = (request.GET.get('plus') or '').strip()
    no_result = False

    # Sigurohemi që pk të trajtohet si numër (funksionon edhe nëse vjen si string)
    try:
        pk_int = int(pk)
    except (TypeError, ValueError):
        pk_int = None

    # --- 2) Rast special: "no result" → pk == 0 ---
    if pk_int == 0:
        no_result = True

        # Krijojmë një "objekt fiktiv" (nuk ruhet në DB)
        obj = Ushtari(
            name=name_search or '—',
            father_name=father_name_search or '—',
            family_name=family_name_search or '—',
            personal_sign=id_search or '—',
        )

        # Flags bosh – nuk thërrasim flags_helper për dummy
        pa_kryer = False
        me_pretendim = False
        kryer_1 = kryer_2 = kryer_3 = False
        paguar = False
        pa_afte = False
        periudha_1 = periudha_2 = periudha_3 = False
        dite_te_kryera_1 = dite_te_kryera_2 = dite_te_kryera_3 = 0

    # --- 3) Rast normal: ushtar real nga DB ---
    else:
        obj = get_object_or_404(Ushtari, pk=pk)

        (pa_kryer, me_pretendim,
         kryer_1, kryer_2, kryer_3,
         paguar, pa_afte,
         periudha_1, periudha_2, periudha_3,
         dite_te_kryera_1, dite_te_kryera_2, dite_te_kryera_3) = flags_helper(request, obj)

    # --- 4) Titullari & firmat ---
    titullari_aktiv = Titullari.objects.filter(is_active=True).first()
    firmetaret = Firmat.objects.filter(is_active=True).first()

    # --- 5) Context për template ---
    context = {
        'titullari_aktiv': titullari_aktiv,
        'firmetaret': firmetaret,
        'obj': obj,
        'plus': plus,
        'no_result': no_result,

        # Të dhënat e kërkimit – për t’u shfaqur te “Të dhënat e kërkimit”
        'name_search': name_search,
        'father_name_search': father_name_search,
        'family_name_search': family_name_search,
        'id_search': id_search,

        # Flags
        'pa_kryer': pa_kryer,
        'me_pretendim': me_pretendim,
        'kryer_1': kryer_1,
        'kryer_2': kryer_2,
        'kryer_3': kryer_3,
        'pa_afte': pa_afte,
        'paguar': paguar,
        'periudha_1': periudha_1,
        'periudha_2': periudha_2,
        'periudha_3': periudha_3,
        'dite_te_kryera_1': dite_te_kryera_1,
        'dite_te_kryera_2': dite_te_kryera_2,
        'dite_te_kryera_3': dite_te_kryera_3,
    }

    return render(request, 'ushtar/u_retrieve_me_kosdakt.html', context)


def pdf_me_kosdakt(request, pk):

    # 1) Input-et e kërkimit (përdoren kur pk == 0)
    name_search = (request.GET.get('name_search') or '').strip()
    father_name_search = (request.GET.get('father_name_search') or '').strip()
    family_name_search = (request.GET.get('family_name_search') or '').strip()
    id_search = (request.GET.get('id_search') or '').strip()
    plus = (request.GET.get('plus') or '').strip()

    no_result = False

    # 2) Rast special: pk == 0 -> "no result" ushtar fiktiv
    if pk == 0:
        obj = Ushtari(
            name=name_search or '—',
            father_name=father_name_search or '—',
            family_name=family_name_search or '—',
            personal_sign=id_search or '—',
        )
        no_result = True

        pa_kryer = False
        me_pretendim = False
        kryer_1 = kryer_2 = kryer_3 = False
        paguar = False
        pa_afte = False
        periudha_1 = periudha_2 = periudha_3 = False
        dite_te_kryera_1 = dite_te_kryera_2 = dite_te_kryera_3 = 0

    else:
        # 3) Rast normal: ushtar real nga DB
        obj = get_object_or_404(Ushtari, pk=pk)

        (pa_kryer, me_pretendim, kryer_1, kryer_2, kryer_3,
         paguar, pa_afte, periudha_1, periudha_2, periudha_3,
         dite_te_kryera_1, dite_te_kryera_2, dite_te_kryera_3) = flags_helper(request, obj)

        # Mund t’i lësh search fields siç janë; në template përdoren vetëm në no_result anyway

    titullari_aktiv = Titullari.objects.filter(is_active=True).first()
    firmetaret = Firmat.objects.filter(is_active=True).first()

    base_url = request.build_absolute_uri('/')
    koka_shkrese_url = request.build_absolute_uri(static('img/koka_e_shkreses.jpg'))

    context = {
        'obj': obj,
        'koka_e_shkreses': koka_shkrese_url,
        'titullari_aktiv': titullari_aktiv,
        'firmetaret': firmetaret,

        'no_result': no_result,
        'plus': plus,

        'name_search': name_search,
        'father_name_search': father_name_search,
        'family_name_search': family_name_search,
        'id_search': id_search,

        'pa_kryer': pa_kryer,
        'me_pretendim': me_pretendim,
        'kryer_1': kryer_1,
        'kryer_2': kryer_2,
        'kryer_3': kryer_3,
        'paguar': paguar,
        'pa_afte': pa_afte,
        'periudha_1': periudha_1,
        'periudha_2': periudha_2,
        'periudha_3': periudha_3,
        'dite_te_kryera_1': dite_te_kryera_1,
        'dite_te_kryera_2': dite_te_kryera_2,
        'dite_te_kryera_3': dite_te_kryera_3,
    }

    html_string = render_to_string("ushtar/u_retrieve_me_kosdakt.html", context, request=request)

    css_url = request.build_absolute_uri(static('css/pdf.css'))
    css = CSS(url=css_url)

    pdf_bytes = HTML(
        string=html_string,
        base_url=base_url,
    ).write_pdf(stylesheets=[css])

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    filename = f"_{obj.name}_{obj.family_name}.pdf"
    response["Content-Disposition"] = f'inline; filename="{filename}"'


    return response

def pdf_pa_kosdakt(request, pk):
    # 1) Marrim input-et e kërkimit (duhen për rastin pk == 0)
    name_search = (request.GET.get('name_search') or '').strip()
    father_name_search = (request.GET.get('father_name_search') or '').strip()
    family_name_search = (request.GET.get('family_name_search') or '').strip()
    id_search = (request.GET.get('id_search') or '').strip()

    no_result = False

    # 2) Rast special: pk == 0 -> "no result" soldier fiktiv
    if pk == 0:
        obj = Ushtari(
            name=name_search or '—',
            father_name=father_name_search or '—',
            family_name=family_name_search or '—',
            personal_sign=id_search or '—',
        )
        no_result = True

        # Asnjë llogaritje flags; i vendosim manualisht
        pa_kryer = False
        me_pretendim = False
        kryer_1 = kryer_2 = kryer_3 = False
        paguar = False
        pa_afte = False
        periudha_1 = periudha_2 = periudha_3 = False
        dite_te_kryera_1 = dite_te_kryera_2 = dite_te_kryera_3 = 0

    else:
        # Rast normal: ushtar real nga DB
        obj = get_object_or_404(Ushtari, pk=pk)

        (pa_kryer, me_pretendim, kryer_1, kryer_2, kryer_3,
         paguar, pa_afte, periudha_1, periudha_2, periudha_3,
         dite_te_kryera_1, dite_te_kryera_2, dite_te_kryera_3) = flags_helper(request, obj)

        # Në rast normal nuk na duhen këto në template, por mund t’i lëmë bosh
        name_search = father_name_search = family_name_search = id_search = ''

    titullari_aktiv = Titullari.objects.filter(is_active=True).first()
    firmetaret = Firmat.objects.filter(is_active=True).first()

    base_url = request.build_absolute_uri('/')
    koka_shkrese_url = request.build_absolute_uri(static('img/koka_e_shkreses.jpg'))

    context = {
        'obj': obj,
        'koka_e_shkreses': koka_shkrese_url,
        'titullari_aktiv': titullari_aktiv,
        'firmetaret': firmetaret,

        'no_result': no_result,
        'name_search': name_search,
        'father_name_search': father_name_search,
        'family_name_search': family_name_search,
        'id_search': id_search,

        'pa_kryer': pa_kryer,
        'me_pretendim': me_pretendim,
        'kryer_1': kryer_1,
        'kryer_2': kryer_2,
        'kryer_3': kryer_3,
        'paguar': paguar,
        'pa_afte': pa_afte,
        'periudha_1': periudha_1,
        'periudha_2': periudha_2,
        'periudha_3': periudha_3,
        'dite_te_kryera_1': dite_te_kryera_1,
        'dite_te_kryera_2': dite_te_kryera_2,
        'dite_te_kryera_3': dite_te_kryera_3,
    }

    html_string = render_to_string("ushtar/u_retrieve_pa_kosdakt.html", context, request=request)

    css_url = request.build_absolute_uri(static('css/pdf.css'))
    css = CSS(url=css_url)

    pdf_bytes = HTML(
        string=html_string,
        base_url=base_url,
    ).write_pdf(stylesheets=[css])

    response = HttpResponse(pdf_bytes, content_type="application/pdf")

    filename = f"_{obj.name}_{obj.family_name}.pdf"
    response["Content-Disposition"] = f'inline; filename="{filename}"'
    return response 
