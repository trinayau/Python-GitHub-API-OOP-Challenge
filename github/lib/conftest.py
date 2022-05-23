import pytest

@pytest.fixture
def repo_test_data():
    return { 
        "name": "Test Repo",
        "description": "Test Description",
        "forks": "Test Fork"
    }


@pytest.fixture()
def repo_test_list():
    return [
        {   "username": "username",
            "name": "Test Repo 1",
            "description": "Test Description",
            "forks_count": "Test Fork"
        },
        { 
            "name": "Test House 2",
            "description": "Test Description 2",
            "forks_count": "Test Fork 2"
        }
    ]
