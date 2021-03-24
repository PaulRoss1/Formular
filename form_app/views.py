from django.shortcuts import render, redirect
from .forms import FormularForm

def index(request):
    if request.method == 'POST':
        form = FormularForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('form_app:index')
    else:
        form = FormularForm()
    context = {'form': form}
    return render(request, 'form_app/index.html', context)

    # form = FormularForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    # context = {
    #     'form': form
    # }
    # return render(request, 'form_app/index.html', context)

