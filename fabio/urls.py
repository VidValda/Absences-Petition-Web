from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('petition-list/', views.petition_list, name='petition_list'),
    
    path('update/<int:petition_id>/<str:new_status>/', views.update_petition_status, name='update_petition'),
    path('create',views.create_petition,name='create_petition'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin-only/', views.AdminOnlyView.as_view(), name='admin_only_view'),
    path('update_observation/', views.update_observation, name='update_observation'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
