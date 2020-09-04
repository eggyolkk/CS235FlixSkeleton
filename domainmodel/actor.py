class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name: str = actor_full_name.strip()
        self._actor_colleagues: list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self) -> str:
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other) -> bool:
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self) -> str:
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self._actor_colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague) -> bool:
        return colleague in self._actor_colleagues
