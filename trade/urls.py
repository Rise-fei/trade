"""trade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from user import views as user_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^index/', user_views.index),
    url(r'^remote_ip/', user_views.remote_ip),
    url(r'^fanyi/', user_views.fanyi),
    url(r'^login/', user_views.login),
    url(r'^logout/', user_views.logout),
    url(r'^login_check/', user_views.login_check),
    url(r'^check_status/', user_views.check_status),
    url(r'^logout_all_cuser/', user_views.logout_all_cuser),
    url(r'^offline/', user_views.offline),


    url(r'^letter/', user_views.letter),
    url(r'^show_letter/(\d+)/', user_views.show_letter),
    url(r'^delete_letter/', user_views.delete_letter),

    url(r'^mail/', user_views.mail),
    url(r'^add_mail/', user_views.add_mail),
    url(r'^test_email/', user_views.test_email),
    url(r'^delete_email/', user_views.delete_email),
    url(r'^upload_email/', user_views.upload_email),
    url(r'^download_csv/', user_views.download_csv),
    url(r'^send_mail/', user_views.send_mail_crm),
    url(r'^send_mail_ajax/', user_views.send_mail_ajax),
    url(r'^send_mail_extend/', user_views.send_mail_extend),
    url(r'^email_record/', user_views.email_record),
    url(r'^delete_record/', user_views.delete_record),

    url(r'^import_customer/', user_views.import_customer),
    url(r'^send_target/', user_views.send_target),
    url(r'^add_target/', user_views.add_target),
    url(r'^add_target2/', user_views.add_target2),
    url(r'^upload_target/', user_views.upload_target),
    url(r'^delete_target/', user_views.delete_target),
    url(r'^tree/', user_views.tree),
    url(r'^test/', user_views.test),
    url(r'^keyword_manage/', user_views.keyword_manage),
    url(r'^delete_keyword/', user_views.delete_keyword),
    url(r'^delete_keywords/', user_views.delete_keywords),


    url(r'^delete_user_searchresult/', user_views.delete_user_searchresult),


    url(r'^$', user_views.index),
]
