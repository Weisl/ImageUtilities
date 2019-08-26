'''
Copyright (C) 2017 MATTHIAS PATSCHEIDER
patscheider.matthias@gmail.com

Created by Matthias Patscheider

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#The addon is currently able to
#       export ALL images to a csv. Procedural and images with no path are simply shown blank
#       it shows the current image resolution. this value can not be changed
#       create the material tree for all materials (DESTRUCTIVE)




# TODO: Make a list of materials that are supposed to be effected by the texture reload and creation for the shader tree
# TODO: Easily change the prefixes for the textures



bl_info = {
    "name": "Image Utilities",
    "description": "Export and import texture paths from csv files",
    "author": "Matthias Patscheider",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object"}
# load and reload submodules
##################################

if "bpy" in locals():
    import importlib

    importlib.reload(createMaterialNodes)
    importlib.reload(csv_util)
    importlib.reload(imageFile_utils)
    importlib.reload(operators)
    importlib.reload(panel)
    importlib.reload(preferences)

else:
    from . import preferences
    from . import createMaterialNodes
    from . import csv_util
    from . import imageFile_utils
    from . import operators
    from . import panel

import bpy
from bpy.types import WindowManager, Scene

classes = (
    createMaterialNodes.IMAGES_OT_LoadImages,
    operators.IMAGES_OT_change_extension,
    operators.IMAGES_OT_export_csv,
    operators.IMAGES_OT_print_csv,
    operators.IMAGES_OT_import_paths_from_csv,
    operators.IMAGES_OT_load_paths_from_csv_02,
    operators.IMAGES_OT_import_csv,
    operators.IMAGES_OT_findIn_csv,
    panel.LAYOUT_PT_TexturePanel,
    preferences.SomeAddonPrefs
)

# register
##################################
import traceback

def register():

    WindowManager.csv_dir = bpy.props.StringProperty(
            name="Export Path",
            subtype='DIR_PATH',
            default=""
            )

    WindowManager.texture_dir = bpy.props.StringProperty(
            name="Texture Directory",
            subtype='DIR_PATH',
            default=""
            )
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)