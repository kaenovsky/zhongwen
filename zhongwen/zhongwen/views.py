from django.http import HttpResponse
import datetime
from django.template import Template, Context

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)

def static_page(request, pagename):
    ext_doc = open("./zhongwen/templates/{}.html".format(pagename))
    templ = Template(ext_doc.read())
    ext_doc.close()
    ctx = Context({})
    document = templ.render(ctx)
    return HttpResponse(document)