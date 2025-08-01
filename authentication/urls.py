# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path, include     # URL routing
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Static files serving
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

# Define URL patterns
urlpatterns = [
    # path("", include("players.urls")),
    path("admin/", admin.site.urls),          # Admin interface
    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page  
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'), # LOGOUT 
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()