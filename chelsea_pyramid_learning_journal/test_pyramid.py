"""Test files for Pyramid Learning Journal."""

import pytest
from pyramid import testing
from chelsea_pyramid_learning_journal.models.mymodel import Journal
from chelsea_pyramid_learning_journal.models.meta import Base
from pyramid.httpexceptions import HTTPNotFound, HTTPFound


@pytest.fixture(scope='function')
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/test_journal'
    })
    config.include("chelsea_pyramid_learning_journal.models")
    config.include("chelsea_pyramid_learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture(scope='function')
def db_session(configuration, request):
    """Create a session for interacting with the test database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope='function')
def dummy_request(db_session):
    """Instantiate a fake HTTP Request with a database session."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_dictionary(dummy_request):
    """Test that list_view returns a dict from DB."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_create_view_has_title(dummy_request):
    """Test that response to list_view has image."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert response['title'] == 'Create New Entry'


def test_journal_is_added_to_db(db_session):
    """Journal can be added to DB."""
    first_len = len(db_session.query(Journal).all())
    ex_journal = Journal(
        title='Harry Potter and the Chamber of Secrets',
        creation_date='11/13/2017',
        body='Today I fought a snake',
        author='Chelsea Dole'
    )
    db_session.add(ex_journal)
    assert len(db_session.query(Journal).all()) == first_len + 1


def test_created_journal_in_db_is_a_dict(dummy_request):
    """Test that newly added Journal is a dictionary."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    new_journal = Journal(
        author='Chelsea Dole',
        creation_date='11/03/2017',
        title='yoYOyo',
        body='Harry Potter and the Prisoner of Azkaban'
    )
    dummy_request.dbsession.add(new_journal)
    dummy_request.dbsession.commit()
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_detail_view_non_existent_journal(dummy_request):
    """View detail with HTTPNotFound response."""
    from chelsea_pyramid_learning_journal.views.default import detail_view
    new_entry = Journal(
        author='Chelsea Dole',
        creation_date='11/02/2017',
        title='Day 400',
        body='Harry Potter and the Chamber of Secrets'
    )
    dummy_request.dbsession.add(new_entry)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 2000
    with pytest.raises(HTTPNotFound):
        detail_view(dummy_request)


def test_create_view_still_works(dummy_request):
    """Test that create_view still works despite changes to other fns."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    new_entry = Journal(
        author='Chelsea Dole',
        creation_date='11/30/2017',
        title='Hogwarts Year 5',
        body='Harry Potter and the Order of the Phoenix',
    )
    dummy_request.dbsession.add(new_entry)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 5
    response = create_view(dummy_request)
    assert response['title'] == 'Create New Entry'


def test_create_get_request_returns_correct_page(dummy_request):
    """POST requests without data should return an empty dictionary."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    dummy_request.method = "GET"
    response = create_view(dummy_request)
    assert response['title'] == 'Create New Entry'


def test_list_view_return_journal_instance_with_incomplete_info(dummy_request):
    """Update view response has file content."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    new_journal = Journal(
        title='this is an incomplete entry',
    )
    dummy_request.dbsession.add(new_journal)
    request = dummy_request
    response = list_view(request)
    assert 'creation_date' not in response


def test_list_view_http_not_found(dummy_request):
    """Test HTTPNotFound response when there are no posts."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    with pytest.raises(HTTPNotFound):
        assert list_view(None)


def test_update_view_still_works(dummy_request):
    """Test that update_view still works despite changes to other fns."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    updated_entry = {
        'author': 'Chelsea Dole',
        'creation_date': '11/30/2017',
        'title': 'Hogwarts Year 5',
        'body': 'Harry Potter and the Order of the Phoenix'
    }
    dummy_request.method == "POST"
    dummy_request.POST = updated_entry
    dummy_request.matchdict['id'] = 5
    response = update_view(dummy_request)
    assert response['title'] == 'Edit Entry'


def test_create_view_adds_entry_on_post_request(dummy_request):
    """Test adding entry via create_view."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    entry_ex = {
        'author': 'Chelsea Dole',
        'creation_date': '2017-11-07',
        'title': 'Example',
        'body': 'a hot bod'
    }
    dummy_request.method = "POST"
    dummy_request.POST = entry_ex
    create_view(dummy_request)
    query = dummy_request.dbsession.query(Journal)
    assert query.get(1).title == 'Example'


def tests_request_method_is_httpfound(dummy_request):
    """."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    dummy_request.method = "POST"
    dummy_request.POST = {
        'title': 'New Entry',
        'body': 'Some additional text',
        'author': 'Chelsea Dole',
        'creation_date': '2017-11-07'
    }
    response = create_view(dummy_request)
    assert isinstance(response, HTTPFound)


def test_update_view_updates_entry_via_website(dummy_request):
    """."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    new_info = {'title': 'New Title',
                'body': 'New Body',
                'author': 'Chelsea Dolewhip',
                'creation_date': '2017-11-07'
                }
    dummy_request.matchdict['id'] = 1
    dummy_request.method = "POST"
    dummy_request.POST = new_info
    update_view(dummy_request)
    entry = dummy_request.dbsession.query(Journal).get(1)
    assert entry.title == 'New Title' and entry.body == 'New Body'


def test_update_view_sends_http_found(dummy_request):
    """Test that update view redirects user."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    updated_info = {'title': "UPDATED",
                    'author': 'cdawg',
                    'body': 'bodyboi',
                    'creation_date': '2017-11/07'
                    }
    dummy_request.method = "POST"
    dummy_request.matchdict['id'] = 1
    dummy_request.POST = updated_info
    response = update_view(dummy_request)
    assert isinstance(response, HTTPFound)


def test_update_view_replaces_existing_journal(dummy_request):
    """Confirm that update view replaces content of original journal."""
    from chelsea_pyramid_learning_journal.views.default import update_view, detail_view
    original_journal = {
        'title': 'Hermione Granger',
        'creation_date': '01/23/45',
        'body': 'ORIGINAL ENTRY'
    }
    dummy_request.matchdict['id'] = 2
    dummy_request.POST = original_journal
    response = update_view(dummy_request)
    assert response['ljpost']['body'] == 'ORIGINAL ENTRY'
    replacement = {
        "title": "Remus Lupin",
        "creation_date": "00/00/4200",
        "body": "Harry Potter and the Prisoner of Azkaban"
    }
    dummy_request.matchdict['id'] = 2
    dummy_request.POST = replacement
    response = update_view(dummy_request)
    assert response['ljpost']['body'] == 'Harry Potter and the Prisoner of Azkaban'


def test_make_sure_update_updates_and_doesnt_just_add_new_journal(dummy_request):
    """Make sure that DB length doesnt change when updating."""
    from chelsea_pyramid_learning_journal.views.default import update_view
    original_len = len(dummy_request.dbsession.query(Journal).all())
    original_journal = Journal(
        title='Sirius Black',
        creation_date='11/11/1111',
        body='I did my time. 12 years of it! In AZKABAN'
    )
    dummy_request.dbsession.add(original_journal)
    dummy_request.matchdict['id'] = 1
    assert len(dummy_request.dbsession.query(Journal).all()) == original_len + 1
    dummy_request.method = 'POST'
    update_entry = {
        "title": 'Remus Lupin',
        "creation_date": '99/99/99',
        "body": 'Awoooooo'
    }
    dummy_request.POST = update_entry
    update_view(dummy_request)
    assert len(dummy_request.dbsession.query(Journal).all()) == original_len + 1
