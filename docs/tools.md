# Configuration

This project supports local configuration for both the Python MCP server and the Java REST API.

## Python MCP settings

The Python server is configured through environment variables and the MCP client config.

### Example MCP client config

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

You can also set environment variables:

```json
{
  "mcpServers": {
    "designforge": {
      "command": "python",
      "args": ["-m", "design_forge.server"],
      "env": {
        "DESIGNFORGE_ENV": "development",
        "DESIGNFORGE_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

## Java API settings

The Java service uses Spring Boot defaults. You can override them in:

```properties
# java/src/main/resources/application.properties
server.port=8080
spring.application.name=designforge
logging.level.root=INFO
```

Example:

```properties
server.port=8080
spring.datasource.url=jdbc:postgresql://localhost:5432/designforge
spring.datasource.username=postgres
spring.datasource.password=postgres
spring.jpa.hibernate.ddl-auto=update
```

## Common environment variables

| Variable | Purpose |
| --- | --- |
| `DESIGNFORGE_ENV` | Runtime environment (`development`, `staging`, `production`) |
| `DESIGNFORGE_LOG_LEVEL` | Logging verbosity |
| `FREECAD_PATH` | Optional path to the FreeCAD executable |
| `FREECAD_MCP_TOKEN` | Optional auth token for secure remote access |
| `POSTGRES_URL` | Database connection string |

## Security guidance

If the system is exposed beyond localhost:

- use a secure token or authentication layer
- restrict allowed IP ranges
- avoid exposing raw FreeCAD execution endpoints publicly
- prefer an SSH tunnel or private network for remote access

## Local development example

```bash
export DESIGNFORGE_ENV=development
export DESIGNFORGE_LOG_LEVEL=DEBUG
export FREECAD_PATH="/usr/bin/freecad"
```

Then start the Python server and Java API separately.

## Ports

| Service | Default Port |
| --- | --- |
| Python MCP server | stdin/stdout over client channel |
| Java API | 8080 |
| PostgreSQL | 5432 |

## Remote connection model

The original FreeCAD MCP project exposes a remote RPC bridge and auth tokens. This repository follows a similar security philosophy:

- keep machine-to-machine connections private
- require tokens for network access
- never expose arbitrary code execution to the public internet
