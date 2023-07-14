from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="글 제목")
    contents = models.TextField(verbose_name="글 내용")
    writer = models.ForeignKey('user.FcUser', on_delete=models.CASCADE,
                               verbose_name="글 작성자")  # on_delete=models.CASECASE : user가 없어지면 이와 관련된 모든 것을 지움
    tags = models.ManyToManyField('tag.Tag', verbose_name="태그")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'  # 앱들과 구분해서 db의 실제 테이블명을 짓기 위해서 사용함
        verbose_name = "패스트캠퍼스 게시글"
        verbose_name_plural = "패스트캠퍼스 게시글 목록"
