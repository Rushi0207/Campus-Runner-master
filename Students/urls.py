"""campusrunner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Dashboard, ResumeView, SaveInternship, SaveProject, EligibleJobs, RegisterForJob
from django.contrib.auth.decorators import login_required

app_name = 'students'


urlpatterns = [
    path('dashboard/', login_required(Dashboard.as_view()), name='dashboard'),
    path('resume/', login_required(ResumeView.as_view()), name='resume'),
    path('save-internship/', login_required(SaveInternship.as_view()), name='save_internship'),
    path('save-projetct/', login_required(SaveProject.as_view()), name='save_project'),
    path('available-jobs/', login_required(EligibleJobs.as_view()), name='available_jobs'),
    path('register-jobs/', login_required(RegisterForJob.as_view()), name='register_jobs'),

]
