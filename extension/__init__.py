import bpy

from ext_name.submod1.foo import hello_world # to have it available in the imported namespace
import ext_name


__all__ = [
    "submod1",
    "hello_world"
    ]

def __dir__():
    return __all__

from ext_name.submod1 import foo

classes = [
    foo.HelloWorldOperator
]


def register():
    print("Registering extension...") 
    print("Available submodules:", dir(ext_name))
    print("__all__:", __all__)

    print("registering operator")
    bpy.utils.register_class(foo.HelloWorldOperator)

    print("Extension registered successfully.🔥🚁🚁")

def unregister():
    print("Unregistering extension...") 
    # hello_world()
    bpy.utils.unregister_class(foo.HelloWorldOperator)