# Code execution

DesignForge MCP follows a layered execution model. The Python MCP layer handles direct tool calls, while the Java service manages orchestration and task lifecycle.

## Execution model

### 1. MCP tool execution

When a client invokes an MCP tool, the Python server executes the requested action in-process. For example:

```python
from design_forge.server import generate_parametric_model

result = generate_parametric_model(
    model_name="bearing_support",
    dimensions={"length": 45.0, "radius": 18.0}
)
```

### 2. Java orchestration

The Java API can receive REST calls for task metadata and status tracking.

Example endpoint:

```http
GET /api/design
POST /api/design
GET /api/design/{id}
```

### 3. CAD-generation bridge

When a real CAD runtime is connected, the Python layer can hand off generation tasks to the FreeCAD bridge or another model engine.

## Background jobs

For long-running operations, the Python layer can be extended to support:

- async generation tasks
- worker-thread execution
- queued geometry operations
- progress status polling
- failure tracebacks

A design flow could look like:

```text
client request -> python tool -> queue task -> java status endpoint -> result export
```

## Recommended patterns

- Keep all direct CAD operations in the Python layer.
- Keep lifecycle state, user identity, and project metadata in Java.
- Store export artifacts and design metadata in a database.
- Use the Java layer for API exposure and auditability.

## Timeout and reliability guidance

For real geometry generation and FEM workloads:

- use queueing for long-running tasks
- keep a clear job ID and status endpoint
- surface exceptions with traceback data
- avoid running GUI-blocking tasks from the main API thread

This mirrors the robust design model used by the original FreeCAD MCP project, but it is applied in a more service-oriented architecture.
