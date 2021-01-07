from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import TemplateView, ListView

from .models import Receta, Ingrediente, Paso
import json
from web.antlr.main import web_main

class IndexView(TemplateView):
    template_name = 'web/index.html'

    def post(self, request):
        print(request.POST)
        text = request.POST['receta']
        
        try:
            print(text)
            recetas_dict = web_main(text)
            return JsonResponse({'error': False, 'result': 'La receta ha sido almacenada correctamente'},
                                 status=200)
        except Exception as e:
            return JsonResponse({'error': True, 'result': str(e)}, status=200)

class RecetasView(ListView):
    template_name = 'web/recetas.html'
    context_object_name = 'recetas'
    model = Receta
    paginate_by = 1

    def get_queryset(self):
        return super().get_queryset().order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredientes'] = Ingrediente.objects.all().order_by('nombre')
        context['pasos'] = Paso.objects.all().order_by('num_paso')
        return context
