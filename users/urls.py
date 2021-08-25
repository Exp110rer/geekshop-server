from django.urls import path
import users.views

app_name = 'users'

urlpatterns = [
    path('login/', users.views.login, name='login'),
    path('registration/', users.views.registration, name='registration')
]