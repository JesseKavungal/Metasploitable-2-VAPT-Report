import re
from pathlib import Path

def test_readme_links_exist():
    repo_root = Path(__file__).resolve().parents[1]
    readme = repo_root / 'Readme.md'
    content = readme.read_text()
    links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', content)
    local_links = [l for l in links if not re.match(r'https?://', l)]
    for link in local_links:
        path = repo_root / link
        assert path.exists(), f"Missing file referenced in README: {link}"
