
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from phone.models import Phone
from .serializers import PhoneSerializer, PhoneCreateSerializer, PhoneDeleteSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListCreateAPIView

from rest_framework import filters


class QuestionsAPIView(ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneList(APIView):
    def get(self, request, format=None):
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneCreate(CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneCreateSerializer


class PhoneDelete(DestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneDeleteSerializer
    lookup_field = "id"
