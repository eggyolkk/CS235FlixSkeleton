from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watchlist: list = []
        self.__size: int = len(self.__watchlist)

    @property
    def watchlist(self):
        return self.__watchlist

    def add_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            add = True
            for m in self.__watchlist:
                if str(m) == str(movie):
                    add = False
                    break

            if add:
                self.__watchlist.append(movie)
                self.__size += 1

    def remove_movie(self, movie: Movie):
        remove_m = None
        if isinstance(movie, Movie):
            for m in self.__watchlist:
                if m.title == movie.title and m.release_date == movie.release_date:
                    remove_m = m

            if remove_m is not None:
                self.__watchlist.remove(remove_m)
                self.__size -= 1
        

    def select_movie_to_watch(self, index: int):
        if 0 <= index <= len(self.__watchlist) - 1:
            return self.__watchlist[index]
        else:
            return None

    def size(self):
        return self.__size

    def first_movie_in_watchlist(self):
        if self.__size == 0:
            return None
        else:
            return self.__watchlist[0]

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= self.__size:
            raise StopIteration
        else:
            movie = self.__watchlist[self.i]
            self.i += 1
            return movie
