from django.shortcuts import render


def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="blog/index.html",
        context=contexto,
    )
    
    return http_response
