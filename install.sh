#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="saas-audit"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="user"

usage() {
  cat <<'EOF'
Install the SaaS Audit Agent Skill.

Usage:
  ./install.sh             Install for the current user
  ./install.sh --project   Install into the current project

Environment:
  HERMES_SKILLS_DIR        Optional Hermes skills destination
EOF
}

for arg in "$@"; do
  case "$arg" in
    --project) MODE="project" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $arg" >&2; usage >&2; exit 2 ;;
  esac
done

copy_skill() {
  local destination="$1"
  mkdir -p "$(dirname "$destination")"
  rm -rf "$destination"
  mkdir -p "$destination"

  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude '.git/' \
      --exclude '.github/' \
      --exclude 'saas-audit-output/' \
      "$SOURCE_DIR/" "$destination/"
  else
    cp -R "$SOURCE_DIR/." "$destination/"
    rm -rf "$destination/.git" "$destination/.github" "$destination/saas-audit-output"
  fi
  printf 'Installed: %s\n' "$destination"
}

if [[ "$MODE" == "project" ]]; then
  destinations=(
    "$PWD/.agents/skills/$SKILL_NAME"
    "$PWD/.claude/skills/$SKILL_NAME"
    "$PWD/.github/skills/$SKILL_NAME"
  )
else
  destinations=(
    "$HOME/.agents/skills/$SKILL_NAME"
    "$HOME/.claude/skills/$SKILL_NAME"
  )
fi

if [[ -n "${HERMES_SKILLS_DIR:-}" ]]; then
  destinations+=("${HERMES_SKILLS_DIR%/}/$SKILL_NAME")
fi

for destination in "${destinations[@]}"; do
  copy_skill "$destination"
done

cat <<'EOF'

SaaS Audit installed successfully.
Restart or reload your AI coding client, then ask:

Use the saas-audit skill to audit this repository and issue a release verdict.
EOF
