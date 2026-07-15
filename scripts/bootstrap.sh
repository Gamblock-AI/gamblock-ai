#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INSTALL=false

if [[ "${1:-}" == "--install" ]]; then
  INSTALL=true
elif [[ $# -gt 0 ]]; then
  echo "Usage: $0 [--install]" >&2
  exit 2
fi

cd "$ROOT_DIR"

if git rev-parse --show-toplevel >/dev/null 2>&1; then
  git submodule sync --recursive
  git submodule update --init --recursive
else
  echo "warning: umbrella Git metadata is not initialized; using existing component directories" >&2
fi

components=(
  "gamblock-ai-backend"
  "gamblock-ai-website"
  "gamblock_ai_apps"
  "browser_extension"
  "gamblock-ai-infrastructure"
)

for component in "${components[@]}"; do
  if [[ ! -d "$component" ]]; then
    echo "missing component directory: $component" >&2
    exit 1
  fi
done

for component in gamblock-ai-backend gamblock-ai-website gamblock_ai_apps; do
  if [[ -f "$component/.env.example" && ! -e "$component/.env" ]]; then
    cp "$component/.env.example" "$component/.env"
    echo "created $component/.env from .env.example"
  fi
done

if [[ "$INSTALL" == true ]]; then
  (cd gamblock-ai-backend && go mod download)
  (cd gamblock-ai-website && npm ci)
  (cd browser_extension && npm ci)
  (cd gamblock_ai_apps && flutter pub get)

  if [[ -f gamblock-ai-infrastructure/requirements.yml ]]; then
    (cd gamblock-ai-infrastructure && ansible-galaxy collection install -r requirements.yml)
  fi
fi

echo "workspace bootstrap complete"
if [[ "$INSTALL" == false ]]; then
  echo "run '$0 --install' to install component dependencies"
fi
