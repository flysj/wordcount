#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:44:39 2019

@author: root
"""
from django.http import HttpRequest
from django.shortcuts import render

def home(request):
    return render(request,'home.html')