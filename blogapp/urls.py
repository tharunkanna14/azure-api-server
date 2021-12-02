from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('',views.index),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('search/',views.search,name='search' ),
	path('api/v1/posts/', views.post_list.as_view(),name='api-postlist-view'),
	path('api/v1/posts/<int:pk>/', views.post_details.as_view(),name='api-postdetails-view'),

	path('api/v2/secrets/', views.secretlistview.as_view(),name='secret-list-view'),
	path('api/v2/secrets/<int:pk>/', views.secretdetailview.as_view(),name='secret-detail-view'),





]
