# Standard classes like str,int,list can be subclassed

class CSV(str):

    # Accept any type of value (str,int,float...) and use it's str representation to create the CSV instance
    def __init__(self, value):
        str.__init__(str(value))

    # Overloading + for CSV, should return a CSV
    def __add__(self, other):
        # self is an str (by inheritance)
        # Using standard + operator for str
        # Convert the str again to CSV
        return CSV(str(self) + ',' + str(other))

    # Overloading the iadd : csv += other
    # Note : no need to modify the internal state of self, python assigns the result again to the LHS variable
    def __iadd__(self, other):
        # reuse the __add__ already defined above
        return self + CSV(other)

    # Overloading the reverse add : other + CSV : first operand is other
    def __radd__(self, other):
        # Convert the other to CSV first
        # reuse the __add__ already defined above
        return CSV(other) + self

    # Overloading unary operator ~ for a CSV
    def __invert__(self):
        return CSV(",".join(reversed(self.split(","))))


csv1 = CSV("one")
csv2 = CSV("two")

print("csv1 : ", csv1)
print("csv2 : ", csv2)
print("type(csv1) : ", type(csv1))
print("csv1 + csv2 : ", csv1 + csv2)
print("csv3 = csv1 + csv2")
csv3 = csv1 + csv2
print("csv3 : ", csv3)  # one,two
print("type(csv3) : ", type(csv3))
print("csv1 + csv2 + 'any_string_after_csv' : ", csv1 + csv2 + "any_string_after_csv")
print("~csv3 : ", ~csv3)  # two,one

print("'zero' + csv3 : ", 'zero' + csv3)  # zero,one,two

print('CSV(0) + 1 + 2 : ', CSV(0) + 1 + 2)  # 0,1,2

print('1.0 + CSV(2.0) : ', 1.0 + CSV(2.0))  # 1.0,2.0

csv4 = CSV(4)
# iadd will be triggered
csv4 += 5
csv4 += 6
print("\ncsv4 = CSV(4)\ncsv4 += 5\ncsv4 += 6\ncsv4 : ", csv4)

print("\nComplex operations:")
print("\n~(CSV(0)+1+2+3) : ", ~(CSV(0) + 1 + 2 + 3))
print("\n~(1+2+CSV(4)+5)+2+1+0 : ", ~(1 + 2 + CSV(4) + 5) + 2 + 1 + 0)
