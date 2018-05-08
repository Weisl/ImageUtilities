'''
Copyright (C) 2017 Matthias Patscheider
patscheider.matthias@mgail.com

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
import bpy
import sys

from .imageFile_utils import ImageFormatEnum

class LoadImagesOp(bpy.types.Operator):
    bl_idname = "images.load"
    bl_label = "Load Images"
    bl_description = ""
    bl_options = {"REGISTER",""}

    my_basecolor = bpy.props.BoolProperty(name = "Base Color", default = True)
    my_metallic = bpy.props.BoolProperty(name = "Metallic", default = True)
    my_specular = bpy.props.BoolProperty(name = "Specular", default = True)
    my_roughness = bpy.props.BoolProperty(name = "Roughness", default = True)
    my_normal = bpy.props.BoolProperty(name = "Normal", default = True )
    my_ior = bpy.props.BoolProperty(name = "IOR", default = True)

    my_basecolor_suffix = bpy.props.StringProperty(name = "Base Color", default = "_B")
    my_metallic_suffix = bpy.props.StringProperty(name = "Base Color", default = "_M")
    my_specular_suffix = bpy.props.StringProperty(name = "Base Color", default = "_S")
    my_roughness_suffix = bpy.props.StringProperty(name = "Base Color", default = "_R")
    my_normal_suffix = bpy.props.StringProperty(name = "Base Color", default = "_N")
    my_ior_suffix = bpy.props.StringProperty(name = "Base Color", default = "_IOR")

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        wm = context.window_manager
        areaType = bpy.context.area.type
        bpy.context.area.type = 'NODE_EDITOR'

        for mat in bpy.data.materials:
            mat.use_nodes = True
            nodes = mat.node_tree.nodes
            diffuse = nodes.get("Principled BSDF")

            # clear all nodes to start clean
            for node in nodes:
                nodes.remove(node)


            textureFolder = wm.texture_dir
            if self.my_basecolor:
                texBName = mat.name + self.my_basecolor_suffix + ".png"
                filepath_B = textureFolder + texBName

                node_baseColor = nodes.new(type='ShaderNodeTexImage')
                node_baseColor.name = 'texture_B'
                node_baseColor.location = -800, 400

            if self.my_normal:
                texNName = mat.name + self.my_normal_suffix + ".png"
                filepath_N = textureFolder + texNName


                node_normal = nodes.new(type='ShaderNodeTexImage')
                node_normal.name = 'texture_N'
                node_normal.color_space = 'NONE'
                node_normal.location = -800, -400

                node_normalMap = nodes.new(type='ShaderNodeNormalMap')
                node_normalMap.name = 'normalMap'
                node_normalMap.inputs[0].default_value = 2
                node_normalMap.location = -600, -400

            if self.my_roughness:
                texRName = mat.name + self.my_roughness_suffix + ".png"
                filepath_R = textureFolder + texRName

                node_roughness = nodes.new(type='ShaderNodeTexImage')
                node_roughness.name = 'texture_R'
                node_roughness.color_space = 'NONE'
                node_roughness.location = -800, 200

            if self.my_metallic:
                texMName = mat.name + self.my_metallic_suffix + ".png"
                filepath_M = textureFolder + texMName

                node_metallic = nodes.new(type='ShaderNodeTexImage')
                node_metallic.name = 'texture_M'
                node_metallic.color_space = 'NONE'
                node_metallic.location = -800, 0

            if self.my_ior:
                rexIORName = mat.name + self.my_ior_suffix + ".png"
                filepath_IOR = textureFolder + rexIORName

                node_ior = nodes.new(type='ShaderNodeTexImage')
                node_ior.name = 'texture_IOR'
                node_ior.color_space = 'NONE'
                node_ior.location = -800, -600

            # create principled node
            node_principled = nodes.new(type='ShaderNodeBsdfPrincipled')
            node_principled.name = 'Principled'
            node_principled.inputs[0].default_value = (0, 1, 0, 1)  # green RGBA
            node_principled.inputs[1].default_value = 0  # strength
            node_principled.inputs[5].default_value = 1  # specular
            node_principled.location = -400, 0

            # create output node
            node_output = nodes.new(type='ShaderNodeOutputMaterial')
            node_output.name = 'Material Output'
            node_output.location = 0, 0

            try:
                texture_BaseColor = bpy.data.images.load(filepath_B, check_existing=True)
                texture_Normal = bpy.data.images.load(filepath_N, check_existing=True)
                texture_Roughness = bpy.data.images.load(filepath_R, check_existing=True)
                texture_Metalness = bpy.data.images.load(filepath_M, check_existing=True)


                node_baseColor.image = texture_BaseColor
                node_normal.image = texture_Normal
                node_roughness.image = texture_Roughness
                node_metallic.image = texture_Metalness

            except:
                print("1111  Unexpected error:" + str(sys.exc_info()[0]))

            try:
                texture_IOR = bpy.data.images.load(filepath_IOR, check_existing=True)
                node_ior.image = texture_IOR
            except:
                print("2222  Unexpected error:" +  str(sys.exc_info()[0]))

            # link nodes
            links = mat.node_tree.links
            link = links.new(node_principled.outputs[0], node_output.inputs[0])
            if self.my_basecolor:
                link = links.new(node_baseColor.outputs[0], node_principled.inputs[0])
            if self.my_roughness:
                link = links.new(node_roughness.outputs[0], node_principled.inputs[7])
            if self.my_metallic:
                link = links.new(node_metallic.outputs[0], node_principled.inputs[4])
            if self.my_normal:
                link = links.new(node_normal.outputs[0], node_normalMap.inputs[1])
                link = links.new(node_normalMap.outputs[0], node_principled.inputs['Normal'])

        bpy.context.area.type = areaType

        return {"FINISHED"}