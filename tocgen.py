import re
import sys
from pathlib import Path

TOC_START = "<!-- TOC START -->"
TOC_END = "<!-- TOC END -->"

def slugify(text):
    """Converts a header into a GitHub-style anchor link."""
    slug = re.sub(r'[^\w\s-]', '', text).lower()
    slug = re.sub(r'\s+', '-', slug).strip('-')
    return slug

def generate_toc(lines):
    toc_lines = [TOC_START]
    for line in lines:
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            anchor = slugify(title)
            indent = '  ' * (level - 1)
            toc_lines.append(f"{indent}- [{title}](#{anchor})")
    toc_lines.append(TOC_END)
    return '\n'.join(toc_lines) + '\n'

def update_markdown_with_toc(filepath):
    content = Path(filepath).read_text(encoding='utf-8')
    
    # Remove existing TOC block if present
    toc_pattern = re.compile(
        rf"{TOC_START}.*?{TOC_END}\n?", re.DOTALL)
    content_wo_toc = re.sub(toc_pattern, '', content).lstrip()

    lines = content_wo_toc.splitlines()
    toc = generate_toc(lines)

    # Prepend new TOC
    new_content = toc + '\n' + content_wo_toc
    Path(filepath).write_text(new_content, encoding='utf-8')
    print(f"✅ TOC updated in: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_toc.py <file.md>")
        sys.exit(1)

    md_file = sys.argv[1]
    if not Path(md_file).is_file():
        print(f"❌ File not found: {md_file}")
        sys.exit(1)

    update_markdown_with_toc(md_file)

