''' Defining the Repository class '''
class Repository():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._description = data['description']
        self._forks = data['forks_count']
        self._save()

    def _save(self):
        self.all.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    @property
    def forks(self):
        return self._forks

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]
