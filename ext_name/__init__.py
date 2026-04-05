from .ext_name.submod1.foo import hello_world

def register():
    print("Registering extension...")
    hello_world()   

def unregister():
    print("Unregistering extension...") 
    hello_world()