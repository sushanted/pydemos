# Evaluate any python expression
evaluated_list = eval("['a','b']+['c']")

print(evaluated_list)

# Previously defined variables can also be used in the evaluation
eval("evaluated_list.extend(('x','y','z'))")

print(evaluated_list)

# Note : assignments cannot be done in eval

# eval vs exec : eval evaluates the expression and returns the result, assignments cannot be done
# exec executes the statement, doesn't return anything

# PyCalculator using eval
print("Enter any expression to evaluate, q to quit:")
while (expression := input()) != 'q':
    try:
        print(eval(expression))
    except Exception as e:
        print(e)

# PyExecutor using exec
print("Enter any statement to execute, q to quit:")
while (expression := input()) != 'q':
    try:
        exec(expression)
    except Exception as e:
        print(e)
