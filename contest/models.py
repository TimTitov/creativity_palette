from django.db import models


class ClassContest(models.Model):
    contest_title = models.CharField(max_length=100)

    contest_date = models.DateTimeField()
    contest_image = models.TextField(blank=True, null=True)
    contest_text = models.TextField()

    def contest_files(self):
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

