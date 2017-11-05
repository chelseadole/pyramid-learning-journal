"""Create callables for calling routes."""
from pyramid.view import view_config
from chelsea_pyramid_learning_journal.models import Journal
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest, HTTPFound
from chelsea_pyramid_learning_journal.data.LJ_entries import POST
from datetime import datetime


@view_config(route_name='list_view',
             renderer='chelsea_pyramid_learning_journal:templates/homepage.jinja2')
def list_view(request):
    """Show homepage with all listed posts."""
    posts = request.dbsession.query(Journal).all()
    if posts is None:
        raise HTTPNotFound
    return {'ljposts': posts,
            'title': 'Chelsea LJ',
            'image': "home-bg.jpg"}


@view_config(route_name='detail_view',
             renderer='chelsea_pyramid_learning_journal:templates/detail-entry.jinja2')
def detail_view(request):
    """Show detailed post page, and give option to update post contents."""
    post_id = int(request.matchdict['id'])
    post = request.dbsession.query(Journal).get(post_id)
    if post is None:
        raise HTTPNotFound
    return {'ljpost': post,
            'title': post.title,
            'image': 'post-bg.jpg'}


@view_config(route_name='create_view',
             renderer='chelsea_pyramid_learning_journal:templates/new-entry.jinja2')
def create_view(request):
    """Show create post page, and process POST request to add new journal to DB."""
    if request.method == 'GET':
        return {'title': 'Create New Entry',
                'image': 'new-entry.jpg'}
    if request.method == 'POST':
        now = str(datetime.now())[:10]
        if not request.POST.body or not request.POST.title:
            raise HTTPBadRequest
        new_entry = Journal(
            title=request.POST['title'],
            body=request.POST['body'],
            due_date=now,
            author='Chelsea Dole'
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('list_view'))


@view_config(route_name='update_view',
             renderer='chelsea_pyramid_learning_journal:templates/edit-entry.jinja2')
def update_view(request):
    """Show update post page, and process POST request to update database."""
    post_id = int(request.matchdict['id'])
    target_journal = request.dbsession.query(Journal).get(post_id)
    if not target_journal:
        raise HTTPFound
    if request.method == "GET":
        return {'ljpost': target_journal,
                'image': 'post-bg.jpg',
                'title': 'Edit Entry'}
    if request.method == "POST":
        target_journal.body = request.POST['body']
        target_journal.title = request.POST['title']
        request.dbsession.add(target_journal)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail_view', id=target_journal.id)
