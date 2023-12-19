from django.urls import path
from user_profile.views import user_profile, get_user_json, edit_profile, show_user_json, edit_profile_flutter, edit_profile_flutter_user


app_name = 'user_profile'

urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('get-user/', get_user_json, name='get_user_json'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('show-user/', show_user_json, name='show_user_json'),
    path('edit-profile-admin/', edit_profile_flutter, name='edit_profile'),
    path('edit-profile-user/', edit_profile_flutter_user, name='edit_profile_flutter_user'),
]