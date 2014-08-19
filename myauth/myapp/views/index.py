# -*- Coding: utf-8 -*-
from django.shortcuts import render_to_response

# View for index page.
def page(request):
    return render_to_response('jp/index.html')
