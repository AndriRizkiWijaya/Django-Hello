from django.shortcuts import render

# Create your views here.
def login_view(request):
    template = 'account/login.html'
    context  = {
        'title_page':'Login'
    }
    return render(request, template, context)
