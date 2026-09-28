# DesignForge MCP architecture

## Overview

DesignForge connects three major layers:

1. A Python-based MCP server for direct CAD and model operations.
2. A Java-based orchestration service for API access, scheduling, and task storage.
3. A design workflow that supports generation, validation, export, and version tracking.

## Flow

- a client submits a request through MCP or REST
- Python tools interpret the task and invoke CAD operations or local generation logic
- Java coordinates metadata, tasks, and web integration
- the system returns generated design artifacts and summaries

## Key concepts

- sessions: temporal design workspaces
- tasks: generated actions or requests
- exports: STL/STEP/OBJ/PNG deliverables
- versions: design snapshots and iteration history
