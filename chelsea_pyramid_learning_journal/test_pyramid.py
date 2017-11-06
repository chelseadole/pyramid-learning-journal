"""Test files for Pyramid Learning Journal."""

import pytest
from pyramid import testing
from chelsea_pyramid_learning_journal.models.mymodel import Journal
from chelsea_pyramid_learning_journal.models.meta import Base
from pyramid.httpexceptions import HTTPNotFound


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='session')
def dummy_request(db_session):
    """Instantiate a fake HTTP Request with a database session."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_dictionary(dummy_request):
    """Test that list_view returns a dict from DB."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_response_has_image(dummy_request):
    """Test that response to list_view has image."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert response['title'] == 'Create New Entry'


def test_journal_is_added_to_db(db_session):
    """Journal can be added to DB."""
    assert len(db_session.query(Journal).all()) == 0
    ex_journal = Journal(
        title='Harry Potter and the Chamber of Secrets',
        creation_date='11/13/2017',
        body='Today I fought a snake',
        author='Chelsea Dole'
    )
    db_session.add(ex_journal)
    assert len(db_session.query(Journal).all()) == 1


def test_created_journal_in_db_is_a_dict(dummy_request):
    """Test that newly added Journal is a dictionary."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    new_journal = Journal(
        author='Chelsea Dole',
        creation_date='11/03/2017',
        title='Day 15',
        body='Harry Potter and the Prisoner of Azkaban.'
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
