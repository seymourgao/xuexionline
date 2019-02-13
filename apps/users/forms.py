#*coding:utf-8
#!@Author : gaogao
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=8)  #在连接数据库之前限制密码长度

