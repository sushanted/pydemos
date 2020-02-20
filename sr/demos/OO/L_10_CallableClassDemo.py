class Callable:

    def __call__(self,*args):
        print("callable called with args: "+str(args))


callable_instance = Callable()

# Now onwards callable_instance will behave as a regular method

callable_instance() # () after the instance name calls the __call__ method of the class

callable_instance(1,2,'value')

