from django.db import models

# Create your models here.

class Comment(models.Model):
	# <form action="" method="post">
	#   <input type="text" name="username" />
	#   <input type="password" name="password" />
	#   <input type="submit" value="login" />
	# </form
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]