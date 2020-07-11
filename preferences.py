import bpy
from bpy.props import (
    StringProperty,
)


class VIEW3D_OT_image_utilis_preferences(bpy.types.AddonPreferences):
    '''Addon preferences'''

    bl_idname = __package__
    # here you define the addons customizable props

    b_baseColor: StringProperty(name="Basecolor", default=True)
    b_roughnessMetalnessAO: bpy.props.StringProperty(name="RMA (roughnessMetalnessAo)", default=True)
    b_normal: bpy.props.StringProperty(name="Normal", default=True)
    b_emissive: bpy.props.StringProperty(name="Emissive", default=False)
    b_roughness: bpy.props.StringProperty(name="Roughness", default=False)
    b_metalness: bpy.props.StringProperty(name="Metalness", default=False)
    b_ambientOcclussion: bpy.props.StringProperty(name="AmbientOcclusion", default=False)

    baseColorSuf: StringProperty(name="Basecolor Suffix", default="_B")
    normalSuf: StringProperty(name="Basecolor Suffix", default="_N")
    roughnessMetalnessAOSuf: StringProperty(name="RMA (roughnessMetalnessAo)", default="_RMA")
    emissiveSuf: StringProperty(name="Emissive", default="_E")
    roughnessSuf: StringProperty(name="Roughness", default="_R")
    metalnessSuf: StringProperty(name="Metalness", default="_M")
    ambientOcclussionSuf: StringProperty(name="AmbientOcclusion", default="_AO")

    props = [
        "b_baseColor",
        "b_roughnessMetalnessAO",
        "b_normal",
        "b_emissive",
        "b_roughness",
        "b_metalness",
        "b_ambientOcclussion",

        "baseColorSuf",
        "normalSuf",
        "roughnessMetalnessAOSuf",
        "emissiveSuf",
        "roughnessSuf",
        "metalnessSuf",
        "ambientOcclussionSuf"
    ]

    # here you specify how they are drawn
    def draw(self, context):
        layout = self.layout
        for propName in self.props:
            raw = layout.raw()
            raw.prop(self, propName)
