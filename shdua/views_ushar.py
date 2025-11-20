from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.templatetags.static import static
from .forms import UshtariForm
from .models import Ushtari, Titullari
from weasyprint import HTML, CSS
from django.core.paginator import Paginator


def flags_helper(pk):
    try:
        ushtari = Ushtari.objects.get(pk=pk)
    except Ushtari.DoesNotExist:
        return False, False, False, False, False, False, 0, 0, 0

    kryer = False
    paguar = False
    paguar_pjeserisht = False
    periudha_1 = False
    periudha_2 = False
    periudha_3 = False
    dite_te_kryera_1 = 0
    dite_te_kryera_2 = 0
    dite_te_kryera_3 = 0


    if ushtari.nr_act_paguar and ushtari.date_of_act_paguar:
        paguar = True

    if  ushtari.shdua_start_date_1 and ushtari.shdua_finish_date_1 \
        and ushtari.shdua_start_date_1 <= ushtari.shdua_finish_date_1:
        dite_te_kryera_1 = (ushtari.shdua_finish_date_1 - ushtari.shdua_start_date_1).days + 1
        periudha_1 = True
        print(f"DEBUG: periudha_e_pare {dite_te_kryera_1} ditë")
        if dite_te_kryera_1 >= 350:
            kryer = True

            
    if periudha_1 and (ushtari.shdua_start_date_2 and ushtari.shdua_finish_date_2) \
        and (ushtari.shdua_start_date_2 <= ushtari.shdua_finish_date_2):
        dite_te_kryera_2 = (ushtari.shdua_finish_date_2 - ushtari.shdua_start_date_2).days + 1 
        periudha_2 = True
        print(f"DEBUG: periudha_e_dyte {dite_te_kryera_2} ditë")
        if dite_te_kryera_1 + dite_te_kryera_2 >= 350:
            kryer = True


    if periudha_2 and (ushtari.shdua_start_date_3 and ushtari.shdua_finish_date_3) \
        and (ushtari.shdua_start_date_3 <= ushtari.shdua_finish_date_3):
        dite_te_kryera_3 = (ushtari.shdua_finish_date_3 - ushtari.shdua_start_date_3).days + 1
        periudha_3 = True
        print(f"DEBUG: periudha_e_trete {dite_te_kryera_3} ditë")
        if dite_te_kryera_1 + dite_te_kryera_2 + dite_te_kryera_3 >= 350:
            kryer = True

    return kryer, paguar, paguar_pjeserisht, periudha_1, periudha_2, periudha_3, dite_te_kryera_1, dite_te_kryera_2, dite_te_kryera_3


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

def ushar_list (request):
    titullari_aktiv = Titullari.objects.filter(is_active=True).first()
    qs = Ushtari.objects.all()

    name_search = (request.GET.get('name_search') or '').strip()
    father_name_search = (request.GET.get('father_name_search') or '').strip()
    family_name_search = (request.GET.get('family_name_search') or '').strip()
    id_search = (request.GET.get('id_search') or '').strip()


    if name_search:
        qs = qs.filter(name__icontains=name_search)

    if father_name_search:
        qs = qs.filter(father_name__icontains=father_name_search)

    if family_name_search:
        qs = qs.filter(family_name__icontains=family_name_search)

    if id_search:
        qs = qs.filter(personal_sign__icontains=id_search)

    qs = qs.order_by('family_name', 'name', 'personal_sign')  

    paginator = Paginator(qs, 10)  # 10 per page
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'qs': qs,
        'titullari_aktiv': titullari_aktiv,
        'name_search': name_search, 
        'father_name_search': father_name_search, 
        'family_name_search': family_name_search,
        'id_search': id_search,
        'page_obj': page_obj,
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

    obj = get_object_or_404(Ushtari, pk=pk)
    titullari_aktiv = Titullari.objects.filter(is_active=True).first()

    kryer, paguar, paguar_pjeserisht, periudha_1, periudha_2, periudha_3, dite_te_kryera_1, dite_te_kryera_2, dite_te_kryera_3 = flags_helper(obj.pk)

    kryer = kryer
    paguar = paguar
    paguar_pjeserisht = paguar_pjeserisht
    periudha_1 = periudha_1
    periudha_2 = periudha_2
    periudha_3 = periudha_3
    dite_te_kryera_1 = dite_te_kryera_1
    dite_te_kryera_2 = dite_te_kryera_2
    dite_te_kryera_3 = dite_te_kryera_3


    context = {
        'titullari_aktiv': titullari_aktiv,
        'obj': obj, 
        'kryer': kryer, 
        'paguar_pjeserisht': paguar_pjeserisht,
        'paguar': paguar,
        'periudha_1': periudha_1,
        'periudha_2': periudha_2,
        'periudha_3': periudha_3,
        'dite_te_kryera_1': dite_te_kryera_1,
        'dite_te_kryera_2': dite_te_kryera_2,
        'dite_te_kryera_3': dite_te_kryera_3,
        }

    template_name = 'ushtar/u_retrieve.html'

    return render(request, template_name, context)


def vertetimi_pdf(request, pk):
    obj = get_object_or_404(Ushtari, pk=pk)
    titullari_aktiv = Titullari.objects.filter(is_active=True).first()
    kryer, paguar, paguar_pjeserisht, periudha_1, periudha_2, periudha_3, dite_te_kryera_1, dite_te_kryera_2, dite_te_kryera_3 = flags_helper(obj.pk)

    kryer = kryer
    paguar = paguar
    paguar_pjeserisht = paguar_pjeserisht
    periudha_1 = periudha_1
    periudha_2 = periudha_2
    periudha_3 = periudha_3
    dite_te_kryera_1 = dite_te_kryera_1
    dite_te_kryera_2 = dite_te_kryera_2
    dite_te_kryera_3 = dite_te_kryera_3

    base_url = request.build_absolute_uri('/')

    koka_shkrese_url = request.build_absolute_uri(static('img/koka_e_shkreses.jpg'))

    context = {
        'obj': obj,
        'koka_e_shkreses': koka_shkrese_url,
        'titullari_aktiv': titullari_aktiv,
        
        'kryer': kryer, 
        'paguar_pjeserisht': paguar_pjeserisht,
        'paguar': paguar,
        'periudha_1': periudha_1,
        'periudha_2': periudha_2,
        'periudha_3': periudha_3,
        'dite_te_kryera_1': dite_te_kryera_1,
        'dite_te_kryera_2': dite_te_kryera_2,
        'dite_te_kryera_3': dite_te_kryera_3,
    }

    html_string = render_to_string("ushtar/u_retrieve.html", context, request=request)

    css_url = request.build_absolute_uri(static('css/pdf.css'))
    css = CSS(url=css_url)

    pdf_bytes = HTML(
        string=html_string,
        base_url=base_url,
    ).write_pdf(stylesheets=[css])

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename=\"ushtar_{pk}.pdf\"'
    return response




