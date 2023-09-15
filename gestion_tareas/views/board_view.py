
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from ..serializers.board_serializers import BoardSerializer
from ..models.board import Board




class BoardsView(APIView):
    
    def get(self, request, pk=None):
        try:
            if pk is not None:
                board_obj = Board.objects.get(pk=pk)
                serializer = BoardSerializer(board_obj)
                return Response(serializer.data)
        
            
            else:
                queryset = Board.objects.all()
                serializer = BoardSerializer(queryset, many=True)

                if queryset.exists():
                    response_data = {"message": "Success", 'Boards': serializer.data}
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    response_data = {"message": "No boards found"}
                    return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            response_data = {"message": str(e)}
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            
    def post(self, request):

        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {"message": "Created board!"}
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        else:
            response_data = {"message": "Error", "errors": serializer.errors}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk=None):

        try:
            board_obj = Board.objects.filter(pk=pk).first()

            if board_obj:
                serializer = BoardSerializer(board_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    response_data = {"message": "Updated board!", 'Boards': serializer.data}
                    return Response(response_data)
        
            else:
                return Response({"message": "Board not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            response_data = {"message": str(e)}
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, pk=None):

        try:
            board_to_delete = Board.objects.filter(pk=pk).first()
            if board_to_delete:
                board_to_delete.delete()
                response_data = {"message": "Deleted board!"}
                return Response(response_data)
            else:
                return Response({"message": "Board not found"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            response_data = {"message": str(e)}
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

