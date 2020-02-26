# An IMPORTANT note on MRO order :
# the basic rule : depth-first, left-right (starting from the class of the object on which a method id called)
# the dedup rule : If above rule generates any duplicates, all but last duplicate is eliminated
# Examples:
# 1) B(A) C(A) D(B,C) : mro => [D,B,A,C,A] => [D,B,C,A]
# 2) B(A) C(A) D(C) E(B,D) : mro => [E,B,A,D,C,A] => [E,B,D,C,A]
# The logic behind eliminating duplicates : Allow more specialized methods to be executed instead of very generic method:
# E.g. in following hierarchy :  B(A) C(A) D(B,C), if A and C has implemented m() and B hasn't implemented m()
# when m() is called on D, better call C.m() instead of A.m(), because it is more specialized then A.m()


# Classic diamond hierarchy
class Top:
    def print(self):
        print("center")

    def top_print(self):
        print("center_print")

    def only_right_print(self):
        print("only_right_print of Top")


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

    def only_right_print(self):
        print("only_right_print of Right")


class BottomLR(Left, Right):
    pass


class BottomRL(Right, Left):
    pass


for cls in (BottomLR, BottomRL):
    ob = cls()
    print(f"For class: {ob.__class__} with inheritance order: {ob.__class__.__bases__}")
    # The print method is found in mro order
    # The output depends on the class for LR Left.print is found first, for RL Right.print is found first
    ob.print()
    # All inherited methods are available
    ob.top_print()
    ob.left_print()
    ob.right_print()
    # method in top, overridden in left only, missing in right
    ob.only_right_print()

print("\nSuper with multiple inheritance:")


#                          Player
#               /             |           \
#             /               |            \
#           Batsman         Bowler       Fielder
#               \              |            |
#                \             |          Keeper
#                 \            |            /
#                           AllRounder
# Note : super() doesn't always return a super class, in case of multiple inheritance it returns
# the next class in mro order, it could a next sibling as well


class Player:
    def print_name(self):
        print("Player")


class Batsman(Player):
    def print_name(self):
        print("Batsman")
        super().print_name()


class Bowler(Player):
    def print_name(self):
        print("Bowler")
        super().print_name()


class Fielder(Player):
    def print_name(self):
        print("Fielder")
        super().print_name()


class Keeper(Fielder):
    def print_name(self):
        print("Keeper")
        super().print_name()


class AllRounder(Batsman, Bowler, Keeper):
    def print_name(self):
        super().print_name()


# Allrounder mro => [AllRounder.Batsman,Player,Bowler,Player,Keeper,Fielder,Player] => [AllRounder,Batsman,Bowler,Keeper,Fielder,Player]

AllRounder().print_name()

print(AllRounder.mro())
