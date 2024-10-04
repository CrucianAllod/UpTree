from django.urls import path
from .views import GenericPageView

urlpatterns = [

    path('', GenericPageView.as_view(), name='home'),
    path('<path:page_path>/', GenericPageView.as_view(), name='generic_page'),
    path('suda/', GenericPageView.as_view(), name='suda'),

]