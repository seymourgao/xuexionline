#*coding=utf-8

from datetime import datetime


from django.db import models


# Create your models here.

from users.models import UserProfile
from courses.models import Course

class UserAsk(models.Model):
    #"用户咨询"
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    #"课程评论"
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    #"用户收藏"
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    # ID是课程的ID或者是讲师、课程机构的ID
    fav_id = models.IntegerField(default=0, verbose_name="收藏数据 Id")
    fav_type = models.IntegerField(choices=( (1, "课程"), (2, "课程机构"), (3, "讲师") ), default=1, verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    # 初始化判断是否收藏
    # has_fav = False
    # if request.user.is_authenticated():
    #     if UserProfile.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
    #         has_fav = True


class UserMessage(models.Model):
    # 如果 为 0 代表全局消息，否则就是用户的 ID
    user = models.IntegerField(default=0, verbose_name="接受用户")
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


# CourseComments 和 UserCourse 字段差不多，可以使用 UserCourse 继承 CourseComments
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户学习过的课程"
        verbose_name_plural = verbose_name