from pathlib import Path

def build_tree(files, root):

    root = Path(root)

    lines = []

    for f in files:

        rel = f.relative_to(root)

        depth = len(rel.parts) - 1

        indent = "  " * depth

        lines.append(f"{indent}{rel.name}")

    return "\n".join(lines)