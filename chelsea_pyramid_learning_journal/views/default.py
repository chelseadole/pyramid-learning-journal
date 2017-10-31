"""Create callables for calling routes."""
import io  # for backwards compatability
import os

from pyramid.response import Response
from pyramid.view import view_config

HERE = os.path.dirname(__file__)


def list_view(request):
    """Parse file path and pass it to response to serve home page."""
    path = os.path.join(HERE, '../templates/homepage.html')
    with io.open(path) as file:
        return Response(file.read())


def detail_view(request):
    """Parse file path and pass it to response to serve home page."""
    path = os.path.join(HERE, '../templates/detail-entry.html')
    with io.open(path) as file:
        return Response(file.read())


def create_view(request):
    """Parse file path and pass it to response to serve home page."""
    path = os.path.join(HERE, '../templates/create-entry.html')
    with io.open(path) as file:
        return Response(file.read())


def update_view(request):
    """Parse file path and pass it to response to serve home page."""
    path = os.path.join(HERE, '../templates/update-entry.html')
    with io.open(path) as file:
        return Response(file.read())
