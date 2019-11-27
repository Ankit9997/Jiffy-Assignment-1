from POC.models import Registration
from .serializers import POCSerializer
from rest_framework import serializers
from rest_framework import generics
from rest_framework import mixins

class POCAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class=POCSerializer

    def get_queryset(self):
        qs=Registration.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.objects.filter(content_icontains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class POCDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class=POCSerializer


    def get_queryset(self):
        qs=Registration.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.objects.filter(content_icontains=query)
        return qs

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
