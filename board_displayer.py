from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror

'''
Name:   Oilver Zhang
SID:    520651281
Unikey: ozha8307

BoardDisplayer - A helper class used to display the circuit board.
Each time a component is added to the circuit, this board is updated to
store the component's symbol in its assigned position on the board.

You are free to add more attributes and methods, as long as you aren't
modifying the existing scaffold.
'''


class BoardDisplayer:
    def __init__(self, width: int, height: int):
        '''
        Initialises a BoardDisplayer instance given a width and height
        which is the size of the circuit board. board should be
        initialised to the return value of the create_board method.

        width:  int             - the width of this board
        height: int             - the height of this board
        board:  list[list[str]] - a list of list of strings representing the
                                  circuit board, having the symbol of each
                                  component and photon in the circuit at its
                                  assigned position

        Parameters
        ----------
        width  - the width to set this board to
        height - the height to set this board to
        '''
        self.width = width
        self.height = height
        self.board = BoardDisplayer.create_board(self)

    def create_board(self) -> list[list[str]]:
        '''
        Creates a board of size width x height and returns it.

        Returns
        -------
        Returns a list of list of strings representing an empty circuit
        board of size width x height.

        Example
        -------
        >>> self.width, self.height
        (8, 3)
        >>> create_board() # board split across multiple lines for readability
        [
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        The board above has 3 rows (height), with each row having 8 columns (width).
        Each cell is initialised as a space, which represents an empty cell.
        '''
        board = []
        row = 0
        # for each row, generate all the cols
        while row < self.height:
            current_row = []
            col = 0
            while col < self.width:
                current_row.append(' ')
                col += 1
            board.append(current_row)
            row += 1
        return board

    def add_component_to_board(
            self,
            component: Emitter | Receiver | Mirror) -> None:
        '''
        Adds the symbol of the component on the board at its assigned
        position.

        Parameters
        ----------
        component: the component to add its symbol on the board

        Hint
        ----------
        You shouldn't need to care what type of component you are adding,
        since all components have a symbol, x and y.

        >>> self.board # board split across multiple lines for readability
        [
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
        ]
        >>> emitter = Emitter('A', 0, 0)
        >>> receiver = Receiver('R0', 2, 0)
        >>> self.add_component_to_board(emitter)
        >>> self.add_component_to_board(receiver)
        >>> self.board
        [
         ['A', ' ', '0'],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
        ]
        '''
        # check inputted x,y are within board's indices range, then duck type.
        if (0 <= component.x < self.width) and (
                0 <= component.y < self.height):
            # to make sure that we add only the last symbol of receiver to
            # board.
            self.board[component.y][component.x] = component.get_symbol()

    def add_photon_to_board(self, photon: Photon) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Adds the symbol of the photon on the board at its current position. If
        there already is a component on the board at its position, it should not
        replace it.

        Parameters
        ----------
        photon: the photon to add its symbol on the board
        '''
        # check if photon is in-bounds of board and if its current cell is
        # empty.
        if (0 <= photon.x < self.width) and (0 <= photon.y <
                                             self.height) and self.board[photon.y][photon.x] == " ":
            self.board[photon.y][photon.x] = photon.get_symbol()

    def print_board(self) -> None:
        '''
        Prints a formatted board with the border included.

        Example 1
        ---------
        >>> self.board # board split across multiple lines for readability
        [
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        >>> self.print_board()
        +--------+
        |        |
        |        |
        |        |
        +--------+

        Example 2
        ---------
        >>> self.board # board split across multiple lines for readability
        [
         ['A', ' ', ' ', ' ', ' ', ' ', ' ', '0'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['B', ' ', ' ', ' ', ' ', ' ', ' ', '1']
        ]
        >>> self.print_board()
        +--------+
        |A      0|
        |        |
        |B      1|
        +--------+

        Example 3
        ---------
        >>> self.board # board split across multiple lines for readability
        [
         ['A', '.', '.', '.', '.', '.', '.', '0'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['B', '.', '.', '.', '.', '.', '.', '1']
        ]
        >>> self.print_board()
        +--------+
        |A......0|
        |        |
        |B......1|
        +--------+
        '''

        top_and_bot = "+" + "-" * self.width + "+"
        print(top_and_bot)
        # for each row, concatenate all elements into a single string, coated
        # with "|"
        row = 0
        all_rows = ""
        while row < self.height:
            row_string = ""
            col = 0
            while col < self.width:
                row_string += self.board[row][col]
                col += 1
            print("|" + row_string + "|")
            row += 1
        print(top_and_bot)

