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
        return False, False, False, False, False

    kryer = False
    paguar = False
    nje_periudhe = False
    dy_periudha = False
    tre_periudha = False
    
    if ushtari.paguar == 'Po':
        paguar = True

    if  ushtari.shdua_start_date_1 and ushtari.shdua_finish_date_1:
        if ushtari.shdua_finish_date_1 > ushtari.shdua_start_date_1:
            kryer = True
            nje_periudhe = True
        else:
            kryer = False

    if nje_periudhe and (ushtari.shdua_start_date_2 and ushtari.shdua_finish_date_2):
        if ushtari.shdua_finish_date_2 > ushtari.shdua_start_date_2:
            dy_periudha = True

    if dy_periudha and ushtari.shdua_start_date_3 and ushtari.shdua_finish_date_3:
        if ushtari.shdua_finish_date_3 > ushtari.shdua_start_date_3:
            tre_periudha = True
    return kryer, nje_periudhe, dy_periudha, tre_periudha, paguar

def ushtar_create(request):
    if request.method == "POST":
        form = UshtariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ushtar_list")
    else:
        form = UshtariForm()
    context = {"form": form}
    template_name = "ushtar/create.html"
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
        qs = qs.filter(personal_id__icontains=id_search)

    qs = qs.order_by('family_name', 'name', 'personal_id')  

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

    template_name = 'ushtar/list.html'
    
    return render(request, template_name, context)

def ushtar_update(request, pk):
    obj = get_object_or_404(Ushtari, pk=pk)
    if request.method == 'POST':
        form = UshtariForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('ushtar_list')
        else:
            # DEBUG: see why it didn't redirect
            print("FORM ERRORS:", form.errors)
    else:
        form = UshtariForm(instance=obj)
    
    context = {'form': form, 'obj': obj} 

    template_name = 'ushtar/update.html'
    return render(request, template_name, context)

def ushtar_delete(request, pk):

    obj = get_object_or_404(Ushtari, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('ushtar_list')
    
    template_name = 'ushtar/delete.html'

    context = {'obj': obj}

    return render(request, template_name, context)

def ushtar_retrieve(request, pk):

    obj = get_object_or_404(Ushtari, pk=pk)
    titullari_aktiv = Titullari.objects.filter(is_active=True).first()

    kryer, paguar, nje_periudhe, dy_periudha, tre_periudha = flags_helper(obj.pk)

    kryer = kryer
    paguar = paguar
    nje_periudhe = nje_periudhe
    dy_periudha = dy_periudha
    tre_periudha = tre_periudha


    context = {
        'titullari_aktiv': titullari_aktiv,
        'obj': obj, 
        'kryer': kryer, 
        'paguar': paguar,
        'nje_periudhe': nje_periudhe, 
        'dy_periudha': dy_periudha, 
        'tre_periudha': tre_periudha,
        }

    template_name = 'ushtar/retrieve.html'

    return render(request, template_name, context)


def vertetimi_pdf(request, pk):
    obj = get_object_or_404(Ushtari, pk=pk)
    titullari_aktiv = Titullari.objects.filter(is_active=True).first()
    kryer, paguar, nje_periudhe, dy_periudha, tre_periudha = flags_helper(obj.pk)

    kryer = kryer
    paguar = paguar
    nje_periudhe = nje_periudhe
    dy_periudha = dy_periudha
    tre_periudha = tre_periudha

    base_url = request.build_absolute_uri('/')

    koka_shkrese_url = request.build_absolute_uri(static('img/koka_e_shkreses.jpg'))

    context = {
        'obj': obj,
        'koka_e_shkreses': koka_shkrese_url,
        'titullari_aktiv': titullari_aktiv,
        
        'kryer': kryer, 
        'paguar': paguar, 
        'nje_periudhe': nje_periudhe,
        'dy_periudha': dy_periudha, 
        'tre_periudha': tre_periudha,
    }

    html_string = render_to_string("ushtar/retrieve.html", context, request=request)

    css_url = request.build_absolute_uri(static('css/pdf.css'))
    css = CSS(url=css_url)

    pdf_bytes = HTML(
        string=html_string,
        base_url=base_url,
    ).write_pdf(stylesheets=[css])

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename=\"ushtar_{pk}.pdf\"'
    return response




