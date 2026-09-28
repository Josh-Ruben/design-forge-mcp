# DesignForge MCP

A full-stack, AI-powered design automation platform inspired by the original FreeCAD MCP project, but expanded with a Python-first Model Context Protocol server and a Java orchestration layer for enterprise automation.

This project is designed to help AI assistants and engineering agents:

- create and edit CAD models
- run parametric design workflows
- inspect assemblies and document structures
- trigger FEM/simulation jobs
- export STEP/STL/OBJ and reports
- manage design sessions, version history, and bill of materials (BOM)
- coordinate Python and Java services in a unified workflow

## Architecture

DesignForge MCP is intentionally hybrid:

- Python service: MCP server for CAD operations, local execution, and model inspection
- Java service: REST API, orchestration, task management, auth-ready integration, and admin tooling
- Shared design pipeline: model specification -> validation -> generation -> simulation -> export

## Repository layout

- `python/` — MCP server and CAD integration code
- `java/` — Java Spring Boot service and REST API
- `docs/` — architecture, usage, and workflow notes
- `scripts/` — local dev helpers

## Quick start

### 1) Python MCP server

```bash
cd python
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
python -m design_forge.server
```

### 2) Java service

```bash
cd java
./mvnw clean package
java -jar target/designforge-java-0.1.0.jar
```

### 3) Example MCP client config

```json
{
  "mcpServers": {
    "designforge": {
      "command": "python",
      "args": ["-m", "design_forge.server"]
    }
  }
}
```

## New features beyond the original project

- Java REST orchestration layer for design tasks
- project and session metadata tracking
- parametric design templates and reusable model recipes
- CAD operation validation and safety checks
- BOM and assembly summary generation
- export pipeline for STL/STEP/OBJ and reports
- design history snapshots and version tagging
- integration-ready API for frontend or agent systems

## Typical workflow

1. A user or AI agent submits a design request.
2. The Python MCP server communicates with the CAD runtime or FreeCAD bridge.
3. The Java service validates tasks, stores metadata, and exposes APIs.
4. The system executes generation and simulation steps.
5. Assets are exported and saved with project-version metadata.

## License

MIT
