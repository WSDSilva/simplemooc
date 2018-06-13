from django.db import models


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Informações detalhada', blank=True, null=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now_add=True)

    objects = CourseManager()

    @models.permalink
    def get_absolute_url(self):
        return ('courses:detail', (), {'slug':self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'



