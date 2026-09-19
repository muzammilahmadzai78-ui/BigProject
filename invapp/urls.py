from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_home_view, name='create'),
    path('view/', views.create_read_view, name='product_list'),
    path('update/<int:product_id>/', views.create_update_view, name='update'),
    path('delete/<int:product_id>/', views.create_delete_view, name='delete'),
    path('register/', views.register_account, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('detail/<int:product_id>/', views.create_product_detail, name='detail'),
    path('profile/', views.create_user_profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)