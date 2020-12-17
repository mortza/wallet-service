from django.conf.urls import url, include

urlpatterns = [
    url(r'wallet/', include('wallet.urls'), name='wallet'),
]
