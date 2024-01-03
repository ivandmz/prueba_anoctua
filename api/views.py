from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cotizacion
from .serializers import CotizacionSerializer
from django.db.models import Avg


# Create your views here.
class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer

    @action(detail=False, methods=['get'])
    def promediar_periodo(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio', None)
        fecha_fin = request.query_params.get('fecha_fin', None)

        if fecha_inicio and fecha_fin:
            promedio = Cotizacion.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).aggregate(Avg('tipo_de_cambio'))
            response_data = {
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'promedio_tipo_de_cambio': promedio['tipo_de_cambio__avg']
            }
            return Response(response_data)
        else:
            return Response({'error': 'Se requieren los parámetros fecha_inicio y fecha_fin.'}, status=400)
