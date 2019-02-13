#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!@Author : gaogao
#!@File : .py

import xadmin

from .models import Course,Lesson,Video,CourseResource
CourseResource
class CourseAdmin(object):
    list_disply = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_field = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']

class LessonAdmin(object):
    list_disply = ['course','name','add_time']
    search_field = ['course','name']
    list_filter = ['course__name','name','add_time']


class VideoAdmin(object):
    list_disply = ['lesson', 'name', 'add_time']
    search_field = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_disply = ['course', 'name', 'download','add_time']
    search_field = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download','add_time']



xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)