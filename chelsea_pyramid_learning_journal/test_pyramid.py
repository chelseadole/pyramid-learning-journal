"""Test files for Pyramid Learning Journal."""

from __future__ import unicode_literals
from pyramid import testing
from pyramid.httpexceptions import HTTPNotFound
import pytest


@pytest.fixture
def dummy_request():
    """Create dummy request fixture."""
    return testing.DummyRequest()


def test_list_view_response_title(dummy_request):
    """Test list view response of title."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response['title'] == 'Chelsea LJ'


def test_list_view_response_is_a_dictionary(dummy_request):
    """Test that response to list_view is a dictionary."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_response_has_good_img(dummy_request):
    """Test that response to list_view has the right image."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response['image'] == 'home-bg.jpg'


def test_list_view_response_has_a_post(dummy_request):
    """Test that response to list_view has the right image."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    from chelsea_pyramid_learning_journal.data.LJ_entries import POST
    response = list_view(dummy_request)
    assert response['ljposts'] == POST


def test_detail_view_has_correct_keys(dummy_request):
    """Test that response to detail_view has the correct keys."""
    from chelsea_pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert 'image' in response
    assert 'ljpost' in response
    assert 'image' in response


def test_http_not_found(dummy_request):
    """Test that response to detail_view has the correct keys."""
    from chelsea_pyramid_learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 50
    with pytest.raises(HTTPNotFound):
        assert detail_view(dummy_request)


def test_new_entry_has_correct_response(dummy_request):
    """Test that response to create_view_has_correct routing."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    dummy_request.matchdict['id'] = 4
    response = create_view(dummy_request)
    assert response['title'] == 'Create New Entry'


def test_new_entry_works_with_a_specific_entry(dummy_request):
    """Test that response to create_view has the correct value."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    dummy_request.matchdict['id'] = 7
    response = create_view(dummy_request)
    assert response['image'] == 'new-entry.jpg'


def test_update_entry_works_for_response_title(dummy_request):
    """Test that response to update_view has the correct title."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 10
    response = update_view(dummy_request)
    assert response['title'] == 'Edit Entry'


def test_update_entry_post_content_loads_correctly(dummy_request):
    """Test that response to update_view has the correct post."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 12
    response = update_view(dummy_request)
    assert "10/31/2017" in response['ljpost']['creation_date']


def test_update_entry_raises_http_error(dummy_request):
    """Test that response to update_view raises httperror."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 5000
    with pytest.raises(HTTPNotFound):
        assert update_view(dummy_request)


def test_update_entry_error_type(dummy_request):
    """Test that httperror is 404."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 2345
    with pytest.raises(HTTPNotFound):
        request = update_view(dummy_request)
        request.response.status = 404
