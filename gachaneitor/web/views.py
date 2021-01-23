from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
import traceback

from web.models import Receta, Ingrediente, Paso
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
            traceback.print_exc()
            return JsonResponse({'error': True, 'result': error}, status=200)
    
    def save_recetas(self, recetas):
        print(recetas)
        for receta in recetas:
            receta_instance = Receta(nombre=receta["nombre"], descripcion=receta["descripcion"], tmp_preparacion=receta["tiempo"]["preparacion"]["cantidad"], 
                                    ud_tmp_preparacion=receta["tiempo"]["preparacion"]["unidad"], 
                                    tmp_total=receta["tiempo"]["total"]["cantidad"], 
                                    ud_tmp_total=receta["tiempo"]["total"]["unidad"])
            
            receta_instance.save()
            for ingrediente in receta["ingredientes"]:
                ingrediente_instance = Ingrediente(receta=receta_instance, nombre=ingrediente,
                            cantidad=receta["ingredientes"][ingrediente]["cantidad"],
                            ud_cantidad=receta["ingredientes"][ingrediente]["unidad"])
                ingrediente_instance.save()

            num_paso=1
            for paso in receta["pasos"]:
                tipo_verbo = paso["tipo_verbo"]
                ingredientes_str = ""
                for ingrediente in paso["ingredientes"]:
                    ingredientes_str += ingrediente + " " + str(paso["ingredientes"][ingrediente]["cantidad"]) + paso["ingredientes"][ingrediente]["unidad"] + ", " 
                ingredientes_str = ingredientes_str[:-2]

                if tipo_verbo == "persona":
                    paso_instance = Paso(receta=receta_instance, num_paso=num_paso, 
                                        verbo=paso["verbo"], tipo_verbo=tipo_verbo, ingredientes=ingredientes_str)
                    paso_instance.save()
                elif tipo_verbo == "cocinar":
                    paso_instance = Paso(receta=receta_instance, num_paso=num_paso, verbo=paso["verbo"], 
                                            tipo_verbo=tipo_verbo, ingredientes=ingredientes_str, 
                                            temperatura=paso["temperatura"]["cantidad"], 
                                            ud_temperatura=paso["temperatura"]["unidad"], 
                                            tiempo=paso["tiempo"]["cantidad"], 
                                            ud_tiempo=paso["tiempo"]["unidad"])
                    paso_instance.save()
                elif tipo_verbo == "mover":
                    paso_instance = Paso(receta=receta_instance, num_paso=num_paso, 
                                        verbo=paso["verbo"], tipo_verbo=tipo_verbo, 
                                        ingredientes=ingredientes_str, 
                                        velocidad=int(paso["velocidad"]),
                                        tiempo=paso["tiempo"]["cantidad"], 
                                        ud_tiempo=paso["tiempo"]["unidad"])
                    paso_instance.save()              
                num_paso += 1
                

            
            

class RecetasView(ListView):
    template_name = 'web/recetas.html'
    context_object_name = 'recetas'
    model = Receta
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredientes'] = Ingrediente.objects.all().order_by('nombre')
        context['pasos'] = Paso.objects.all().order_by('num_paso')
        return context
