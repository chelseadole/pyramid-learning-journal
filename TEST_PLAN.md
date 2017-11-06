# Pyramid Learning Journal Tests plan/outline
#### Chelsea Dole, 11/05/2017


### Step 3 and 4 Tests

* *test_list_view_returns_dictionary* - Checks that list_view returns a dictionary containing information to send to jinja2 homepage. 

* *test_create_view_has_title* - Checks that create_view's returned dictionary has the correct image key.

* *test_journal_is_added_to_db* - Checks that when a new journal is added to the database, the length of the database goes up by one. (Therefore confirming that it was successfully added.)

* *test_created_journal_in_db_is_a_dict* - Checks that the new Journal class instance is a dictionary.

* *test_detail_view_non_existent_journal* - Checks that when detail_view is sent a request for a non-existance journal entry ID, it returns an HTTPNotFound page.

* *test_list_view_response_has_image* - Checks that list_view dictionary contains correct information, by checking for 'image' key.

* *test_create_view_still_works* - Checks that create_view works with addition of database, not just with previous .py module of journal data. 

* *test_create_get_request_returns_correct_page* - Checks that when a GET request is sent to the create_view page, it returns just the blank page, not a POST request/its info to the DB. 

* *test_list_view_return_journal_instance_with_incomplete_info* - Test that when one adds an incomplete entry to the DB, the page cannot find the information afterwards. 

* *test_list_view_http_not_found* - Test that when there are no posts, list_view raises an HTTPNotFound error. 

* *test_update_view_still_works* - Test that update_view works with update to DB usage. 

* *test_update_view_replaces_existing_journal* - Tests that when an entry is added to the DB, it replaces the old journal, instead of just adding a new one.

* *test_make_sure_update_updates_and_doesnt_just_add_new_journal* - 2nd test for adding a new entry to overwrite old entry through update_view

### Step 2 Tests (Those not included in step 4 list)

* *test_list_view_response_title* - Checks that list_view returns the correct response title as a key in a dictionary. 

* *test_list_view_response_has_good_img* - Checks that list_view returns the correct image tag. 

* *test_list_view_has_a_post* - Checks that list_view has a post (containing body, title, and creation_date) inside. 

* *test_detail_view_has_correct_keys* - Checks that detail_view contains a dictionary with the keys image and ljpost. 

* *test_http_not_found* - Checks that detail_view raises an HTTPNotFound when a journal with a nonexistant ID is searched for. 

* *test_new_entry_has_correct_response* - Checks that a new entry (within create_entry) has a response that includes the title "Create New Entry"

* *test_new_entry_works_with_specific_entry* - Checks that response has the tag images, and that its value is 'new-entry.jpg'

* *test update_entry_works_for_response_title* - Checks that the title (within response) of update_view is 'Edit Entry'

* *test_update_entry_post_content_loads_correctly* - Tests that "10/31/2017" is the creation_date of an ljpost for id 12. (As dictated in the post data.)

* *test_update_entry_raises_http_error* - Checks that HTTPNotFound is raised when update_view is used with  an id that doesn't exist. 

* *test_update_entry_error_type* - Tests that the request response status is 404 when a 404 error (for a nonexistant ID) is raised in update_view