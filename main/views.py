from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Football Shop',
        'user_name': 'Jonathan Immanuel Tampubolon',
        'user_npm': '2406395695',
        'user_class': 'PBP F',
    }

    return render(request, "main.html", context)