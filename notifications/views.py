from django.shortcuts import render

# Create your views here.

def notifications_page_view(request):
    return render(request, 'notifications/notification_page.html')