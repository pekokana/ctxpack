from .reader import read_file
from .tree import build_tree
from .token import estimate_tokens


def detect_language(path):

    mapping = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".java": "java",
        ".go": "go",
        ".rs": "rust",
        ".c": "c",
        ".cpp": "cpp",
        ".sh": "bash",
        ".md": "markdown",
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".html": "html",
        ".css": "css",
    }

    return mapping.get(path.suffix.lower(), "")


def write_output(
    files,
    output_path,
    root=None,
    show_tree=False,
    include_tokens=False,
    llm_format=False
):

    total_tokens = 0

    with open(output_path, "w", encoding="utf-8") as out:

        if show_tree and root:

            tree = build_tree(files, root)

            out.write("# Project Structure\n\n")
            out.write("```\n")
            out.write(tree)
            out.write("\n```\n\n")

        for file in files:

            content = read_file(file)

            if content is None:
                continue

            lang = detect_language(file)

            if llm_format:
                out.write(f"=== FILE: {file} ===\n\n")
            else:
                out.write(f"# {file}\n\n")

            out.write(f"```{lang}\n")
            out.write(content)
            out.write("\n```\n\n")

            total_tokens += estimate_tokens(content)

        if include_tokens:
            out.write("\n---\n")
            out.write(f"Estimated tokens: {total_tokens}\n")

    return total_tokens