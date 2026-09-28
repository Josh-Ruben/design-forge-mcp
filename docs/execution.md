# Tools

The Python MCP server exposes a small but extensible set of CAD-oriented operations.

## Available tools

| Tool | Purpose |
| --- | --- |
| `create_design_session` | Create a new design session or project workspace |
| `generate_parametric_model` | Generate a parametric model specification with dimensions |
| `inspect_model` | Inspect a model and summarize components |
| `export_design` | Export a design to a supported format |

## Tool behavior

### `create_design_session`

Creates a new session ID and workspace metadata for a project.

Example:

```json
{
  "project_name": "bracket-assembly",
  "design_type": "mechanical"
}
```

### `generate_parametric_model`

Accepts a model name and a dimensions dictionary. This is useful for parametric design flows and downstream CAD generation.

Example:

```json
{
  "model_name": "mounting_bracket",
  "dimensions": {
    "length": 120.0,
    "width": 80.0,
    "height": 45.0
  }
}
```

### `inspect_model`

Returns summary metadata about a model, including components and warnings.

### `export_design`

Exports a model to a supported file format. Supported output formats include:

- `step`
- `stl`
- `obj`
- `png`

## Future tool additions

This project is intended to evolve toward advanced design operations such as:

- `create_document`
- `list_documents`
- `create_object`
- `edit_object`
- `delete_object`
- `execute_code`
- `execute_code_async`
- `run_fem_analysis`
- `get_view`
- `insert_part_from_library`

These are modeled after the original FreeCAD MCP tool set and can be implemented as the CAD bridge matures.
