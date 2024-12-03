from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.utils import timezone

def active_users(request):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now()).count()
    return JsonResponse({'active_users': active_sessions})