from django.contrib import admin
# from embed_video.admin import AdminVideoMixin
from . models import video
# from . models import jacp
from . models import jacms
from . models import jacps
from . models import jaccs
from . models import jamcs,jamps,jamms
from . models import jatcs,jatps,jatms
# from . models import video

# class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
# class MyModelAdmin(admin.ModelAdmin):
    # pass

admin.site.register(video)
admin.site.register(jacps)
admin.site.register(jacms)
admin.site.register(jaccs)
admin.site.register(jamps)
admin.site.register(jamcs)
admin.site.register(jamms)
admin.site.register(jatps)
admin.site.register(jatcs)
admin.site.register(jatms)


    

# admin.site.register(video)
# Register your models here.
