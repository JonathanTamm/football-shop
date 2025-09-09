from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Football Shop', 
    }

    return render(request, "main.html", context)