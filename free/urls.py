from django.urls import path
from django.urls import path 
from . import views
from .views import video 

urlpatterns = [
    path('',views.index,name="index"),
    path('neet',views.neet,name="neet"),
    path('boards',views.boards,name="boards"),
    path('copy',views.copy,name="copy"),
    path('login',views.login,name ="login"),
    path('logout',views.logout,name ="logout"),
    path('signup',views.signup,name ="signup"),
    path('profile',views.profile,name ="profile"),
    # *******************jee*****************
    path('jacp',views.jacp,name ="jacp"),
    path('jacm',views.jacm,name ="jacm"),
    path('jacc',views.jacc,name ="jacc"),
    path('jamp',views.jamp,name="jamp"),
    path('jamc',views.jamc,name ="jamc"),
    path('jamm',views.jamm,name ="jamm"),
    path('jatp',views.jatp,name ="jatp"),
    path('jatc',views.jatc,name ="jatc"),
    path('jatm',views.jatm,name ="jatm"),
    # *****************board*******************
    path('bamc',views.bamc,name="bamc"),
    path('bamb',views.bamb,name="bamb"),
    path('bamp',views.bamp,name="bamp"),
    path('bamm',views.bamm,name="bamm"),
    path('batc',views.batc,name="batc"),
    path('batp',views.batp,name="batp"),
    path('batb',views.batb,name="batb"),
    path('batm',views.batm,name="batm"),
    # ***************neet*************
    path('namb',views.namb,name="namb"),
    path('namc',views.namc,name="namc"),
    path('namp',views.namp,name="namp"),
    path('natc',views.natc,name="natc"),
    path('natb',views.natb,name="natb"),
    path('natp',views.natp,name="natp"),
]
