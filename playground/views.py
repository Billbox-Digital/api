from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
import requests
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view



logger = logging.getLogger(__name__) 

# class HelloView(APIView):
#     def get(self, request):
#         try:
#             logger.info('Calling httpbin')
#             response = requests.get('https://httpbin.org/delay/2')
#             logger.info('Received the response')
#             data = response.json()
#         except requests.ConnectionError:
#             logger.critical('httpbin is offline')
#         return render(request, 'hello.html', {'name': 'Mosh'})



class HelloView(APIView):
    schema_view = get_swagger_view(title='Pastebin API')
    urlpatterns = [
    url(r'^$', schema_view)]