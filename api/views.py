from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cotizacion, Compra
from .serializers import CotizacionSerializer, CompraSerializer
from django.db.models import Avg
from datetime import timedelta


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


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def create(self, request):
        fecha = request.POST['fecha']
        monto = request.POST['monto']

        if fecha and monto:
            cotizacion = Cotizacion.objects.filter(fecha__lte=fecha).order_by('-fecha').first()

            if cotizacion:
                data = {'cotizacion': cotizacion.tipo_de_cambio, 'monto': monto, 'fecha_de_compra': fecha}
                serializer = CompraSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                print("Nueva compra ingresada al sistema.")
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'error':'No hay cotización disponible para la fecha de compra o fechas anteriores.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Debe ingresar fecha y monto para generar una nueva compra.")
            return Response({'error':'Debe ingresar fecha y monto para generar una nueva compra.'}, status=status.HTTP_400_BAD_REQUEST)