from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406395695',
        'name': 'Jonathan Immanuel Tampubolon',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)