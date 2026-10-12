"""Scaffold a new numbered project folder.

Usage:
    python new_project.py "number guessing game"
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PROJECTS = ROOT / "projects"
README = ROOT / "README.md"

MAIN_TEMPLATE = '''"""{title}."""


def main() -> None:
    print("{title} - let's build it!")


if __name__ == "__main__":
    main()
'''

TEST_TEMPLATE = """from main import main


def test_main_runs(capsys):
    main()
    assert "{title}" in capsys.readouterr().out
"""

README_TEMPLATE = """# {title}

## What it does
Describe the project in one or two sentences.

## How to run
```bash
python main.py
pytest
```

## What I learned
- ...
"""


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def next_number() -> int:
    numbers = [int(p.name[:2]) for p in PROJECTS.glob("[0-9][0-9]-*") if p.is_dir()]
    return max(numbers, default=0) + 1


def add_to_progress_table(number: str, slug: str) -> None:
    text = README.read_text(encoding="utf-8")
    row = f"| {number} | [{slug}](projects/{number}-{slug}) | ... | 🚧 In progress |\n"
    text = text.replace("<!-- PROGRESS:END -->", row + "<!-- PROGRESS:END -->")
    README.write_text(text, encoding="utf-8")


def create_project(name: str) -> Path:
    slug = slugify(name)
    if not slug:
        raise ValueError("Project name must contain letters or numbers.")
    number = f"{next_number():02d}"
    folder = PROJECTS / f"{number}-{slug}"
    folder.mkdir(parents=True)

    title = name.strip().capitalize()
    (folder / "main.py").write_text(MAIN_TEMPLATE.format(title=title), encoding="utf-8")
    (folder / "test_main.py").write_text(TEST_TEMPLATE.format(title=title), encoding="utf-8")
    (folder / "README.md").write_text(README_TEMPLATE.format(title=title), encoding="utf-8")
    add_to_progress_table(number, slug)
    return folder


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Usage: python new_project.py "project name"')
    path = create_project(sys.argv[1])
    print(f"Created {path.relative_to(ROOT)}")
