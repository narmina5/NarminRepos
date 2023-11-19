from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import ContactInfo
from .forms import RequestForm


def contact(request):
    contact_info = ContactInfo.objects.first()
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Muracietiniz ugurla qeyde alindi, tezlikle sizle elaqe saxlanilacaq')
            return redirect(reverse_lazy('contact'))

    context = {
        'contact_info': contact_info,
        'form': form
    }
    return render(request, 'contact/index.html', context)
