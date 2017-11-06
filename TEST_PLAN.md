# Pyramid Learning Journal Tests plan/outline
### Chelsea Dole, 11/05/2017


#### Step 4 Tests

* *test_list_view_returns_dictionary* - Checks that list_view returns a dictionary containing information to send to jinja2 homepage. 

* *test_list_view_response_has_image* - Checks that list_view dictionary contains correct information, by checking for 'image' key.

* *test_journal_is_added_to_db* - Checks that new Journal class instance is added to database correctly by testing size of DB before and after insertion of new Journal instance.

* *test_created_journal_in_db_is_a_dict* - Checks that the new Journal class instance is a dictionary.

* *test_detail_view_non_existent_journal* - Checks that when detail_view is sent a request for a non-existance journal entry ID, it returns an HTTPNotFound page. 

* *test_create_view_still_works* - Checks that create_view works with addition of database, not just with previous .py module of journal data. 

* *test_create_get_request_returns_correct_page* - Checks that when a GET request is sent to the create_view page, it returns just the blank page, not a POST request/its info to the DB. 

* *test_list_view_return_journal_instance_with_incomplete_info* - Test that when one adds an incomplete entry to the DB, the page cannot find the information afterwards. 

* *test_update_view_still_works* - Test that update_view works with update to DB usage. 