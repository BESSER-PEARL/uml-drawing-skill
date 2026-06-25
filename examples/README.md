# Examples

Five ready-to-render B-UML class models, one per feature the `uml-drawing`
skill handles. Each file is a complete, `validate()`-checked
[BESSER](https://github.com/BESSER-PEARL/BESSER) `DomainModel`.

| File | Demonstrates |
|------|--------------|
| [`ecommerce.py`](ecommerce.py) | associations · 1..1 / 0..\* / 1..\* multiplicities · composition |
| [`vehicles.py`](vehicles.py)   | multi-level inheritance · abstract superclass |
| [`tasks.py`](tasks.py)         | enumeration as an attribute type · composition |
| [`org.py`](org.py)             | self-referential association (manages / managedBy) |
| [`enroll.py`](enroll.py)       | association class (attribute on the link) |

Two of them ship with their rendered output for reference —
[`vehicles.svg`](vehicles.svg) and [`tasks.svg`](tasks.svg) — each produced by
the one-call command below, straight from the matching `.py`.

## Render one to an image

No browser, no install — one HTTP call to BESSER's headless `B-UML → SVG`
endpoint:

```bash
curl -X POST https://editor.besser-pearl.org/besser_api/get-svg \
  -F "buml_file=@vehicles.py;type=text/x-python" \
  -o vehicles.svg
```

Then embed it: `![Vehicles](vehicles.svg)`.

## Or generate code from the same model

These are real B-UML models, so the very same file can drive any BESSER
generator (Python, SQL, FastAPI, Django, React, …) — see the
[besser-generators](https://github.com/BESSER-PEARL/besser-skills) skill.
