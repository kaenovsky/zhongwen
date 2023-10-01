from django.shortcuts import render
from django.http import Http404

def static_page(request, pagename):
    try:
        context = {
            'pagename': pagename,
        }
        return render(request, f"{pagename}.html", context)
    except:
        raise Http404("Page not found")
