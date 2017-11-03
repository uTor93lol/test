from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return "Проект %s %s" % (self.name, self.description,)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectImg(models.Model):
    key = models.ForeignKey(Projects)
    img = models.ImageField(upload_to='project_img/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Картинка %s %s" % (self.key, self.img,)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'