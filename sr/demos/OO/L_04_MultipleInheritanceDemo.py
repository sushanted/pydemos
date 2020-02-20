
# Classic diamond hierarchy
class Top:
    def print(self):
        print("center")

    def top_print(self):
        print("center_print")


class Left(Top):
    def print(self):
        Top.print(self)
        print("left")

    def left_print(self):
        print("left_print")


class Right(Top):
    def print(self):
        Top.print(self)
        print("right")

    def right_print(self):
        print("right_print")


class BottomLR(Left, Right):
    pass


class BottomRL(Right, Left):
    pass


for cls in (BottomLR, BottomRL):
    ob = cls()
    print(f"For class: {ob.__class__} with inheritance order: {ob.__class__.__bases__}")
    # The print method is found bottom to top, left to right manner
    # The output depends on the class for LR Left.print is found first, for RL Right.print is found first
    ob.print()
    # All inherited methods are available
    ob.top_print()
    ob.left_print()
    ob.right_print()
