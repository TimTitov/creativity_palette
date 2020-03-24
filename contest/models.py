from django.db import models


class ClassContest(models.Model):
    сontest_title = models.CharField(max_length=100)
    сontest_date = models.DateTimeField()
    сontest_image = models.TextField(blank=True, null=True)
    сontest_text = models.TextField()

    def сontest_files(self):
        list = [{i.file} for i in ClassFile.objects.filter(feed=self)]
        return list

    class Meta:
        verbose_name = 'Contest'
        verbose_name_plural = 'Contests'

class ClassFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    feed = models.ForeignKey(ClassContest, on_delete=models.CASCADE)

    # def to_contest(self):
    #     feed = self.feed
    #     ClassFile.objects.filter(=self)
    #     return feed
    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

