import bpy
from mathutils import Vector

bl_info = {
    "name": "Gesture Helper",
    "description": "手势助手,可以快速的使用手势运行blender 操作符或是更改属性",
    "author": "AIGODLIKE Community(BlenderCN辣椒, 会飞的键盘侠, 小萌新)",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "Tool Panel",
    "support": "COMMUNITY",
    "category": "辣椒出品",
}


def HookReset(object, hook):
    for m in object.modifiers:
        if m.object==hook:
            P=Vector([m.center[0],m.center[1],m.center[2]])
            hook.location=P


class HookResetOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.hook_reset_lj"
    bl_label = "辣椒:钩挂物体校正已启动"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and len(context.selected_objects)==2

    def execute(self, context):
        ob=context.active_object
        hk=[obj for obj in context.selected_objects if obj != ob]
        print(hk)
        HookReset(ob, hk[0])
        return {'FINISHED'}


def register():
    bpy.utils.register_class(HookResetOperator)


def unregister():
    bpy.utils.unregister_class(HookResetOperator)


if __name__ == "__main__":
    register()

