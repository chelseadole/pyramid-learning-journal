"""Test configuration."""

import pytest
from pyramid import testing
from chelsea_pyramid_learning_journal.models.mymodel import Journal
from chelsea_pyramid_learning_journal.models.meta import Base


@pytest.fixture
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/test_journal'
    })
    config.include("chelsea_pyramid_learning_journal.models")
    config.include("chelsea_pyramid_learning_journal.routes")
    # config.include("chelsea_pyramid_learning_journal.security")

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


@pytest.fixture(scope="session")
def testapp(request):
    """Fake app for testing."""
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        settings = {
            'sqlalchemy.url': 'postgres://localhost:5432/test_journal'
        }
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('chelsea_pyramid_learning_journal.routes')
        config.include('chelsea_pyramid_learning_journal.models')
        config.include('chelsea_pyramid_learning_journal.security')
        config.scan()
        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)

    return TestApp(app)


@pytest.fixture(scope="session")
def fill_the_db(testapp):
    """Fill test DB."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(JOURNALS)

JOURNALS = []
for i in range(20):
    new_journal = Journal(
        title='journal number {}'.format(i),
        body="this is the body",
        creation_date="11/08/2017"
    )
    JOURNALS.append(new_journal)