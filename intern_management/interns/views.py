from django.shortcuts import render
from django.db.models import Q
from .models import Intern


def home(request):
    """Home page view with all interns and search functionality"""
    interns = Intern.objects.all()
    
    # Get search query from URL
    search_query = request.GET.get('q', '')
    
    if search_query:
        interns = interns.filter(
            Q(full_name__icontains=search_query) |
            Q(passport_id__icontains=search_query) |
            Q(department__icontains=search_query)
        )
    
    context = {
        'interns': interns,
        'search_query': search_query,
    }
    
    return render(request, 'index.html', context)
