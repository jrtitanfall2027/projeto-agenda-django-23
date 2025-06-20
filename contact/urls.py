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
]








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
