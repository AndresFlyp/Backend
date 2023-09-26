from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models.board import Board 
from ..serializers.board_serializers import BoardSerializer

class BoardsViewTestCase(APITestCase):
    
    def setUp(self):
        self.board = Board.objects.create(title="Test Board")

    def test_list_boards(self):
        url = reverse("boards_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_board(self):
        url = reverse("boards_create")
        data = {"title": "New Board"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_board(self):
        url = reverse("board_detail", args=[self.board.pk])
        data = {"title": "Updated Board"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_board(self):
        url = reverse("board_detail", args=[self.board.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_board_not_found(self):
        url = reverse("board_detail", args=[1000]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
