
from django.contrib import admin
from django.urls import path,include
from home.views import home, books_page, feedback_page, about_page, index_page, login_page, signup_page, question_page, profile_page

admin.site.site_header = "Peer Learn Connect Admin"
admin.site.site_title = "Peer learn connect Admin Portal"
admin.site.index_title = "Welcome to Peer Learn Connect Portal"

urlpatterns = [
    path('', home ,name="home"),
    path('books',books_page,name="books_page"),
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('feedback',feedback_page ,name="feedback_page"),
    path('about',about_page,name="about_page"),
    path('index',index_page,name="index_page"),
    #path('login',login_page,include('home.urls')),
    path('signup',signup_page,name="signup_page"),
    path('question',question_page,name="question_page"),
    path('profile',profile_page,name="profile_page"),
    path('login/', login_page, name='login'),
]
