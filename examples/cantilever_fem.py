# Demos and examples

## Design demo

The original FreeCAD MCP example shows the style of interactive CAD design this project is intended to support:

![Designing a flange in FreeCAD](https://raw.githubusercontent.com/neka-nat/freecad-mcp/main/assets/freecad_mcp4.gif)

## Example project workflows

### 1. Parametric bracket design

Goal: generate a bracket model from a set of dimensions.

```python
from design_forge.server import generate_parametric_model

result = generate_parametric_model(
    model_name="wall_bracket",
    dimensions={
        "length": 120.0,
        "width": 80.0,
        "height": 30.0,
        "thickness": 5.0,
    }
)

print(result)
```

### 2. Design session creation

```python
from design_forge.server import create_design_session

session = create_design_session(
    project_name="pump_mount",
    design_type="mechanical"
)

print(session)
```

### 3. Export pipeline

```python
from design_forge.server import export_design

result = export_design("pump_mount", format_name="step")
print(result)
```

## Example script files

The repository includes starter examples in `examples/`.

### `examples/cantilever_fem.py`

This example demonstrates the style of a detailed design and analysis script, inspired by the original project’s FEM examples.

```python
"""Example: parametric model workflow for a simple bracket or cantilever style design."""

from design_forge.server import generate_parametric_model, export_design

model = generate_parametric_model(
    model_name="cantilever_demo",
    dimensions={
        "length": 200.0,
        "width": 30.0,
        "thickness": 8.0,
        "load": 1000.0,
    },
)

print(model)
print(export_design("cantilever_demo", format_name="step"))
```

## Future examples

This project is intended to support:

- FEM analysis examples
- CAD generation examples
- agent orchestration with LangChain or ADK
- dashboard-backed workflows
- 3D model preview and export history

## Inspiration source

This repository intentionally draws inspiration from the original FreeCAD MCP project and its robust documentation set, especially the installation, tool, execution, and example workflow structure.
