from django.shortcuts import render
from django.http import Http404
from apps.words.models import Word

# convert querySet to list
words_list = list(Word.objects.all())

# get wordcount with len()
total_wordcount = len(words_list)

# Define a view function 'static_page' that takes a 'request' and a 'pagename' as parameters.
def static_page(request, pagename):
    try:
        # Try to render an HTML template with the given 'pagename'.
        # Create a 'context' dictionary to pass data to the template.
        context = {
            'pagename': pagename,
            # Add any other data to context here.
            'wordcount': total_wordcount
        }
        # Use the 'render' function to render the template with the provided 'context'.
        return render(request, f"{pagename}.html", context)
    except:
        # If an exception occurs during rendering, raise a 404 error.
        raise Http404("Page not found")
