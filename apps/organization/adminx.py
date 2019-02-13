#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!@Author : gaogao
#!@File : .py

import xadmin

from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_disply = ['name', 'desc', 'add_time']
    search_field = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_disply = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']
    search_field = ['name', 'desc', 'click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums','fav_nums','image','address','city','add_time']


class TeacherAdmin(object):
    list_disply = ['name', 'org', 'work_years','work_company','work_position','points','click_nums','fav_nums','add_time']
    search_field = ['name', 'org', 'work_years','work_company','work_position','points','click_nums','fav_nums']
    list_filter = ['name', 'org', 'work_years','work_company','work_position','points','click_nums','fav_nums','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)