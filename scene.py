import logging
from math import radians
from random import uniform

import bpy
from mathutils import Euler, Vector, Color

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def update_scene(scene):
    """Update the scene before rendering."""

    LOGGER.info("Hello!")

    cube = scene.objects["Cube"]

    rotation_vector = (uniform(0, 360),
                       uniform(0, 360),
                       uniform(0, 360))

    rotation_vector_radians = (radians(scalar) for scalar in rotation_vector)

    rotation_euler_angles = Euler(rotation_vector_radians, 'XYZ')

    cube.rotation_euler.rotate(rotation_euler_angles)

    cube.scale.x = cube.scale.y = cube.scale.z = uniform(1, 3)

    # Equivalent to:
    # cube.scale = Vector(3 * [uniform(1, 3)])

    cube.location.x = uniform(-2, 2)
    cube.location.y = uniform(-2, 2)
    cube.location.z = uniform(-2, 2)

    # Equivalent to
    # cube.location = Vector((uniform(-2, 2),
    #                        uniform(-2, 2),
    #                        uniform(-2, 2)))

    cube.active_material.diffuse_color.h = uniform(0, 1)
    cube.active_material.diffuse_color.s = uniform(.8, 1)
    cube.active_material.diffuse_color.v = uniform(.8, 1)

    for vertex in cube.data.vertices:
        vertex.co = Vector((vertex.co[0] + uniform(0, 0.1),
                            vertex.co[1] + uniform(0, 0.1),
                            vertex.co[2] + uniform(0, 0.1)))

    cube.data.materials[0].diffuse_shader = "TOON"


if __name__ == "__main__":
    bpy.context.scene.render.resolution_x = 800
    bpy.context.scene.render.resolution_y = 800

    camera = bpy.data.objects["Camera"]
    camera.location = Vector((0, 0, 20))
    camera.rotation_euler = Euler((0, 0, radians(90)))

    lamp = bpy.data.objects["Lamp"]
    lamp.data.type = "HEMI"
    lamp.data.energy = 8

    world = bpy.data.worlds["World"]
    world.horizon_color = Color((0.8, 0.8, 0.8))
    world.horizon_color = Color((0.01, 0.01, 0.01))

    bpy.app.handlers.frame_change_pre.append(update_scene)
