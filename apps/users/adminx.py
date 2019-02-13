#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!@Author : gaogao
#!@File : .py

import xadmin

from xadmin import views

from .models import EmailVerifyRecord,Banner

class BaseSetting(object):
    enable_thems = True
    user_bootswatch = True


class GlobalSettings(object):
    site_title = "学习在线后台管理系统"
    site_footer = "学习在线网"
    #实现导航栏折叠功能
    menu_style = "accordion"


#注册邮箱功能
class EmailVerfyRecordAdmin(object):
    #后台实现增、删、改、查功能
    list_disply = ['code','email','send_type','send_time']
    search_field = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']

class BannerAdmin(object):
    list_disply = ['title', 'image', 'url', 'index','add_time']
    search_field = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']

# models模块实现关联注册
xadmin.site.register(EmailVerifyRecord,EmailVerfyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)