from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<int:post_id>/', views.post_detail, name='post_detail') ,
    path('profile/<int:user_id>', views.user_dashboard, name='dashboard' ) ,
    path('category/<int:cat_id>', views.post_categories, name='post_categories' ) ,
    path('add-post/', views.add_post, name='add_post') ,
    path('delete-post/<int:user_id>/<int:post_id>', views.delete_post, name='delete_post') ,
    path('edit-post/<int:user_id>/<int:post_id>', views.edit_post, name='edit_post') ,
    path('add-reply/<int:post_id>/<int:comment_id>', views.add_reply, name='add_reply') ,
    path('', views.all_posts, name='all_posts') ,
]



