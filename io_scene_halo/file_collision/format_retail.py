# ##### BEGIN MIT LICENSE BLOCK #####
#
# MIT License
#
# Copyright (c) 2022 Steven Garcia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ##### END MIT LICENSE BLOCK #####

from mathutils import Vector

class CollisionAsset():
    def __init__(self):
        self.header = None
        self.coll_body = None
        self.materials = []
        self.regions = []
        self.pathfinding_spheres = []
        self.nodes = []

    class CollBody:
        def __init__(self, flags=0, indirect_damage_material=0, maximum_body_vitality=0.0, body_system_shock=0.0, friendly_damage_resistance=0.0, localized_damage_effect=None,
                     area_damage_effect_threshold=0.0, area_damage_effect=None, body_damaged_threshold=0.0, body_damaged_effect=None, body_depleted_effect=None,
                     body_destroyed_threshold=0.0, body_destroyed_effect=None, maximum_shield_vitality=0.0, shield_material_type=0, shield_failure_function=0,
                     shield_failure_threshold=0.0, shield_failing_leak_fraction=0.0, minimum_stun_damage=0.0, stun_time=0.0, recharge_time=0.0, shield_damaged_threshold=0.0,
                     shield_damaged_effect=None, shield_depleted_effect=None, shield_recharging_effect=None, shield_recharge_rate=0.0, materials_tag_block=None,
                     regions_tag_block=None, modifiers_tag_block=None, pathfinding_box=Vector(), pathfinding_spheres_tag_block=None, nodes_tag_block=None):
            self.flags = flags
            self.indirect_damage_material = indirect_damage_material
            self.maximum_body_vitality = maximum_body_vitality
            self.body_system_shock = body_system_shock
            self.friendly_damage_resistance = friendly_damage_resistance
            self.localized_damage_effect = localized_damage_effect
            self.area_damage_effect_threshold = area_damage_effect_threshold
            self.area_damage_effect = area_damage_effect
            self.body_damaged_threshold = body_damaged_threshold
            self.body_damaged_effect = body_damaged_effect
            self.body_depleted_effect = body_depleted_effect
            self.body_destroyed_threshold = body_destroyed_threshold
            self.body_destroyed_effect = body_destroyed_effect
            self.maximum_shield_vitality = maximum_shield_vitality
            self.shield_material_type = shield_material_type
            self.shield_failure_function = shield_failure_function
            self.shield_failure_threshold = shield_failure_threshold
            self.shield_failing_leak_fraction = shield_failing_leak_fraction
            self.minimum_stun_damage = minimum_stun_damage
            self.stun_time = stun_time
            self.recharge_time = recharge_time
            self.shield_damaged_threshold = shield_damaged_threshold
            self.shield_damaged_effect = shield_damaged_effect
            self.shield_depleted_effect = shield_depleted_effect
            self.shield_recharging_effect = shield_recharging_effect
            self.shield_recharge_rate = shield_recharge_rate
            self.materials_tag_block = materials_tag_block
            self.regions_tag_block = regions_tag_block
            self.modifiers_tag_block = modifiers_tag_block
            self.pathfinding_box = pathfinding_box
            self.pathfinding_spheres_tag_block = pathfinding_spheres_tag_block
            self.nodes_tag_block = nodes_tag_block

    class Materials:
        def __init__(self, name="", flags=0, material_type=0, shield_leak_percentage=0.0, shield_damage_multiplier=0.0, body_damage_multiplier=0.0):
            self.name = name
            self.flags = flags
            self.material_type = material_type
            self.shield_leak_percentage = shield_leak_percentage
            self.shield_damage_multiplier = shield_damage_multiplier
            self.body_damage_multiplier = body_damage_multiplier

    class Regions:
        def __init__(self, name="", flags=0, damage_threshold=0, destroyed_effect=None, permutation_tag_block=None, permutations=[]):
            self.name = name
            self.flags = flags
            self.damage_threshold = damage_threshold
            self.destroyed_effect = destroyed_effect
            self.permutation_tag_block = permutation_tag_block
            self.permutations = permutations

    class Permutations:
        def __init__(self, name=""):
            self.name = name

    class PathfindingSphere:
        def __init__(self, node=0, center=Vector(), radius=0.0):
            self.node = node
            self.center = center
            self.radius = radius

    class Nodes:
        def __init__(self, name="", region=0, parent=0, sibling=0, child=0, unknown_0=0, unknown_1=0, bsps_tag_block=None, bsps=[]):
            self.name = name
            self.region = region
            self.parent = parent
            self.sibling = sibling
            self.child = child
            self.unknown_0 = unknown_0
            self.unknown_1 = unknown_1
            self.bsps_tag_block = bsps_tag_block
            self.bsps = bsps

    class BSP:
        def __init__(self, bsp3d_nodes_tag_block=None, planes_tag_block=None, leaves_tag_block=None, bsp2d_references_tag_block=None, bsp2d_nodes_tag_block=None,
                     surfaces_tag_block=None, edges_tag_block=None, vertices_tag_block=None, bsp3d_nodes=[], planes=[], leaves=[], bsp2d_references=[],
                     bsp2d_nodes=[], surfaces=[], edges=[], vertices=[]):
            self.bsp3d_nodes_tag_block = bsp3d_nodes_tag_block
            self.planes_tag_block = planes_tag_block
            self.leaves_tag_block = leaves_tag_block
            self.bsp2d_references_tag_block = bsp2d_references_tag_block
            self.bsp2d_nodes_tag_block = bsp2d_nodes_tag_block
            self.surfaces_tag_block = surfaces_tag_block
            self.edges_tag_block = edges_tag_block
            self.vertices_tag_block = vertices_tag_block
            self.bsp3d_nodes = bsp3d_nodes
            self.planes = planes
            self.leaves = leaves
            self.bsp2d_references = bsp2d_references
            self.bsp2d_nodes = bsp2d_nodes
            self.surfaces = surfaces
            self.edges = edges
            self.vertices = vertices

    class BSP3DNode:
        def __init__(self, plane=0, back_child=0, front_child=0):
            self.plane = plane
            self.back_child = back_child
            self.front_child = front_child

    class Plane:
        def __init__(self, translation=Vector(), distance=0.0):
            self.translation = translation
            self.distance = distance

    class Leaf:
        def __init__(self, flags=0, bsp2d_reference_count=0, first_bsp2d_reference=0):
            self.flags = flags
            self.bsp2d_reference_count = bsp2d_reference_count
            self.first_bsp2d_reference = first_bsp2d_reference

    class BSP2DReference:
        def __init__(self, plane=0, bsp2d_node=0):
            self.plane = plane
            self.bsp2d_node = bsp2d_node

    class BSP2DNode:
        def __init__(self, plane_i=0.0, plane_j=0.0, distance=0.0, left_child=0, right_child=0):
            self.plane_i = plane_i
            self.plane_j = plane_j
            self.distance = distance
            self.left_child = left_child
            self.right_child = right_child

    class Surface:
        def __init__(self, plane=0, first_edge=0, flags=0, breakable_surface=0, material=0):
            self.plane = plane
            self.first_edge = first_edge
            self.flags = flags
            self.breakable_surface = breakable_surface
            self.material = material

    class Edge:
        def __init__(self, start_vertex=0, end_vertex=0, forward_edge=0, reverse_edge=0, left_surface=0, right_surface=0):
            self.start_vertex = start_vertex
            self.end_vertex = end_vertex
            self.forward_edge = forward_edge
            self.reverse_edge = reverse_edge
            self.left_surface = left_surface
            self.right_surface = right_surface

    class Vertex:
        def __init__(self, translation=Vector(), first_edge=0):
            self.translation = translation
            self.first_edge = first_edge
