"""Test files for Pyramid Learning Journal."""

import pytest
from chelsea_pyramid_learning_journal.models.mymodel import Journal
from pyramid.httpexceptions import HTTPNotFound, HTTPFound


def test_list_view_returns_dictionary(dummy_request):
    """Test that list_view returns a dict from DB."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_detail_view_dict_contents_correct(dummy_request, db_session):
    """Test that list_view dict contents are accurate."""
    from chelsea_pyramid_learning_journal.views.default import detail_view
    ex_journal = Journal(
        title='Harry Potter and the Chamber of Secrets',
        creation_date='11/13/2017',
        body='Today I fought a snake',
        author='Chelsea Dole'
    )
    db_session.add(ex_journal)
    db_session.commit()
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert response['image'] == 'post-bg.jpg'


def test_detail_view_with_incorrect_request_type(dummy_request):
    """Test that d_v returns empty dict with PUT request."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    dummy_request.method = "POST"
    dummy_request.POST = None
    assert create_view(dummy_request) == {}


def tests_home_route_is_200_ok(dummy_request):
    """Check home route."""
    from chelsea_pyramid_learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response['image'] == 'home-bg.jpg'


def test_login_incorrect_password(dummy_request):
    """Attempt login with incorrect password."""
    from chelsea_pyramid_learning_journal.views.default import login
    login_info = {
        "username": "chelseadole",
        "password": "wrongpassword"
    }
    dummy_request.method = "POST"
    dummy_request.POST = login_info
    response = login(dummy_request)
    assert isinstance(response, dict)
    assert response['error'] == 'Username/password combination invalid.'


def test_login_incorrect_username(dummy_request):
    """Attempt login with incorrect username."""
    from chelsea_pyramid_learning_journal.views.default import login
    login_info = {
        "username": "wrongusername",
        "password": "potato"
    }
    dummy_request.method = "POST"
    dummy_request.POST = login_info
    response = login(dummy_request)
    assert isinstance(response, dict)
    assert response['error'] == 'Username/password combination invalid.'


def test_login_with_correct_combo(dummy_request):
    """Attempt login with correct pass/user combo."""
    from chelsea_pyramid_learning_journal.views.default import login
    login_info = {
        "username": "chelseadole",
        "password": "potato"
    }
    dummy_request.method = "POST"
    dummy_request.POST = login_info
    response = login(dummy_request)
    assert isinstance(response, HTTPFound)


def test_csrf_token_exists(testapp):
    """."""
    login_info = {
        "username": "chelseadole",
        "password": "potato"
    }
    testapp.post('/login', login_info)
    response = testapp.get('/journal/new-entry')
    token = response.html.find('input', {'type': 'hidden'}).attrs['value']
    new_post = {
        'csrf_token': token,
        'author': 'Chelsea',
        'creation_date': '11/11/1111',
        'title': 'MYTITLE',
        'body': 'MYBODY'
    }
    testapp.post('/journal/new-entry', new_post)
    assert new_post['title'] in testapp.get('/').ubody
    testapp.get('/logout')


def test_delete_journal(dummy_request, db_session):
    """Test that delete journal removes item from DB."""
    from chelsea_pyramid_learning_journal.views.default import delete_view, create_view
    to_delete = {
        'author': 'Chelsea Dole',
        'creation_date': '2017-11-07',
        'title': 'Example',
        'body': 'a hot bod'
    }
    dummy_request.method = "POST"
    dummy_request.matchdict['id'] = 2
    dummy_request.POST = to_delete
    create_view(dummy_request)
    query = db_session.query(Journal)
    length = len(query.all())
    assert len(query.all()) == length
    query = db_session.query(Journal)
    delete_view(dummy_request)
    assert len(query.all()) == length - 1


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
    db_session.commit()
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
    dummy_request.dbsession.commit()
    request = dummy_request
    response = list_view(request)
    assert 'creation_date' not in response


def test_update_view_writes_over_previous_entry(dummy_request):
    """Test that update_view still works despite changes to other fns."""
    from chelsea_pyramid_learning_journal.views.default import update_view, create_view
    original_entry = {
        'author': 'Chelsea Dole',
        'creation_date': '11/30/2017',
        'title': 'Hogwarts Year 5',
        'body': 'Harry Potter and the Order of the Phoenix'
    }
    dummy_request.method = "POST"
    dummy_request.POST = original_entry
    dummy_request.matchdict['id'] = 1
    response = create_view(dummy_request)
    assert response.code == 302
    updated_entry = {
        'author': 'Chelsea Dole',
        'creation_date': '11/30/2017',
        'title': 'UPDATED TITLE',
        'body': 'Harry Potter and the Order of the Phoenix'
    }
    dummy_request.POST = updated_entry
    dummy_request.matchdict['id'] = 1
    response = update_view(dummy_request)
    assert isinstance(response, HTTPFound)


def test_create_view_adds_entry_on_post_request(dummy_request, db_session):
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
    query = db_session.query(Journal)
    assert query.get(1).title == 'Example'


def tests_create_view_is_instance_of_httpfound(dummy_request):
    """Create view returns HTTPFound."""
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


def test_update_view_replaces_title_and_body(dummy_request):
    """Replace title and entry with new body in via update_view."""
    from chelsea_pyramid_learning_journal.views.default import update_view, create_view
    new_info = {'title': 'Old Title',
                'body': 'Old Body',
                'author': 'Chelsea',
                'creation_date': '2017-11-07'
                }
    dummy_request.method = "POST"
    dummy_request.POST = new_info
    create_view(dummy_request)
    dummy_request.POST = {
        'title': 'Updated Title',
        'body': 'New Body',
        'author': 'Chelsea Dolewhip',
        'creation_date': '2017-11-07'
    }
    dummy_request.matchdict['id'] = 1
    update_view(dummy_request)
    entry = dummy_request.dbsession.query(Journal).get(1)
    assert entry.title == 'Updated Title' and entry.body == 'New Body'


def test_create_view_makes_a_new_journal(dummy_request):
    """Send a post request to my view with data to make a new expense."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    journal_info = {
        "title": "mytitle",
        "body": "mybody",
        "creation_date": "11/11/1111",
        "author": "me"
    }
    dummy_request.method = "POST"
    dummy_request.POST = journal_info
    create_view(dummy_request)
    expense = dummy_request.dbsession.query(Journal).first()
    assert expense.title == "mytitle"


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


def test_logged_out_user_has_no_access_to_create(dummy_request, testapp):
    """Test that unauthenticated user returns 403 error on detail_view."""
    assert testapp.get("/journal/1/edit-entry", status=403)


def test_create_view_has_title(dummy_request, testapp):
    """Test that response to list_view has image."""
    from chelsea_pyramid_learning_journal.views.default import create_view
    testapp.post('/login', {'username': 'chelseadole', 'password': 'potato'})
    response = testapp.get('/journal/new-entry')
    token = response.html.find_all('input', {'name': 'crsf_token'})  # is this right?
    response = create_view(dummy_request)
    assert response['title'] == 'Create New Entry'
