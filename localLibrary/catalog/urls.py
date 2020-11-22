# Use include() to add paths from the catalog application 
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic import RedirectView


# urlpatterns += [
#     path('catalog/', include('catalog.urls')),
#     path('', RedirectView.as_view(url='catalog/', permanent=True)),
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ]

urlpatterns = [

]