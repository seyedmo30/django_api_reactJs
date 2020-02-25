<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.urls import reverse_lazy
from phone import views
from rest_framework.urlpatterns import format_suffix_patterns
from phone.api import views as vv
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', vv.PhoneList.as_view()),
    path('api/create/', vv.PhoneCreate.as_view(), name='create'),
    path('api/<int:id>/delete/', vv.PhoneDelete.as_view(), name='delete'),
    path('api/search/', vv.QuestionsAPIView.as_view()),


    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('contacts/<int:grp_id>/', views.contacts, name='contacts'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.contacts, name='contacts'),
    path('contacts/<int:grp_id>/delete/<int:contact_id>/',
         views.delete, name='delete'),
    path('contacts/delete/<int:contact_id>/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name='add'),
    path('contacts/update/<int:contact_id>/', views.update, name='update'),
    path('add_grp/', views.add_grp, name='add_grp'),
    path('search/', views.post_search, name='post_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======

from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.urls import reverse_lazy
from phone import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('contacts/<int:grp_id>/',views.contacts ,name='contacts'),
    path('contacts/', views.contacts,name='contacts'),
    path('', views.contacts,name='contacts'),
    path('contacts/<int:grp_id>/delete/<int:contact_id>/',views.delete ,name='delete'),
    path('contacts/delete/<int:contact_id>/',views.delete ,name='delete'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('add/', views.add,name='add'),
    path('contacts/update/<int:contact_id>/',views.update ,name='update'),
    path('add_grp/', views.add_grp,name='add_grp'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 2a6c62489d1acf598d77c6946474d1a50c5119bc
