from django.conf.urls import url,include
from search import views

urlpatterns = [
    url(r'^engine/', views.engine),
    url(r'^results/', views.results),
    url(r'^issensitive/', views.issensitive),
    url(r'^yellow/', views.yellow),
    url(r'^foreign_enterprise/', views.yellow),
    url(r'^get_email/', views.get_email),
    url(r'^get_socials/', views.get_socials),
    url(r'^get_export_india_totalnums/', views.get_export_india_totalnums),
    url(r'^get_yellow_page_nums/', views.get_yellow_page_nums),
    url(r'^test/', views.test),

]
