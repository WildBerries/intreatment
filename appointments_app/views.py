from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Staff
from .forms import AppointmentsForm




# Create your views here.

def setAppointment(request):
    """ Processes doctor appointment registration form.
    """
    form = AppointmentsForm()

    if request.method == 'POST' and form.is_valid:
        form = AppointmentsForm(request.POST)

        if form.is_valid():
            # 'commit=False' lets access submitted form values 'form.formFieldName'
            # and create new attributes.
            form_obj = form.save(commit=False)
            form_obj.name = addNames(last=form.cleaned_data['last_name'],
                                     first=form.cleaned_data['first_name'],
                                     patronomyc=form.cleaned_data['patronymic_name']
                                     )
            form.save()
            return HttpResponseRedirect(reverse('appointment'))
    else:
        print(form.errors)

    form_context = {'form': form}
    return render(request, 'html/appointments_form.html', context=form_context)



# data manipulation block

def addNames(*, last, first, patronomyc):
    """ Concatenates patient's three names
    into one string. """
    return '{} {} {}'.format(last, first, patronomyc)