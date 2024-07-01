## Repo setup

Explain steps to run code locally here

## Additional setup

### Update the following parameters in the `pyproject.toml` file.

Uncomment the following lines and add your package dependencies.
Where possible, please add `~=` instead of `==`

```
#dependencies = [
#    "package~=3.17.0",
#    "package2~=3.15.1",
#]
```

## Formatting

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
