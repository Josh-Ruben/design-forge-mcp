# Installation

This project is designed to be installed and run in two parts:

1. the Python MCP server
2. the Java orchestration API

For real CAD work, the Python layer can also be connected to a FreeCAD runtime or a FreeCAD-compatible bridge.

## Requirements

- Python 3.10+
- Java 21+
- Maven or Maven Wrapper
- Optional: FreeCAD installed locally
- Optional: uv for fast Python setup

## 1. Install the Python MCP server

From the repository root:

```bash
cd python
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

Start the server:

```bash
python -m design_forge.server
```

Or with the installed command:

```bash
designforge
```

## 2. Install the Java service

From the repository root:

```bash
cd java
./mvnw clean package
```

Run the service:

```bash
java -jar target/designforge-java-0.1.0.jar
```

The Java service exposes the REST API on the default Spring Boot port:

- http://localhost:8080

## 3. Optional: connect to FreeCAD

The original FreeCAD MCP project uses a FreeCAD addon and RPC server. This project follows the same broad architecture, but the FreeCAD integration is intentionally modular and can be added as a bridge layer.

A typical design flow is:

```text
MCP client -> Python MCP server -> FreeCAD bridge -> FreeCAD runtime
```

If your environment includes FreeCAD, the Python server can be extended to call:

- document creation
- geometric primitives
- assembly edits
- object inspection
- export to STEP/STL/OBJ
- FEM workflows

## 4. Local development workflow

From the repository root you can use:

```bash
make python
make java
```

Or run a single process directly:

```bash
docker-compose up --build
```

## 5. Troubleshooting

### Python package import errors

Verify the virtual environment is active and dependencies installed:

```bash
pip list
python -c "import design_forge; print('ok')"
```

### Java build failures

Check your Java version:

```bash
java -version
./mvnw -version
```

### Connection issues

Ensure the Python MCP server is running before trying to call tools from a client. Ensure the Java service is running before hitting the REST API endpoints.

## 6. Recommended environment

A typical professional setup is:

- Python MCP server for CAD automation
- Java API for orchestration and persistence
- PostgreSQL for long-term design metadata
- FreeCAD runtime for actual geometry generation
- React dashboard for visual design management
