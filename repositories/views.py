from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Repository


@login_required
def repositories(request):
    """The homepage of repositories as well containing the list of repositories made by a user."""
    return render(request, 'repositories/index.html')

@login_required
def repositories_list(request):
    """Show all topics."""
    repositories_list = Repository.objects.filter(owner= request.user).order_by('date_added')
    context = {'repositories_list' : repositories_list}
    return render(request, 'repositories/repositories.html', context= context)

def new_repository(request):
    pass