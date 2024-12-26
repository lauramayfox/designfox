from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('designquote/', include('designquote.urls')),
    path('contact/', include('contact.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('services/', TemplateView.as_view(template_name="services.html"), name='services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'designfox.views.handler404'

