from django.db import models

class BookType(models.TextChoices):
    STANDARD = 'standard'
    BADIY = 'badiy'
    ILMIY = 'ilmiy'


class Author(models.Model):
    first_name = models.CharField(max_length=20,null=True,blank=True)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        db_table = "authors"
        ordering = ["-birth_date"]



class Books(models.Model):
      title = models.CharField(max_length=255)
      description = models.TextField()
      price = models.DecimalField(max_digits=10,decimal_places=2)
      type = models.CharField(max_length=20,choices=BookType.choices , default=BookType.STANDARD)
      created_time = models.DateTimeField(auto_now_add=True)
      updated_time = models.DateTimeField(auto_now=True)
      authors = models.ManyToManyField(Author,related_name='books')


      def __str__(self):
          return f"{self.title}"


      class Meta:
          db_table = 'books'
          ordering = ['-created_time']


