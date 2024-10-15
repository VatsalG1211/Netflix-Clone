from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, 'templates/404.html', status=404)

