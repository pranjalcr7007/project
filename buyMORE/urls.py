

from django.apps import apps
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
admin.autodiscover()

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
   
    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('admin/', admin.site.urls),

    path('', include(apps.get_app_config('oscar').urls[0])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    # PayPal Express integration...
    path('checkout/paypal/', include('paypal.express_checkout.urls')),
    # Dashboard views for Payflow Pro
    path('dashboard/paypal/payflow/', apps.get_app_config("payflow_dashboard").urls),
    # Dashboard views for Express
    path('dashboard/paypal/express/', apps.get_app_config("express_dashboard").urls),
    # Dashboard views for Express Checkout
    path('dashboard/paypal/express-checkout/', apps.get_app_config('express_checkout_dashboard').urls),
    
   
)
