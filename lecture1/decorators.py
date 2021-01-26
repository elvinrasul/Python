def announce(f):
    def wrapper():
        print("About the run the function...")
        f()
        print("Done with the function.")
    return wrapper

 # this is all decortator. for example

@announce
def hello():
    print("Hello World!")  

hello()

