import random
import PIL
from PIL.ImageDraw import ImageDraw
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
import time
from django.views.generic import ListView
from layver.core.DriverManager import DriverManager
from layver.models import Page


def main_page(request):
    return render(request, 'layver/main_page.html')


def screens_view(request):
    page = Page(link=request.POST['link'])
    page.save()
    #page.make_screenshoots()
    return HttpResponseRedirect(reverse('results', args=(page.id,)))


class ResultView(generic.DetailView):
    model = Page
    template_name = 'layver/result_view.html'


def make_screenshots(request, id):
    page = Page.objects.get(pk=id)
    print(page.screen_set.all())
    if len(page.screen_set.all()) != 0:
        return HttpResponse()
    else:
        print("making screnshoots....")
        page.make_screenshoots()
        DriverManager.close_browsers()
        return HttpResponse()

#-------------------------------------------------------


def layer_page(request):
    return render(request, 'layver/layer_page.html')


def layer_view(request):
    browsers = request.POST.getlist('browsers[]')
    print(browsers)
    page = Page(link=request.POST['link'], browser1=browsers[0], browser2=browsers[1])
    page.save()

    return HttpResponseRedirect(reverse('errors', args=(page.id,)))


class ErrorsView(generic.DetailView):
    model = Page
    template_name = 'layver/errors_view.html'


def tag_errors(request, id):
    page = Page.objects.get(pk=id)
    print("making screenshots...")
    names = page.make_screenshoots()
    print("tagging errors...")
    page.mark_errors([page.browser1, page.browser2], 12, names)
    DriverManager.close_browsers()
    return HttpResponse()

#-------------------------------------------------------------------


class PageListView(ListView):
    model = Page
    template_name = 'layver/page_list_view.html'
