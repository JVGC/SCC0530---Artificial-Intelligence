class Block:
    def __init__(self, position, parent=()):
        self.position = position
        self.parent = parent
        self.distance_start = 0 
        self.distance_end = 0   
        self.distance_total = 0

    # Cmp the blocks
    def __eq__(self, other):
        return self.position == other.position

    # Order
    def __lt__(self, other):
         return self.distance_total < other.distance_total

    # Print Block
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.distance_total))

def check_block(valids, neighbor):
        for block in valids:
            if (neighbor == block and neighbor.distance_total >= block.distance_total):
                return False
        return True