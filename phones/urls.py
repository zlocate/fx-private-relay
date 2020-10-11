from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='phones-index'),
    path('twilio-voice-webhook', views.twilio_voice_webhook),
    path('main-twilio-webhook', views.main_twilio_webhook),
    path('twilio-proxy-out-of-session', views.twilio_proxy_out_of_session),
]
