import bpy

# from foo import hello_world # to have it available in the imported namespace
import ext_name.submod1


# __all__ = [
#     "submod1",
#     "hello_world"
#     ]

# def __dir__():
#     return __all__

# from ext_name.submod1 import foo

# classes = [
#     foo.HelloWorldOperator
# ]


def register():
    print("Registering extension...") 
    print("Available submodules:", dir(ext_name))
    # print("Available further submodules:", dir(ext_name.ext_name))
    # print("Available EVEN further submodules:", dir(ext_name.ext_name.ext_name))

def unregister():
    print("Unregistering extension...") 
    # hello_world()