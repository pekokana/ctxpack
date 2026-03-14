import argparse

from .collector import collect_files
from .writer import write_output


def main():

    parser = argparse.ArgumentParser(
        description="Combine source files for AI context"
    )

    parser.add_argument("target", help="file or directory")

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="output file"
    )

    parser.add_argument(
        "-e",
        "--ext",
        help="target extensions (comma separated)"
    )

    parser.add_argument(
        "--max-size",
        type=int,
        help="max file size (KB)"
    )

    parser.add_argument(
        "--max-files",
        type=int,
        help="maximum number of files"
    )

    parser.add_argument(
        "--tree",
        action="store_true",
        help="include project tree"
    )

    parser.add_argument(
        "--gitignore",
        action="store_true",
        help="respect .gitignore"
    )

    parser.add_argument(
        "--estimate-tokens",
        action="store_true",
        help="estimate tokens"
    )

    parser.add_argument(
        "--token-output",
        action="store_true",
        help="write token estimate to file"
    )

    parser.add_argument(
        "--llm-format",
        action="store_true",
        help="use LLM optimized format"
    )

    args = parser.parse_args()

    extensions = None

    if args.ext:
        extensions = [e.strip() for e in args.ext.split(",")]

    files = collect_files(
        args.target,
        extensions,
        args.max_size,
        args.max_files,
        args.gitignore
    )

    tokens = write_output(
        files,
        args.output,
        root=args.target,
        show_tree=args.tree,
        include_tokens=args.token_output,
        llm_format=args.llm_format
    )

    print(f"Packed files: {len(files)}")
    print(f"Output: {args.output}")

    if args.estimate_tokens:
        print(f"Estimated tokens: {tokens}")