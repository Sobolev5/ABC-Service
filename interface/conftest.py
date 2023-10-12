import uuid
import pytest
from django.contrib.auth.models import User
import settings
from settings import POSTGRES_DB
from settings import POSTGRES_HOST
from settings import POSTGRES_PASSWORD
from settings import POSTGRES_PORT
from settings import POSTGRES_USER
from settings import TEST_USER_EMAIL
from settings import TEST_USER_PASSWORD


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        "ATOMIC_REQUESTS": False
    }


@pytest.fixture
def test_password():
   return 'abc'

  
@pytest.fixture
def create_user(db, django_user_model, test_password):
   def make_user(**kwargs):
       kwargs['password'] = test_password
       if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return make_user


@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
   def make_auto_login(user=None):
       if user is None:
           user = create_user()
       client.login(username=user.username, password=test_password)
       return client, user
   return make_auto_login