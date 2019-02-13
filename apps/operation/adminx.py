#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!@Author : gaogao
#!@File : .py

import xadmin

from .models import CourseComments,UserMessage,UserAsk,UserCourse,UserFavorite


class CourseCommentsAdmin(object):
    list_disply = ['user','course','comment','add_time']
    search_field = ['user','course','comment']
    list_filter = ['user','course','comment','add_time']


class UserMessageAdmin(object):
    list_disply = ['user','message','has_read','add_time']
    search_field = ['user','message','has_read']
    list_filter = ['user','message','has_read','add_time']


class UserAskAdmin(object):
    list_disply = ['name', 'mobile','course_name','add_time']
    search_field = ['name', 'mobile','course_name']
    list_filter = ['name', 'mobile','course_name','add_time']


class UserCourseAdmin(object):
    list_disply = ['user', 'course','add_time']
    search_field = ['user', 'course']
    list_filter = ['user', 'course','add_time']


class UserFavoriteAdmin(object):
    list_disply = ['user','fav_id','fav_type','add_time']
    search_field = ['user','fav_id','fav_type']
    list_filter = ['user','fav_id','fav_type','add_time']


xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)