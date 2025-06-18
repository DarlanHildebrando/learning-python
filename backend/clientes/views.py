from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction, IntegrityError
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@transaction.atomic

from .models import Clientes

# Create your views here.

def ClientView(request):
    if request.method != 'POST'
        return  JsonResponse({'Método não permitido'}, status=405)

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')    
     

    return HttpResponse('HelloWorld')
    
