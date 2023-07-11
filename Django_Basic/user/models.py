from django.db import models


# Create your models here.
class FcUser(models.Model):
    user_name = models.CharField(max_length=64, verbose_name="사용자 이름")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")

    class Meta:
        db_table = 'fastcampus_fcuser' # 앱들과 구분해서 db의 실제 테이블명을 짓기 위해서 사용함
