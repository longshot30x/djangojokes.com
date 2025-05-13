from django.urls import path
from .views import JobAppView, JobAppThanksView

app_name = 'jobs'

urlpatterns = [
    path('apply/', JobAppView.as_view(), name='apply'),
    path('apply/thanks/', JobAppThanksView.as_view(), name='thanks'),
]
