from django.views.defaults import page_not_found


def notFound(request, template_name='404.html'):
    return page_not_found(request, template_name=template_name)
