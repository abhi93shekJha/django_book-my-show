### Django test Framework

- It is based on the python unittest library.
- Django adds additional features to it.
  - Dummy web browser as a Test Client.
  - We can simulate authentication.
  - It provides us with Temporary database.
- Django Rest Framework adds features for API testing.
  - It provides with API test client.
- Django gives tests.py with every app. We can write our classes there.
- Or we can create a directory named tests, then we will have to remove tests.py (we can have any one). (Note here that we will have to add __init __.py file inside my test directory for test runner to pick it up).
- modules inside test directory must start with test_ (ex. test_module_one.py etc).
- Django provides a separate database for testing.
- After every test it clears the data in the database and uses an empty and fresh database. (by default)
- This behaviour can be overridden to have a consistent database for all our testcases. (Not needed often)
- Test classes provided by django are: SimpleTestCase (No database integration), TestCase (Uses Database)

```

"""
Unit tests for views.
"""
from django.test import SimpleTestCase

from app_two import views

class ViewsTests(SimpleTestCase):
	# method name should start with test_
	def test_make_list_unique(self):
		""" Test making a list unique. """
		# setup phase (for setting up data for testing)
		sample_items = [1, 1, 2, 3, 3, 4, 5, 5, 5]

		res = views.remove_duplicates(sample_items)

		self.assertEqual(res, [1, 2, 3, 4, 5])
```

- We run the test using command "python manage.py test"

### Using APIClient

- It is provided by django rest_framework and is based on django TestClient.
- We can make api request using this class.
- We can ovverride the authentication. Meaning if logged in once, we won't have to register everytime when making an API request.

```python
from django.test import SimpleTestCase
from rest_framework.test import APIClient

# necessary to extend either with SimpleTestCase(without DB) or TestCase(with DB)
class TestViews(SimpleTestCase):

	def test_get_greetings(self):
		""" Test getting grettings. """
		client = APIClient()
		res = client.get('/greetings/') # making an API request

		self.assertEqual(res.status_code, 200)
		self.assertEqual(
			res.data,
			["Hello!", "Bonjour!", "Hola!"]
		)
```
