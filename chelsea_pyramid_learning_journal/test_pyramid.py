"""Test files for Pyramid Learning Journal."""

from __future__ import unicode_literals
from pyramid import testing
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
    dummy_request.matchdict['id'] = 1
    with pytest.raises(HTTPNotFound):
        assert detail_view(dummy_request)
