from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # El navegador está enviando datos de login
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                # Si el usuario existe, devuelve un éxito
                return JsonResponse({'status': 'ok'})
            else:
                # Si las credenciales son incorrectas
                return JsonResponse({'status': 'fail'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'error': 'JSON inválido'}, status=400)
    
    # Esta es la parte que faltaba:
    # Cuando la petición es GET, devuelve un mensaje de error claro
    return JsonResponse({'error': 'Se requiere una petición POST para el login'}, status=405)