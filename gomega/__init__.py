"""OMEGA - Optimised Modelling of Groundwater in Australia.

A utility package for generating extruded meshes and loading spatial data
for the G-ADOPT groundwater module.

Example:
    >>> from gomega import SurfaceMesh, build_mesh_hierarchy, GaussianKernelSurface
    >>> from gomega.geometry import Polygon
    >>> polygon = Polygon([(0, 0), (280000, 0), (280000, 130000), (0, 130000)])
    >>> sm = SurfaceMesh(polygon, resolution=3500)
    >>> sm.generate()
    >>> mesh_2d = sm.to_firedrake_mesh()
    >>> top = GaussianKernelSurface(elev_coords, elev_values, sigma=5000)
    >>> thickness = GaussianKernelSurface(depth_coords, depth_values, sigma=5000)
    >>> hierarchy = build_mesh_hierarchy(
    ...     mesh_2d, top, thickness.clamp_min(5.0), n_layers=300,
    ... )
"""

from gomega.exceptions import (
    DataLoadError,
    InterpolationError,
    MeshGenerationError,
    OmegaError,
    PolygonError,
)
from gomega.fields import (
    FieldInterpolator,
    GaussianKernelSurface,
    GridSurface,
    IntervalObservations,
    LayerModel,
    Surface,
    assign_field,
    clamp_monotonic,
    node_coordinates,
)
from gomega.geometry import LocalFrame, Polygon
from gomega.mesh import ExtrusionConfig, SurfaceMesh, build_mesh_hierarchy

__version__ = "0.1.0"

__all__ = [
    # Main API
    "SurfaceMesh",
    "build_mesh_hierarchy",
    "Polygon",
    "LocalFrame",
    "ExtrusionConfig",
    # Surfaces: kernel regression for scattered picks, linear for dense grids
    "Surface",
    "GaussianKernelSurface",
    "GridSurface",
    "clamp_monotonic",
    # Fields and layered models
    "FieldInterpolator",
    "IntervalObservations",
    "LayerModel",
    "assign_field",
    "node_coordinates",
    # Exceptions
    "OmegaError",
    "PolygonError",
    "MeshGenerationError",
    "InterpolationError",
    "DataLoadError",
]
