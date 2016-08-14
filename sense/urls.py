from django.conf.urls import url
from django.contrib import admin
from metrics.views import Index, Register, API, Clean
import startup

urlpatterns = [
    url(r'^$', Index),
    url(r'^api/', API),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', Register),
    url(r'^clean/', Clean),
]
