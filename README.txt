This is a simple converter written in Python to convert Google Keep notes into a JSON file accepted by the SimpleNote notes importer

This conversion performs the following operations:

- Convert all text notes.
- Converts checklists, retains checklist state (checked/unchecked).
- Converts Google Keep note creation date to SimpleNote format.

Future support:

- Convert and add labels.

Not supported:

- Images will not be converted or retained as SimpleNote does not currently support images except as external URL.