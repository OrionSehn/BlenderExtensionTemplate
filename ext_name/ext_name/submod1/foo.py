
import bpy 

def hello_world():
    print("Hello, World!")


class HelloWorldOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.hello_world"
    bl_label = "Hello World Operator"

    def execute(self, context):
        hello_world()
        return {'FINISHED'}