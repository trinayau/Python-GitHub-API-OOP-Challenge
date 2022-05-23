from .api import fetch_repos
from .repository import Repository

class Format():
    ''' ASCI codes for formatting '''
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CLEAR = '\033[0m'

class CLI():
    ''' User interface '''
    def __init__(self):
        self._user_input = ""
        self._repo_input = ""

    #starts up when code is run
    def start(self):
        try:
            print(f'\n{Format.BLUE}{Format.BOLD}Search for GitHub users and see their repos!{Format.CLEAR}\n')
            self.get_user_choice()
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    def menu(self):
        for idx, repo in enumerate(Repository.all, start=1):
            print(f'{idx}. {repo.name}')
        self.get_repo_choice()

    #gets user input
    def get_user_choice(self):
        try:
            self._user_input = input(f'''\n{Format.BLUE}Which user would you like see the repos of?\n{Format.CLEAR}''')
            
            if self._user_input == 'exit':
                return self.goodbye()
                
            fetch_repos(self._user_input)
            self.menu()

        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    def get_repo_choice(self):
        try:
            self._repo_input = input(f'''\n{Format.GREEN}Which repo would you like see more of? To choose new user, type 'user' \n{Format.CLEAR}''')
            
            if self._repo_input == 'exit':
                return self.goodbye()

            if self._repo_input == 'user':
                Repository.all.clear()
                return self.get_user_choice()

            if self.valid_input(self._repo_input):
                self.show_repo()
                self.get_repo_choice()

        except ValueError:
             print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
             self.menu()

    def show_repo(self):
        repo = Repository.find_by_input(self._repo_input)
        print(f'\n{Format.BLUE}{Format.BOLD}Title:{repo.name}{Format.CLEAR}')
        print(f'\n{Format.BLUE}{Format.BOLD}Description:{repo.description}{Format.CLEAR}')
        print(f'\n{Format.BLUE}{Format.BOLD}Forks:{repo.forks}{Format.CLEAR}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repository.all)

    @staticmethod
    def goodbye():
        print(f'\n{Format.BLUE}{Format.BOLD}Thanks for using my GitHub bot!{Format.CLEAR}\n')

if __name__ == '__main__':
    app = CLI()
