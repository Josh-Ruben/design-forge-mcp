# DesignForge MCP

A hybrid design-automation platform inspired by the original FreeCAD MCP project, but extended with a Python-first MCP layer and a Java orchestration service for real-world engineering workflows.

This project is designed for AI assistants and engineering agents that need to:

- create and manage CAD design sessions
- execute parametric design logic
- inspect and validate models
- generate export artifacts
- orchestrate engineering tasks via Java APIs
- integrate with CAD runtimes, simulations, and downstream automation

## Demo

The original project demonstrates the kind of design workflow this stack is intended to support:

![Designing a flange in FreeCAD](https://raw.githubusercontent.com/neka-nat/freecad-mcp/main/assets/freecad_mcp4.gif)

## Architecture

DesignForge MCP is intentionally dual-layered:

- Python service: MCP server, model generation, FreeCAD bridge integration, local execution
- Java service: REST API, orchestration, task lifecycle, persistence-ready backend
- Shared workflow: request -> validate -> generate -> simulate -> export -> version

## Repository layout

- `python/` — Python MCP server and tool implementations
- `java/` — Java Spring Boot orchestration API
- `docs/` — installation, configuration, tools, execution, examples
- `examples/` — sample scripts and design workflows
- `scripts/` — local setup helpers

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

## What makes this project different from the original FreeCAD MCP

This project keeps the same overall mission—AI-driven CAD design—but adds:

- Java-based orchestration and REST API
- project/session/task tracking
- export lifecycle and artifact metadata
- parametric design templates
- orchestration between clients and independent services
- a path toward enterprise automation, persistence, and workflow integration

## Documentation

| Guide | Contents |
| --- | --- |
| [Installation](docs/installation.md) | Setup for Python, Java, and optional CAD integration |
| [Configuration](docs/configuration.md) | Environment variables, ports, client config, security |
| [Tools](docs/tools.md) | Available MCP tools and their purpose |
| [Code execution](docs/execution.md) | Execution modes, async jobs, and orchestration patterns |
| [Demos and examples](docs/examples.md) | Example workflows, design scripts, and inspiration |

## Current capabilities

The Python MCP server includes these tools:

- `create_design_session`
- `generate_parametric_model`
- `inspect_model`
- `export_design`

The Java service includes a REST API for designing tasks and managing design metadata.

## Roadmap

Planned extensions include:

- FreeCAD native bridge and geometry operations
- PostgreSQL persistence layer
- design version history and snapshots
- FEM/simulation integration
- frontend dashboard with React or Next.js
- authentication and RBAC
- artifact storage and BOM generation

## License

MIT
