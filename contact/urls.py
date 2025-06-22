# type:ignore
from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # user
    path('user/create/', views.register, name='register'),
]








# # type:ignore
# from django.urls import path

# from contact import views

# app_name = 'contact'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('search/', views.search, name='search'),

#     # contact (CRUD)
#     path('contact/<int:contact_id>/', views.contact, name='contact'),
#     path('contact/create/', views.create, name='create'),
#     path('contact/<int:contact_id>/update/', views.update, name='update'),
#     path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
# ]








# # type:ignore
# from django.urls import path

# from contact import views

# app_name = 'contact'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('search/', views.search, name='search'),

#     # contact (CRUD)
#     path('contact/<int:contact_id>/', views.contact, name='contact'),
#     path('contact/create/', views.create, name='create'),
#     path('contact/<int:contact_id>/update/', views.update, name='update'),
# ]








# # type:ignore
# from django.urls import path

# from contact import views

# app_name = 'contact'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('search/', views.search, name='search'),

#     # contact (CRUD)
#     path('contact/<int:contact_id>/', views.contact, name='contact'),
#     path('contact/create/', views.create, name='create'),
# ]








# from django.urls import path

# from contact import views

# app_name = 'contact'

# urlpatterns = [
#     path('<int:contact_id>/', views.contact, name='contact'),  # type:ignore
#     path('search/', views.search, name='search'),  # type:ignore
#     path('', views.index, name='index'),  # type:ignore
# ]








# from django.urls import path

# from contact import views

# app_name = 'contact'

# urlpatterns = [
#     path('<int:contact_id>/', views.contact, name='contact'),  # type:ignore
#     path('', views.index, name='index'),  # type:ignore
# ]





# from django.urls import path

# from contact import views

# app_name = 'contact'

# urlpatterns = [
#     path('', views.index, name='index'),
# ]
