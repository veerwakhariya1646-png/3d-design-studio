"""
3D Design Studio (Python edition)
----------------------------------
A small interactive 3D scene builder using matplotlib.
Add boxes, spheres, and cones to a scene, then rotate/zoom to inspect them.

Install dependencies:
    pip install matplotlib numpy

Run:
    python 3d_design_app.py
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (registers 3d projection)
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

PALETTE = ["#7c8cff", "#ff8c6b", "#6bd9a8", "#ffd166", "#f06bb0", "#b6b6c2"]


def make_box(center, size=1.0, color="#7c8cff"):
    """Return a Poly3DCollection cube centered at `center`."""
    cx, cy, cz = center
    s = size / 2
    # 8 corners of the cube
    corners = np.array([
        [cx - s, cy - s, cz - s], [cx + s, cy - s, cz - s],
        [cx + s, cy + s, cz - s], [cx - s, cy + s, cz - s],
        [cx - s, cy - s, cz + s], [cx + s, cy - s, cz + s],
        [cx + s, cy + s, cz + s], [cx - s, cy + s, cz + s],
    ])
    faces = [
        [corners[i] for i in [0, 1, 2, 3]],
        [corners[i] for i in [4, 5, 6, 7]],
        [corners[i] for i in [0, 1, 5, 4]],
        [corners[i] for i in [2, 3, 7, 6]],
        [corners[i] for i in [1, 2, 6, 5]],
        [corners[i] for i in [4, 7, 3, 0]],
    ]
    poly = Poly3DCollection(faces, facecolor=color, edgecolor="black", linewidths=0.4, alpha=0.95)
    return poly


def add_sphere(ax, center, radius=0.7, color="#6bd9a8"):
    u, v = np.mgrid[0:2 * np.pi:24j, 0:np.pi:14j]
    x = center[0] + radius * np.cos(u) * np.sin(v)
    y = center[1] + radius * np.sin(u) * np.sin(v)
    z = center[2] + radius * np.cos(v)
    ax.plot_surface(x, y, z, color=color, linewidth=0, alpha=0.95, shade=True)


def add_cone(ax, center, radius=0.7, height=1.4, color="#ffd166"):
    theta = np.linspace(0, 2 * np.pi, 30)
    z = np.linspace(0, height, 2)
    theta_grid, z_grid = np.meshgrid(theta, z)
    r_grid = radius * (1 - z_grid / height)
    x = center[0] + r_grid * np.cos(theta_grid)
    y = center[1] + r_grid * np.sin(theta_grid)
    zz = center[2] + z_grid
    ax.plot_surface(x, y, zz, color=color, linewidth=0, alpha=0.95, shade=True)


class Scene:
    """Holds the objects in the scene and knows how to render them."""

    def __init__(self):
        self.fig = plt.figure(figsize=(8, 7))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.objects = []  # list of (kind, center, color)

    def add(self, kind, center):
        color = PALETTE[len(self.objects) % len(PALETTE)]
        self.objects.append((kind, center, color))

    def render(self):
        self.ax.clear()
        self.ax.set_title("3D Design Studio", fontsize=13)
        for kind, center, color in self.objects:
            if kind == "box":
                self.ax.add_collection3d(make_box(center, size=1.2, color=color))
            elif kind == "sphere":
                add_sphere(self.ax, center, radius=0.75, color=color)
            elif kind == "cone":
                add_cone(self.ax, center, color=color)

        lim = 4
        self.ax.set_xlim(-lim, lim)
        self.ax.set_ylim(-lim, lim)
        self.ax.set_zlim(0, lim)
        self.ax.set_box_aspect([1, 1, 0.6])
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")

    def show(self):
        self.render()
        plt.tight_layout()
        plt.show()


def demo_scene():
    """Builds a small example layout. Edit this to design your own scene."""
    scene = Scene()
    scene.add("box", center=(-2, -2, 0.6))
    scene.add("sphere", center=(0, 0, 0.75))
    scene.add("cone", center=(2, 1.5, 0))
    scene.add("box", center=(2, -2, 0.6))
    scene.add("sphere", center=(-2, 2, 0.75))
    return scene


if __name__ == "__main__":
    scene = demo_scene()
    print(f"Rendering {len(scene.objects)} objects. Drag the plot window to rotate the camera.")
    scene.show()
