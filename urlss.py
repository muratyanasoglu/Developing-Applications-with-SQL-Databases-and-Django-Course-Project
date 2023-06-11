from django.urls import include, path

urlpatterns = [
    path('exams/', include('exams.urls')),
    # Other url patterns...
]
