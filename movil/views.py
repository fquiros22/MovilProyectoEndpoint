from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def endPointMovil(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        carnet = request.POST.get('carnet')

        Estudiante.objects.create(
            nombre=nombre,
            carnet=carnet
        ).save()
        data = {'data': True}
    else:
        data = {'data': False}
    return JsonResponse(data)