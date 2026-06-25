# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - unreleased

Initial release of the `uml-drawing` skill.

### Added
- `uml-drawing` skill: build a correct UML **class diagram** through BESSER
  B-UML — from a description or from existing code the agent reads — and
  deliver it either as **embedded B-UML code** in a Markdown doc or as a
  **rendered SVG/PNG image**.
- **Automated image rendering** — the agent can produce the image itself with a
  single call to BESSER's headless `B-UML → SVG` endpoint
  (`POST /besser_api/get-svg`): no browser, no manual steps. A hand-tuned
  export from the [BESSER web editor](https://editor.besser-pearl.org) stays
  available for when the layout matters.
- Bundled [`references/class-diagram.md`](uml-drawing/references/class-diagram.md)
  — the full class-diagram metamodel reference (classes, attributes,
  enumerations, associations, association classes, generalizations,
  generalization sets, methods, validation).
- Scope is deliberately narrow for now: class diagrams only, always via
  BESSER B-UML.
- `.github/workflows/release.yml` — auto-creates a GitHub Release from the
  matching CHANGELOG section when a `v*` tag is pushed.
