from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

def users(request):
    """API endpoint for users."""
    # Create pedro user if it doesn't exist (for testing)
    pedro, created = User.objects.get_or_create(
        username='pedro',
        defaults={
            'email': 'pedro@example.com',
            'first_name': 'Pedro',
            'last_name': '',
        }
    )
    
    users_list = []
    for user in User.objects.all():
        users_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
    return JsonResponse({'message': 'Users endpoint', 'users': users_list})

