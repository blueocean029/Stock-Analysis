import json

from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status as st
from algo_task.utils import get_data_from_excel , get_ticker_list_from_excel


class StockAnalysis(viewsets.ViewSet):

	def list(self, request):
		response = get_ticker_list_from_excel() 
		return Response(response, status=st.HTTP_200_OK)


	def retrieve(self, request, pk=None):
		response = get_data_from_excel(pk) 
		return Response(response, status=st.HTTP_200_OK)
