from django.http import HttpResponse
from django.template import Template, Context

def static_page(request, pagename):
    ext_doc = open("./zhongwen/templates/{}.html".format(pagename))
    templ = Template(ext_doc.read())
    ext_doc.close()
    ctx = Context({})
    document = templ.render(ctx)
    return HttpResponse(document)