from django.db import models
from tinymce.models import HTMLField
# Create your models here.


'''

1:n
user -- key  
user -- letter
user -- sender
'''


class CustLoginRecord(models.Model):

    class Meta:
        db_table = 'cust_login_record'

    username = models.CharField(max_length=64)
    oa_session_key = models.CharField(max_length=64)
    login_time = models.DateTimeField(auto_now_add=True)


class User(models.Model):

    class Meta:
        db_table = 'user'

    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    update_time = models.DateTimeField(auto_now_add=True)


class Sender(models.Model):

    class Meta:
        db_table = 'sender'

    email = models.CharField(max_length=64)
    port = models.IntegerField()
    server = models.CharField(max_length=32)
    protocol = models.CharField(max_length=16,default='smtp')
    password = models.CharField(max_length=64)
    user = models.ForeignKey('User')


class Letter(models.Model):

    class Meta:
        db_table = 'letter'

    def __str__(self):
        return str(self.id) + self.title

    title = models.CharField(max_length=128)
    # subject = models.CharField(max_length=128)
    content = HTMLField() # 可以用富文本！！
    user = models.ForeignKey('User')


class SearchKey(models.Model):
    class Meta:
        db_table = 'search_key'

    keyword = models.CharField(max_length=64)
    user = models.ForeignKey('user')


class EmailRecord(models.Model):
    class Meta:
        db_table = 'email_record'
    keyword = models.CharField(max_length=64,default="")
    dest_mail = models.CharField(max_length=128,default="")

    # dest_company = models.CharField(max_length=128,default="")
    # dest_webiste = models.CharField(max_length=128,default="")


    send_status = models.BooleanField()

    letter_title = models.CharField(max_length=128,default="")
    # letter_content = models.TextField(default="")

    send_email = models.CharField(max_length=64,default="")
    port = models.IntegerField()
    server = models.CharField(max_length=32,default="")
    protocol = models.CharField(max_length=16,default="")

    user = models.ForeignKey('User')
    ip = models.CharField(max_length=64,)
    send_time = models.DateTimeField(auto_now_add=True)


class WaitSendCustomer(models.Model):
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'wait_send_customer'

    keyword = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    website = models.CharField(max_length=256)
    update_time = models.DateTimeField(auto_now_add=True)
    sort_id = models.IntegerField(default=0)
    user = models.ForeignKey(to='User')


class SearchResult(models.Model):

    class Meta:
        db_table = 'search_result'

    keyword = models.CharField(max_length=128,db_index=True)
    company = models.CharField(max_length=512,default="")
    website = models.CharField(max_length=512,default="")
    description = models.CharField(max_length=512,default="")
    email = models.CharField(max_length=512,default="")
    addr = models.CharField(max_length=512,default="")
    phone = models.CharField(max_length=256,default="")
    facebook = models.CharField(max_length=512,default="")
    twitter = models.CharField(max_length=512,default="")
    query_flag = models.CharField(max_length=4,default=1)

    user = models.ManyToManyField(to="User")



class SensitiveWord(models.Model):
    word = models.CharField(max_length=128)




class RequestCount(models.Model):
    count = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    customer = models.CharField(max_length=128)

