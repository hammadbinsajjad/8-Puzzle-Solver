class PuzzleSolver:
    """
    Solves an 8 Puzzle given its start state. Checks if it's solvable or not.
    Solution is the tiles ordered in increasing order i.e 1 - 8
    """

    def __init__(self, start: list) -> None:
        self.__start = start
        self.__goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def solve(self):
        if not self.__is_solvable():
            raise InsolvableException()

    def __result(self, state, action):
        pass

    def __is_solvable(self) -> bool:
        """
        Returns True if the start state can be solved, False otherwise.
        """
        flat = [n for row in self.__start for n in row]

        # Calculate inversions
        inversions = 0
        for i in range(3):
            for j in range(3):
                if flat[i] > flat[j]:
                    inversions += 1

        if inversions % 2 != 0:
            return False

        return True


class InsolvableException(Exception):
    """
    Exception to raise if solution is not possible for the puzzle
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = "The start state cannot be solved to achieve the goal state."

    def __str__(self) -> str:
        return super().__str__() + self.message
