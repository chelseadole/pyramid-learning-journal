"""Test files for Pyramid Learning Journal."""

from __future__ import unicode_literals
from pyramid import testing
import pytest


@pytest.fixture
def dummy_request():
    """Create dummy request fixture."""
    return testing.DummyRequest()


def test_list_view_response_status_200_ok(dummy_request):
    """Test list view."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_list_view_response_is_html(dummy_request):
    """Test html contents in list view."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response.content_type == 'text/html'


def test_list_view_response_body_includes_our_page(dummy_request):
    """Test html contents in list view are the correct ones."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    the_tag = '<h1>Pyramid Learning Journal</h1>'
    assert the_tag in response.ubody


def test_detail_view_response_body_includes_our_page(dummy_request):
    """Test html contents in list view are the correct ones."""
    from chelsea_pyramid_learning_journal.views.default import detail_view
    response = detail_view(dummy_request)
    the_tag = '<h1>CF 401, Day 01</h1>'
    assert the_tag in response.ubody


def test_create_view_response_body_includes_our_page(dummy_request):
    """Test html contents in list view are the correct ones."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    response = create_view(dummy_request)
    the_tag = '<h2>New Entry</h2>'
    assert the_tag in response.ubody


def test_update_view_response_body_includes_our_page(dummy_request):
    """Test html contents in list view are the correct ones."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    response = update_view(dummy_request)
    the_tag = '<p>Title:</p>'
    assert the_tag in response.ubody


def test_detail_view_response_status_200_ok(dummy_request):
    """Test detail view response status."""
    from chelsea_pyramid_learning_journal.views.default import detail_view
    response = detail_view(dummy_request)
    assert response.status_code == 200


def test_create_view_response_status_200_ok(dummy_request):
    """Test list view."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert response.status_code == 200


def test_update_view_response_status_200_ok(dummy_request):
    """Test list view."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    response = update_view(dummy_request)
    assert response.status_code == 200
