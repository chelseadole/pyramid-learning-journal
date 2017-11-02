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


# Expense Tracker is below.

# from pyramid.view import view_config
# from datetime import datetime
# from pyramid.httpexceptions import HTTPNotFound


# FMT = '%m/%d/%Y'
# EXPENSES = [
#     {'id': 1, 'title': 'Rent', 'amount': 50000, 'due_date': datetime.strptime('11/1/2017', FMT)},
#     {'id': 2, 'title': 'Phone Bill', 'amount': 100, 'due_date': datetime.strptime('11/27/2017', FMT)},
#     {'id': 3, 'title': 'Food', 'amount': 600, 'due_date': datetime.strptime('11/2/2017', FMT)},
#     {'id': 4, 'title': 'Car', 'amount': 270, 'due_date': datetime.strptime('11/25/2017', FMT)},
#     {'id': 5, 'title': 'Internet', 'amount': 100, 'due_date': datetime.strptime('11/12/2017', FMT)},
# ]


# @view_config(route_name='home', renderer="expense_tracker:templates/index.jinja2")
# def list_expenses(request):
#     return {
#         "title": "Expense List",
#         "expenses": EXPENSES
#     }


# @view_config(route_name='detail', renderer="expense_tracker:templates/detail.jinja2")
# def expense_detail(request):
#     expense_id = int(request.matchdict['id'])
#     if expense_id < 0 or expense_id > len(EXPENSES) - 1:
#         raise HTTPNotFound
#     expense = list(filter(lambda expense: expense['id'] == expense_id, EXPENSES))[0]
#     return {
#         'title': 'One Expense',
#         'expense': expense
#     }


# @view_config(route_name="api_detail", renderer="json")
# def api_detail(request):
#     expense_id = int(request.matchdict['id'])
#     if expense_id < 0 or expense_id > len(EXPENSES) - 1:
#         raise HTTPNotFound
#     expense = list(filter(lambda expense: expense['id'] == expense_id, EXPENSES))[0]
#     expense['due_date'] = expense['due_date'].strftime(FMT)
#     return {
#         'title': 'One Expense',
#         'expense': expense
#     }
