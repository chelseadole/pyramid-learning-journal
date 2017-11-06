# Pyramid Learning Journal Tests plan/outline
### Chelsea Dole, 11/05/2017


#### Step 4 Tests

* *test_list_view_returns_dictionary* - Checks that list_view returns a dictionary containing information to send to jinja2 homepage. 

* *test_list_view_response_has_image* - Checks that list_view dictionary contains correct information, by checking for 'image' key.

* *test_journal_is_added_to_db* - Checks that new Journal class instance is added to database correctly by testing size of DB before and after insertion of new Journal instance.

* *test_created_journal_in_db_is_a_dict* - Checks that the new Journal class instance is a dictionary.

* *test_detail_view_non_existent_journal* - Checks that when detail_view is sent a request for a non-existance journal entry ID, it returns an HTTPNotFound page. 

* 