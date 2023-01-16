from django.views.generic import TemplateView
from django.urls import path

# URLConf
urlpatterns = [
    # path('', TemplateView.as_view(template_name='core/index.html'))
]

from django.views.generic import TemplateView

urlpatterns = [
    # ...
    # Route TemplateView to serve Swagger UI template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path('swagger-ui/', TemplateView.as_view(
        template_name='core/index.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]