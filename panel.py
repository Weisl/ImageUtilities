import bpy

debugMode = True

class LAYOUT_PT_TexturePanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Texture CSV Panel"
    bl_idname = "MISC"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        global debugMode

        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Export CSV")

        row = layout.row()
        wm = bpy.context.window_manager
        row.prop(wm, "csv_export_dir")

        row = layout.row()
        row.operator("images.path_export_csv", text = "Export CSV").my_append = False
        row.operator("images.path_export_csv", text = "Append to CSV").my_append = True

        row = layout.row()

        row.label(text="Import CSV")
        row = layout.row()
        row.prop(wm, "csv_import_file")
        row = layout.row()
        row.operator("images.load_from_csv")

        row = layout.row()
        row.label(text="Material from Textures")
        row = layout.row()
        row.prop(wm, "texture_dir")
        row = layout.row()
        row.operator("images.create_nodetree")

        row = layout.row()
        row.label(text="Image Operators")
        row = layout.row()
        row.operator("images.path_change_extension")

        if debugMode == True:
            row = layout.row()
            row.label(text = "Debut Mode")
            row = layout.row()
            row.operator("images.path_print_import_csv")
            row = layout.row()
            row.operator("images.load_from_csv_replace001")
            row = layout.row()
            row.operator("images.images.path_print_csv")
            row = layout.row()
            row.operator("images.find_in_csv")


