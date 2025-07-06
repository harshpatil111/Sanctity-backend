from django.urls import path
from .views import CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView, CommentRestoreView

urlpatterns = [
  path('', CommentListView.as_view()),
  path('create/', CommentCreateView.as_view()),
  path('<int:pk>/update/', CommentUpdateView.as_view()),
  path('<int:pk>/delete/', CommentDeleteView.as_view()),
  path('<int:pk>/restore/', CommentRestoreView.as_view()),
 ]


   