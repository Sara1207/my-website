
from django.httpimport HttpResponseRedirect
from django.shortcuts import render

from.forms import UserForm

def Register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

else:
    form = UserForm()

return render(request, 'registration.html', {'form': form})
