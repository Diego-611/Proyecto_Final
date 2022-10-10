from django.urls import path
from .views import *

urlpatterns = [
    path('receivedmessages/', viewReceivedMessages, name= 'RMessages'),
    path('sentmessages/', viewSentMessages, name= 'SMessages'),
    path('sendmessage/', viewMessages, name='FMessage'),
    path('sendblogmessage/', viewBlogMessages, name= 'BMessage'),
    path('', viewIndexMessage, name='IMessage'),
    path('sendusermessage/<id>', viewUserMessages, name='UMessage')
]

