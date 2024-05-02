from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView,TokenVerifyView

routes = DefaultRouter()



routes.register('student',views.StudentApi,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
    path('', include(routes.urls)),
]
