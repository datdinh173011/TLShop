from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    # ex: /core/
    path('', views.index, name='index'),
    # ex: /core/3/
    path('<int:question_id>', views.detail, name='detail'),
    # ex: /core/3/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /core/3/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]