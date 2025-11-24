from django.shortcuts import render, redirect, get_object_or_404
from .forms import FirmatForm
from .models import Firmat


def firmat_list(request):
    firmat = Firmat.objects.all()
    
    context = {'firmat': firmat}
    template_name = 'firmat/f_list.html'
    return render(request, template_name, context)

def firmat_create(request):
    if request.method == 'POST':
        form = FirmatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firmat_dashboard')
    else:
        form = FirmatForm()

    context = {"form": form}
    template_name = 'firmat/f_create.html'
    return render(request, template_name, context)

def firmat_dashboard(request):
    # Lista e të gjitha rreshtave të Firmat
    firmat_list = Firmat.objects.all()

    # Firmëtarët aktual aktiv (nëse ekziston)
    current = Firmat.objects.filter(is_active=True).first()

    if request.method == "POST":
        selected_id = request.POST.get("firma_select")

        if selected_id:
            try:
                selected = Firmat.objects.get(pk=selected_id)
            except Firmat.DoesNotExist:
                selected = None
            else:
                # Ç'aktivizojmë të gjithë
                Firmat.objects.update(is_active=False)
                # Aktivizojmë vetëm të zgjedhurin
                selected.is_active = True
                selected.save()

                # Kthehu te ushtar_list siç ke bërë
                return redirect("ushtar_list")

        # Nëse s’ka zgjedhje apo ka gabim, thjesht bie poshtë dhe rishfaq faqen

    context = {
        "firmat_list": firmat_list,
        "firmetaret_aktiv": current,
        # Ky përdoret për ta mbajtur option-in të zgjedhur
        "firma_select": current.id if current else "",
    }
    return render(request, "firmat/f_dashboard.html", context)

def firmat_update(request, pk):
    obj = get_object_or_404(Firmat, pk=pk)
    if request.method == 'POST':
        form = FirmatForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('firmat_list')
        else:
            print('Form errors:', form.errors)
    else:
        form = FirmatForm(instance=obj)
    context = {'obj': obj, 'form': form}
    template_name = 'firmat/f_update.html'
    return render(request, template_name, context)

def firmat_delete(request, pk):
    obj = get_object_or_404(Firmat, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('firmat_list')

    context = {'obj': obj}
    template_name = 'firmat/f_delete.html'
    return render(request, template_name, context)

