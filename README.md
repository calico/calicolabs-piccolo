# Piccolo

#### 

Piccolo provides tools for droplet processing instruments:

1. Generate test data of droplets in microfluidic fluorescence-activated droplet sorter 
2. Display and interact with test data across different channels and set sorting gates in a UI


---

#### Contacts

Kendra Nyberg (codeowner)
Calico Life Sciences LLC


---

#### Quickstart

Run with `bokeh serve --show ui_layout.py`


---

#### Dependencies

[project]
name = "calicolabs-piccolo"
description = "Python Library for piccolo"
authors = [
    {name = "Kendra Nyberg", email = "nyberg@calicolabs.com"},
]
readme = "README.md"
classifiers = ["License :: Apache 2.0"]
dynamic = ["version"]

requires-python = ">=3.8.5"
dependencies = [
    "numpy~=1.24.4",
    "bokeh~=3.1.1",
]

[project.optional-dependencies]
dev = [
    "black~=23.12.1",
    "pytest~=7.4.4",
    "ruff~=0.1.11",
]

[project.urls]
Homepage = "https://github.com/calico/piccolo"
"Bug Tracker" = "https://github.com/calico/piccolo/issues"

[tool.setuptools_scm]

### Prettier

- Install and run `prettier` to maintain consistent YAML/Markdown/JSON formatting.
  - In repo root: `npm install prettier@3.2.4`
  - Reformat repo after changes: `npx prettier --write .`

### Black

- Install and run `black` to maintain consistent Python formatting.
  - In repo root: `pip install black`
  - Reformat repo after changes: `black .`

### Ruff

- Install and run `ruff` to maintain consistent Python formatting.
  - In repo root: `pip install ruff`
  - Reformat repo after changes: `ruff check .`
