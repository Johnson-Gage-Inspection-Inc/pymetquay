#!/usr/bin/env bash
# Regenerate the OpenAPI client from the spec with custom test templates.
# Usage: bash generate.sh

./.venv/Scripts/activate

set -euo pipefail

npx @openapitools/openapi-generator-cli generate \
  -i 1.0.json \
  -g python \
  --template-dir templates \
  --additional-properties=packageName=openapi_client \
  -o .

ruff check . --fix

isort .

black .
