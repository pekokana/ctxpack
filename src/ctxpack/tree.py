from __future__ import annotations
from pathlib import Path


class TreeNode:
    """ツリー構造を表現するためのノードクラス"""

    def __init__(self, name: str, is_file: bool = False):
        self.name = name
        self.is_file = is_file
        self.children: dict[str, TreeNode] = {}


def build_tree(files, root) -> str:
    """
    ファイルパスのリストからLinuxのtreeコマンド風の美しいテキスト構造を生成します。
    """
    if not files:
        return ""

    root_path = Path(root)
    root_node = TreeNode(root_path.name or str(root_path))

    # 1. パスのリストから入れ子状のツリー構造（Trie）を構築
    for f in files:
        try:
            rel = f.relative_to(root_path)
        except ValueError:
            # ルート配下ではないファイルはスキップ
            continue

        current = root_node
        parts = rel.parts
        for i, part in enumerate(parts):
            is_last_part = i == len(parts) - 1
            if part not in current.children:
                current.children[part] = TreeNode(part, is_file=is_last_part)
            current = current.children[part]

    # 2. 再帰的に罫線を描画するヘルパー関数
    def render_node(node: TreeNode, prefix: str = "") -> list:
        lines = []

        # 見栄えを良くするため、ディレクトリを先、ファイルを後に並び替えてソート
        sorted_items = sorted(
            node.children.items(), key=lambda item: (item[1].is_file, item[0].lower())
        )

        count = len(sorted_items)
        for index, (name, child) in enumerate(sorted_items):
            is_last = index == count - 1

            # 最後の子ノードには └── を、それ以外には ├── を使用
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{name}")

            # 子ノードがさらに子供（サブディレクトリ）を持つ場合、再帰的に処理
            if child.children:
                # 最後の要素の下の階層なら空白インデント、途中の要素なら縦線付きインデント
                next_prefix = prefix + ("    " if is_last else "│   ")
                lines.extend(render_node(child, next_prefix))

        return lines

    # ルートノード配下の描画を開始
    tree_lines = render_node(root_node)
    return "\n".join(tree_lines)
