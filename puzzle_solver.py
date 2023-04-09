class PuzzleSolver8:
    """
    Solves an 8 Puzzle given its start state. Checks if it's solvable or not.
    Solution is the tiles ordered in increasing order i.e 1 - 8
    """

    def __init__(self, start: list) -> None:
        self.__start = start
        self.__goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def solve(self):
        """
        Solve the puzzle, displays the path from the start state to goal state
        """
        if not self.__is_solvable():
            raise InsolvableException()

        depth_limit = 0
        while True:
            path = self.__search(self.__start, depth_limit, "")

            if path is None:
                depth_limit += 1
                continue
            else:
                path.reverse()
                for p in path:
                    self.__print_state(p)
                break

    def __search(self, state, depth_limit, prev_action):
        """
        Iterative Depth Limited Search algorithm to search for the goal
        """
        if state == self.__goal:
            return [state]

        if depth_limit <= 0:
            return

        for action in self.__actions(state, prev_action):
            next_state = self.__result(state, action)
            path = self.__search(next_state, depth_limit - 1, action)

            if path is not None:
                path.append(state)
                return path

    def __actions(self, state, prev_action):
        """
        Returns all the possible actions that can be performed
        """
        empty = self.__find_empty(state)

        actions = []

        # Check which actions are possible
        if empty[1] - 1 >= 0 and prev_action != "RIGHT":
            actions.append("LEFT")

        if empty[1] + 1 <= 2 and prev_action != "LEFT":
            actions.append("RIGHT")

        if empty[0] + 1 <= 2 and prev_action != "UP":
            actions.append("DOWN")

        if empty[0] - 1 >= 0 and prev_action != "DOWN":
            actions.append("UP")

        return actions

    def __result(self, state, action):
        """
        Returns a state with the action performed, assumes action is possible
        """
        from copy import deepcopy

        temp_state = deepcopy(state)

        empty = self.__find_empty(temp_state)

        mapping = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        non_empty = (empty[0] + mapping[action][0], empty[1] + mapping[action][1])

        # swap the values to perform the action
        temp_state[empty[0]][empty[1]], temp_state[non_empty[0]][non_empty[1]] = \
            temp_state[non_empty[0]][non_empty[1]], temp_state[empty[0]][empty[1]]

        return temp_state

    def __find_empty(self, state):
        """
        Finds the index of the empty tile space
        """
        empty = (-1, -1)
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty = (i, j)
                    break
            if empty != (-1, -1):
                break
        return empty

    def __is_solvable(self):
        """
        Returns True if the start state can be solved, False otherwise.
        """
        flat = [n for row in self.__start for n in row]

        # Calculate inversions
        inversions = 0
        for i in range(9):
            for j in range(i, 9):
                if flat[j] and flat[i] > flat[j]:
                    inversions += 1

        if inversions % 2 != 0:
            return False

        return True

    def __print_state(self, state):
        """
        Prints a given state in 3 x 3 grid
        """
        for row in state:
            for el in row:
                print(el, end=" ")
            print()
        print()


class InsolvableException(Exception):
    """
    Exception to raise if solution is not possible for the puzzle
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = "The start state cannot be solved to achieve the goal state."

    def __str__(self) -> str:
        return super().__str__() + self.message
