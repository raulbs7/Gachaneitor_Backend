from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import TemplateView, ListView

from .models import Receta, Ingrediente, Paso


# Create your views here.

class IndexView(TemplateView):
    template_name = 'web/index.html'

    def post(self, request):
        result = request.POST['receta']
        return JsonResponse({'receta': result}, status=200)

'''def index(request):
    template = loader.get_template('web/index.html')
    context = {}
    return HttpResponse(template.render(context, request))'''


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


'''def recetas(request):
    template = loader.get_template('web/recetas.html')
    recetas = Receta.objects.all().order_by('nombre')
    ingredientes = Ingrediente.objects.all().order_by('nombre')
    pasos = Paso.objects.all().order_by('num_paso')
    context = {
        'recetas': recetas,
        'ingredientes': ingredientes,
        'pasos': pasos
    }
    return HttpResponse(template.render(context, request))'''
