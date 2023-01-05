from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True, null=False, db_index=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now=True, null=False)


class Post(models.Model):
    id = models.IntegerField(primary_key=True, null=False, db_index=True)
    title = models.CharField(null=False, max_length=100)
    content = models.CharField(null=False, max_length=300)
    published = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now=True, null=False)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Vote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, unique=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, unique=True)

    class Meta:
        unique_together = (('user_id', 'post_id'),)


class Comment(models.Model):
    id = models.IntegerField(primary_key=True, null=False, db_index=True)
    content = models.CharField(null=False, max_length=300)
    created_at = models.DateTimeField(auto_now=True, null=False)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    main_post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
