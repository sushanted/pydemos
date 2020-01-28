deleted_variable = 5
print(deleted_variable)
del deleted_variable

# Following two statements are same now, as x is deleted
try:
    print(deleted_variable)
except NameError as err:
    print(err)

try:
    print(undefined_variable)
except NameError as err:
    print(err)

print("\nScopes\n")

# This is global scope

value = "global value set at global level"


def scope_test():
    # This is non local scope

    def access_local():
        # This is local scope
        value = "local value set in local scope"

    def access_nonlocal():
        nonlocal value
        value = "nonlocal value set in local scope"

    def access_global():
        global value
        value = "global value set in local scope"

    value = "value set in non local scope"
    access_local()
    print("After local assignment:", value)
    access_nonlocal()  # This changes the non local value
    print("After nonlocal assignment:", value)
    access_global()  # This changes the global value, non local remains the same
    print("After global assignment:", value)


scope_test()
print("In global scope:", value)

print("\nNon local multi level\n")


# Level 1 (global)
def level2():
    # Level 2
    level_2_value = "level 2 value set at level 2"
    overridden_value = "overridden value set at level 2"

    def level3(short):
        # Level 3
        nonlocal level_2_value
        level_2_value = "level 2 value set at level 3"
        level_3_value = "level 3 value set at level 3"
        overridden_value = "overridden value set at level 3"
        if short: return

        def level4():
            # Level 4
            nonlocal level_2_value  # the outermost value
            nonlocal level_3_value
            level_2_value = "level 2 value set at level 4"
            level_3_value = "level 3 value set at level 4"
            overridden_value = "overridden value set at level 4"

        level4()
        print("After calling level 4 function")
        print("level_2_value", level_2_value)
        print("level_3_value", level_3_value)
        print(overridden_value)
        level3(
            True)  # This is recursive call, level_3_value inside this call is a local scoped variable, changing it's value won't change the value in level3() function
        print("After resetting value at level 3")
        print("level_2_value", level_2_value)
        print("level_3_value", level_3_value)

    level3(False)
    print("level_2_value", level_2_value)
    print(overridden_value)
    # print("level_3_value", level_3_value)


level2()

print("\nOverriding values/read only values\n")

global_var_overridden = "global value of global_var_overridden"
global_var = "global value of global_var"


def fun():
    # The global variables are read only, as soon as they are assigned a value, a new variable with the same name
    # is created in local scope : it is no more related to global scope. Same is about nonlocal variables
    global_var_overridden = "local value of global var overridden"
    print(global_var_overridden)
    # print(global_var) # This won't compile as there is another variable defined in the local scope with the same name
    # Above would have compiled if we had declared global_var as global
    global_var = "local value of global var"


fun()

print("\nNested values\n")
outer = "Level1"


def level2():
    outer = "Level2"

    def level3():
        print("Outer: ", outer)  # This is the value defined in immediately nesting scope(Level2) and NOT Level1

    level3()


level2()
