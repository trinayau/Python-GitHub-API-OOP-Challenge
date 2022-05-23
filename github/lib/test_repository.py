from .repository import Repository

class TestRepoCase():
    def test_name(self, repo_test_data):
        repo = Repository(repo_test_data)
        assert repo.name == 'Test Repo'

    def test_description(self, repo_test_data):
        repo = Repository(repo_test_data)
        assert repo.description == 'Test Description'

    def test_forks(self, repo_test_data):
        repo = Repository(repo_test_data)
        assert repo.forks == 'Test Fork'

    def test_save(self, repo_test_data):
        start_len = len(Repository.all)
        repo = Repository(repo_test_data)
        assert len(Repository.all) == start_len + 1

    def test_find_by_input(self, repo_test_list):
        Repository.all = []
        for data in repo_test_list:
            Repository(data)
        repo = Repository.find_by_input("2")
        assert repo.name == repo_test_list[1]['name']
