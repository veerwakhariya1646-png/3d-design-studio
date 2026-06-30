# 3D Design Studio

![3D Design Studio preview](assets/preview.png)

A small 3D scene builder, available in two editions: a browser-based app and a pure Python script.

## Web edition (`3d-design-studio.html`)

Built with [three.js](https://threejs.org/). Place primitive shapes (box, sphere, cylinder, cone, torus, capsule), move/rotate/scale them with an on-screen gizmo, recolor from a palette, and adjust position numerically.

**Run it:** just open `3d-design-studio.html` in any modern browser. No install, no server.

## Python edition (`3d_design_app.py`)

Built with `matplotlib`. Define a scene as a list of shapes and positions in code, then render an interactive, rotatable 3D view.

**Run it:**
```bash
pip install -r requirements.txt
python 3d_design_app.py
```

Edit the `demo_scene()` function to design your own layout.

## Project structure
