class Genre:
    def __init__(
            self, genre_name: str
    ):
        if genre_name == "":
            self._genre_name: str = "None"
        else:
            self._genre_name: str = genre_name

    @property
    def genre_name(self) -> str:
        return self._genre_name

    def __repr__(self) -> str:
        return f'<Genre {self._genre_name}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Genre):
            return False
        return other._genre_name == self._genre_name

    def __lt__(self, other) -> bool:
        return self._genre_name < other._genre_name

    def __hash__(self) -> str:
        return hash(self._genre_name)