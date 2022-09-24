from django.urls import path
from haberler.api import views as api_views

urlpatterns = [
    path('makaleler/', api_views.MakaleListAPIView.as_view(), name='article-list'),
    path('makaleler/<int:pk>', api_views.MakeleDetailAPIView.as_view(), name='article-detail'),
]

# urlpatterns = [
#     path('makaleler/', api_views.makale_list_create_view, name='article-list'),
#     path('makaleler/<int:pk>', api_views.makale_detail_api_view, name='article-detail'),
# ]