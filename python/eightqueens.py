import sys

__author__ = 'o'


# solve the 8-queens problem

# Represent the board thus: [x,y]

#  [0,0] [1,0] [2,0] ...
#  [0,1] [1,1] ...
#  [0,2] [1,2] ...



class QueenPosition():
    """Use this class (maybe abstract) to represent a square on a chessboard"""

    def __init__(self, x, y):
        """Constructor for QueenPosition"""
        if x not in range(8) or y not in range(8):
            raise Exception
        self.x = x
        self.y = y
        self.queen = False  # return to representing queens soon

    def share_row(self, other):
        if self.y == other.y:
            return True
        return False

    def share_column(self, other):
        if self.x == other.x:
            return True
        return False


    def share_diagonal(self, other):
        # Case one: x = y + c
        # Case two: x = -y + c
        xdiff = self.x - other.x
        ydiff = self.y - other.y

        if abs(xdiff) is abs(ydiff):
            return True
        return False

    def threatens(self, other):
        if self.share_row(other) or self.share_column(other) or self.share_diagonal(other):
            return True
        return False




def display_board():
    for queen in qpositions:
        y = queen.y
        before = y
        after = 8 - y - 1
        for _ in range(before):
            sys.stdout.write('O ')
        sys.stdout.write('X ')
        for _ in range(after):
            sys.stdout.write('O ')
        sys.stdout.write("\n")  # as row number increases by 1 each queen

# Convenience global variable
qpositions = []

def try_qp(new):
    if any(qp.threatens(new) for qp in qpositions):
        return False
    return True


class NoValidPositionException(Exception):
    pass

def add_queen_to_row(row, offset = 0):
    found_solution = False
    for column in range(8):
        if row is 0 and column < offset:
            continue
        new_qp = QueenPosition(row, column)
        if not try_qp(new_qp):
            # print "Position at %s, %s does not work" % (row, column)
            continue
        qpositions.append(new_qp)
        # print [(qp.x, qp.y) for qp in qpositions]
        if row is 7:
            return True
        try:
            found_solution = add_queen_to_row(row+1)
            if found_solution:
                return True
        except NoValidPositionException:
            qpositions.pop()
            continue
    else:
        raise NoValidPositionException



def main():
    global qpositions
    add_queen_to_row(0)
    print "First position"
    display_board()


    qpositions = []
    add_queen_to_row(0,1)
    print "\nSecond position"
    display_board()


    qpositions = []
    add_queen_to_row(0,2)
    print "\nThird position"
    display_board()

    qpositions = []
    add_queen_to_row(0,3)
    print "\nFourth position"
    display_board()


if __name__ == '__main__':
    main()
