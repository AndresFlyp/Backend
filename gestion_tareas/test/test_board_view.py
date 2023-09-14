from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models.board import Board 
from ..serializers.board_serializers import BoardSerializer

class BoardsViewTestCase(APITestCase):
    
    def setUp(self):
        self.board = Board.objects.create(title="Test Board")
        self.url = reverse('board') 
        
    def test_get_single_board(self):
        response = self.client.get(reverse('board_detail', args=[self.board.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BoardSerializer(self.board)
        self.assertEqual(response.data, serializer.data)
        
    def test_get_all_boards(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['Boards']), 1)  
        
    def test_get_all_boards_empty(self):
        Board.objects.all().delete() 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
