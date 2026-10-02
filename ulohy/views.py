from django.shortcuts import render, HttpResponse

# Create your views here.
def ahoj(request):
    return HttpResponse("<h1>AHOJJJJJJ svet</h1>")

def o_mne(request):
    kontext = {
        "meno": "Jozef",
        "vek":18,
        "zaluby":['hudba', 'pivo', 'programovanie']
    }
    return render(request, 'ulohy/o_mne.html', kontext)