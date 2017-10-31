"""Create callables for calling routes."""
import io  # for backwards compatability
import os

from pyramid.response import Response

HERE = os.path.dirname(__file__)


def home_page(request):
    """Parse file path and pass it to response to serve home page."""
    imported_text = io.open(os.path.join(HERE,
                                         '../templates/homepage.html')).read()
    return Response(imported_text)


def list_view():  # list of journal entries
    """Parse file path and pass it to response to serve home page."""
    imported_text =\
        io.open(os.path.join(HERE, '../templates/homepage.html')).read()
    return Response(imported_text)


def detail_view():  # view single entry
    """Parse file path and pass it to response to serve detail post page."""
    imported_text =\
        io.open(os.path.join(HERE, '../templates/detail-entry.html')).read()
    return Response(imported_text)


def create_view():  # create new entry
    """Parse file path and pass it to response to serve new post page."""
    imported_text =\
        io.open(os.path.join(HERE, '../templates/new-entry.html')).read()
    return Response(imported_text)


def update_view():  # edit existing entry
    """Parse file path and pass it to response to serve edit post page."""
    imported_text =\
        io.open(os.path.join(HERE, '../templates/edit-entry.html')).read()
    return Response(imported_text)
