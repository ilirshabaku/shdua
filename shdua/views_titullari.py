from django.shortcuts import render, redirect, get_object_or_404
from .forms import TitullariForm
from .models import Titullari



def titullari_list(request):
    qs = Titullari.objects.all()
   
    context = {'qs': qs}
    template_name = 'titullari/t_list.html'
    return render(request, template_name, context)

def titullari_create(request):
    if request.method == 'POST':
        form = TitullariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('titullari_dashboard')
    else:
        form = TitullariForm()

    context = {
        "form": form
        }
    template_name = 'titullari/t_create.html'
    return render(request, template_name, context)

def titullari_dashboard(request):
    titullaret_list = Titullari.objects.all()
    # Gjejmë titullarin aktual nëse ekziston
    current = Titullari.objects.filter(is_active=True).first()

    if request.method == "POST":
            selected_id = request.POST.get('titullari_select')
            if selected_id:
                try:
                    selected = Titullari.objects.get(pk=selected_id)
                except Titullari.DoesNotExist:
                    selected = None
                else:
                    # Ç'aktivizojmë të gjithë të tjerët
                    Titullari.objects.update(is_active=False)
                    # Aktivizojmë vetëm të zgjedhurin
                    selected.is_active = True
                    selected.save()

                    # Pasi e zgjodhe, kthehu diku (home, list, etj.)
                    return redirect("ushtar_list")  # ose 'firmat_list'


    context = {
        "titullaret_list": titullaret_list,
        'titullari_aktiv': current, 
        # Ky përdoret për ta mbajtur opsionin të zgjedhur
        'titullari_select': current.id if current else '', 
        }
    return render(request, "titullari/t_dashboard.html", context)

def titullari_update(request, pk):
    obj = get_object_or_404(Titullari, pk=pk)
    if request.method == 'POST':
        form = TitullariForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('titullari_list')
        else:
            print('Form errors:', form.errors)
    else:
        form = TitullariForm(instance=obj)
    context = {'obj': obj, 'form': form}
    template_name = 'titullari/t_update.html'
    return render(request, template_name, context)

def titullari_delete(request, pk):
    obj = get_object_or_404(Titullari, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('titullari_list')

    context = {'obj': obj}
    template_name = 'titullari/t_delete.html'
    return render(request, template_name, context)

