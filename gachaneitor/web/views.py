from django.http import JsonResponse
from django.views.generic import TemplateView, ListView

from .models import Receta, Ingrediente, Paso
import json
from web.antlr.main import web_main

class IndexView(TemplateView):
    template_name = 'web/index.html'

    def post(self, request):
        text = request.POST['receta']
        
        try:
            recetas_dict = web_main(text)
            self.save_recetas(recetas_dict)
            return JsonResponse({'error': False, 'result': 'La receta ha sido almacenada correctamente'},
                                 status=200)
        except Exception as e:
            error = str(e)
            return JsonResponse({'error': True, 'result': error}, status=200)
    
    def save_recetas(self, recetas):
        for receta in recetas:
            Receta(receta["nombre"], receta["descripcion"], 
                    receta["total"]["cantidad"], receta["total"]["unidad"],
                    receta["preparacion"]["cantidad"], receta["preparacion"]["unidad"])
            
            

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
