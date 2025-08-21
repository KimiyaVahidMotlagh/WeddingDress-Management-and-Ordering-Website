from django.urls import path
from .views import (
    login_view, logout_view, signup_view, post_login_redirect_view,
    body_type_result_view, measurements_view, recommendations_view,
    user_home_view,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('post-login-redirect/', post_login_redirect_view, name='post_login_redirect'),
    path('measurements/', measurements_view, name='measurements'),
    path('body-type-result/', body_type_result_view, name='body_type_result'),
    path('recommendations/', recommendations_view, name='recommendations'),
    path('user-home/', user_home_view, name='user_home'),
    path('logout/', logout_view, name='logout'),
]
