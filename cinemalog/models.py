from django.db import models

# Create your models here.
class WatchList(models.Model):

    class Meta:
        verbose_name = "鑑賞記録"
        verbose_name_plural = "鑑賞記録"

    image = models.ImageField(verbose_name="サムネイル", upload_to="thumbnail/", blank=True, null=True)
    title = models.CharField(verbose_name="タイトル", max_length=200)
    date = models.DateField(verbose_name="日付", auto_now_add=True)
    comment = models.TextField(verbose_name="コメント", blank=True, null=True)

    def __str__(self):
        return self.title
