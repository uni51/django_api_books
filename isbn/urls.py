from django.urls import path
from . import views

app_name = "isbn"

urlpatterns = [
    path('list/', views.BookListView.as_view(), name='book_list'),
    path('create/', views.SearchWordCreateView.as_view(), name='create'),
    path('create_done/', views.create_done, name='create_done'),
    path('word_list/', views.WordListView.as_view(), name='word_list'), 
    path('update/<int:pk>/', views.WordUpdateView.as_view(), name='update'),
    path('update_done/', views.update_done, name='update_done'),         
]