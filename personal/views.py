from django.shortcuts import render,redirect
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.views import get_blog_queryset
from blog.models import BlogPost
from personal.models import Event
from account.models import Account

BLOG_POSTS_PER_PAGE = 10

def home_screen_view(request, *args, **kwargs):
	
	context = {}
	

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

#	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	


	# Pagination
	page = request.GET.get('page', 1)
#	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
#	try:
	#	blog_posts = blog_posts_paginator.page(page)
#	except PageNotAnInteger:
#		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
#	except EmptyPage:
#		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

#	context['blog_posts'] = blog_posts
#	events=Event.objects.all()
	
#	sorted_events = sorted(events, key=lambda x: x.time, reverse=True)
#	context['events']=sorted_events
	return render(request, "personal/home.html", context)



def all_posts_view(request, *args, **kwargs):
	
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	


	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts
	
	return render(request, "personal/all_blogs.html", context )


def all_events(requset):
	context = {}
	events=Event.objects.all()
	sorted_events = sorted(events, key=lambda x: x.time, reverse=True)
	context['events']=sorted_events
	return render(requset, "personal/all_events.html", context)


from itertools import chain
from operator import attrgetter

def community_view(request):
    context = {}
    blog_posts = get_blog_queryset("")
    events = Event.objects.all()
    
    user = request.user
    
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    all_items = sorted(chain(blog_posts, events), key=attrgetter('date_updated'), reverse=True)
    context['all_items'] = all_items
    return render(request, "personal/community.html", context)


def team_view(requset):
	context = {}
	accounts=Account.objects.all()
	context['accounts']=accounts
	
	return render(requset,"personal/team.html",context)


def about_us(requset):
	return render (requset,"personal/about.html")








