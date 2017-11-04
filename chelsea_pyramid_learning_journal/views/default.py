"""Create callables for calling routes."""
from pyramid.view import view_config
from chelsea_pyramid_learning_journal.models import Journal
from pyramid.httpexceptions import HTTPNotFound


@view_config(route_name='list_view',
             renderer='chelsea_pyramid_learning_journal:templates/homepage.jinja2')
def list_view(request):
    """Parse file path and pass it to response to serve home page."""
    posts = request.dbsession.query(Journal).all()
    return {'ljposts': posts,
            'title': 'Chelsea LJ',
            'image': "home-bg.jpg"}


@view_config(route_name='detail_view',
             renderer='chelsea_pyramid_learning_journal:templates/detail-entry.jinja2')
def detail_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    posts = request.dbsession.query(Journal).get(post_id)
    for post in posts:
        if post['id'] == post_id:
            return {'ljpost': post,
                    'title': post['title'],
                    'image': 'post-bg.jpg'}

    raise HTTPNotFound


@view_config(route_name='create_view',
             renderer='chelsea_pyramid_learning_journal:templates/new-entry.jinja2')
def create_view(request):
    """Parse file path and pass it to response to serve home page."""
    return {'title': 'Create New Entry',
            'image': 'new-entry.jpg'}


@view_config(route_name='update_view',
             renderer='chelsea_pyramid_learning_journal:templates/edit-entry.jinja2')
def update_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    for post in POST:
        if post['id'] == post_id:
            return {'ljpost': post,
                    'image': 'post-bg.jpg',
                    'title': 'Edit Entry'}

    raise HTTPNotFound
