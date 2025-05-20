from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key]= link.url
    return ctx

def redes_dict(request):
    links = Link.objects.all()
    return {"social_links": links}