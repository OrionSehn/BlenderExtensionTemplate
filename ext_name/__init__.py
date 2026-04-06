import bpy

from .ext_name.submod1.foo import hello_world # to have it available in the imported namespace


__all__ = [
    "submod1",
    "hello_world"
    ]

def __dir__():
    return __all__

from .ext_name.submod1 import foo

classes = [
    foo.HelloWorldOperator
]


def register():
    hello_world() # Call the function to print "Hello, World!" when the extension is registered
    foo.HelloWorldOperator
    print("Registering extension...")
    for cls in classes:
        bpy.utils.register_class(cls)
    

def unregister():
    print("Unregistering extension...") 
    hello_world()