"""Create callables for calling routes."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
# from pyramid.response import Response
# import os
# import io

# HERE = os.path.dirname(__file__)

FMT = "%m/%d/%Y"

POST = [
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Chelsea Mother-Effin Dole',
     'body': 'I am the baddest b!tch on the block.', 'id': '1'},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Chelsea Mother-Effin Dole',
     'body': 'I am the baddest b!tch on the block.', 'id': '2'},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Chelsea Mother-Effin Dole',
     'body': 'I am the baddest b!tch on the block.', 'id': '3'},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Chelsea Mother-Effin Dole',
     'body': 'I am the baddest b!tch on the block.', 'id': '4'},
    {'creation_date': datetime.strptime('11/1/2017', FMT),
     'title': 'LJ1', 'author': 'Chelsea Mother-Effin Dole',
     'body': 'I am the baddest b!tch on the block.', 'id': '5'}
]


@view_config(route_name='list_view',
             renderer='chelsea_pyramid_learning_journal:templates/homepage.jinja2')
def list_view(request):
    """Parse file path and pass it to response to serve home page."""
    return {'ljposts': POST}


@view_config(route_name='detail_view',
             renderer='chelsea_pyramid_learning_journal:templates/detail-entry.jinja2')
def detail_view(request):
    """Parse file path and pass it to response to serve home page."""
    post_id = int(request.matchdict['id'])
    if post_id not in POST:
        return HTTPNotFound
    target_post = list(filter(lambda x: x['id'] == post_id, POST))[0]
    return {'ljposts': target_post}


@view_config(route_name='create_view',
             renderer='chelsea_pyramid_learning_journal:templates/new-entry.jinja2')
def create_view(request):
    """Parse file path and pass it to response to serve home page."""
    # does anything go here??
    return


@view_config(route_name='update_view',
             renderer='chelsea_pyramid_learning_journal:templates/templates/edit-entry.jinja2')
def update_view(request):
    """Parse file path and pass it to response to serve home page."""
    # get post ID from detail_view page... import it?
    # do same filter fn from detail_view
    return {
        'ljposts': target_post
    }
