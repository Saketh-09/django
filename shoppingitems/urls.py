from django.urls import path, include
from . import views
from .router import router
urlpatterns = [
    path('', views.create_view, name='create_view'),
    path('listview', views.list_view, name='list_view'),
    path('<int:id>', views.detail_view, name='detail_view'),
    path('<int:id>/update', views.update_view, name='update_view'),
    path('<int:id>/delete', views.delete_view, name='delete_view'),
    path('api/items', views.shopping_list, name='apilist'),
    path('api/items/<int:pk>', views.shopping_detail, name='apidetail'),
    path('api/', include(router.urls))
]
