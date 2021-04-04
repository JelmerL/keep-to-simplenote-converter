This is a simple converter written in Python to convert Google Keep notes into a JSON file accepted by the SimpleNote notes importer

--------------------------

This conversion performs the following operations:

- Convert all text notes.
- Converts checklists, retains checklist state (checked/unchecked).
- Converts Google Keep note creation date to ISO 8601 format.

Future support:

- Convert and add labels.
- Automatically enable markdown setting ON for notes with checkmarks, currently required to manually enable to be able to check/uncheck lines in simplenote

Not supported:

- Images will not be converted or retained as SimpleNote does not currently support images except as external URL.

-----------------------------------

How to:

1) Download your Google Keep notes using Google Takeout
2) Move the files inside Takeout\Keep into a folder called "Keep Files"
3) Copy converter.py in the folder above Keep Files
4) run converter.py
5) import your notes using the SimpleNotes importer as simplenote
