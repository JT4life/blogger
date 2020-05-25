from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

#app_name = 'blog'
urlpatterns = [
    #path('', views.index, name="index"),
    #path('', views.PostList.as_view(), name='home'),
    url(r'^$', views.index, name="index"),
    url(r'^add_blog/$', views.addBlog, name="add_blog"),
    url(r'^add_comment/$', views.add_comment, name="add_comment"),
    url(r'^add_comment_submit/$', views.add_comment_submit, name="add_comment_submit"),
    url(r'^login/$', views.login, name="login"),
    url(r'^add_blog_form_submit/$', views.add_blog_form_submit, name="add_blog_form_submit"),
    path('login/', LoginView.as_view(template_name='blogReview/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name="logout"),
    path('register/', views.registerView, name="register_url"),
    path('dashboard/', views.dashboardView, name="dashboard"),

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #url(r'^post_detail/$', views.PostDetail.as_view(), name="post_detail"),
]