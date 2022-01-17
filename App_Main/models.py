from django.db import models


class CategoryParent(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        abstract = True


def upload_project(instance, filename):
    return "Projects/{instance.project_name}/{instance.project_name}.png".format(
        instance=instance
    )


# Create your models here.
class ProjectCategory(CategoryParent):
    class Meta:
        verbose_name_plural = "Project Category"
        db_table = "Project Category"


class ProjectAdmin(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


def upload_project(instance, filename):
    return "Projects/{instance.name}/{instance.name}.png".format(instance=instance)


class Projects(ProjectAdmin):
    image = models.ImageField(upload_to=upload_project, blank=True, null=True)
    category = models.ManyToManyField(ProjectCategory, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"
        db_table = "Projects"


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=254)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name + " Just Messaged You."

    class Meta:
        verbose_name_plural = "Contact"
        db_table = "Contact"


class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "NewsLetter"
        db_table = "NewsLetter"
