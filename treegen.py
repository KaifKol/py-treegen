import os
import argparse
import sys


def build_tree(path, file, prefix="", ignore=None, files_only=False, dirs_only=False):
    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        return

    if ignore:
        entries = [e for e in entries if e not in ignore]

    filtered = []
    for e in entries:
        full = os.path.join(path, e)
        if files_only and not os.path.isfile(full):
            continue
        if dirs_only and not os.path.isdir(full):
            continue
        filtered.append(e)

    for index, name in enumerate(filtered):
        full_path = os.path.join(path, name)
        is_last = index == len(filtered) - 1

        connector = "└── " if is_last else "├── "
        file.write(prefix + connector + name + "\n")

        if os.path.isdir(full_path) and not files_only:
            extension = "    " if is_last else "│   "
            build_tree(
                full_path,
                file,
                prefix + extension,
                ignore=ignore,
                files_only=files_only,
                dirs_only=dirs_only
            )


def main():
    parser = argparse.ArgumentParser(
        prog="treegen",
        description="Directory tree generator",
        epilog="""
Examples:
  treegen -p .
  treegen -p . -i .git,node_modules
  treegen -p D:\\Projects -o struct.txt
  treegen -p . -f
  treegen -p . -d
  treegen -p . -s
""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-p", "--path",
        help="Target directory (., *, or full path)"
    )

    parser.add_argument(
        "-o", "--out",
        default="tree.txt",
        help="Output file name (default: tree.txt)"
    )

    parser.add_argument(
        "-i", "--ignore",
        help="Comma-separated ignore list (.git,node_modules,...)"
    )

    parser.add_argument(
        "-f", "--files-only",
        action="store_true",
        help="Show only files"
    )

    parser.add_argument(
        "-d", "--dirs-only",
        action="store_true",
        help="Show only directories"
    )

    parser.add_argument(
        "-s", "--stdout",
        action="store_true",
        help="Print output to console instead of file"
    )

    # 👇 если запустили без аргументов — показываем help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if not args.path:
        print("Error: path must be specified (-p)\n")
        parser.print_help()
        sys.exit(1)

    root_path = os.path.abspath(args.path)

    if not os.path.isdir(root_path):
        print(f"Error: not a folder → {root_path}")
        sys.exit(1)

    ignore = args.ignore.split(",") if args.ignore else []

    title = os.path.basename(root_path.rstrip(os.sep)) or root_path
    header = title + "/\n"

    if args.stdout:
        sys.stdout.write(header)
        build_tree(
            root_path,
            sys.stdout,
            ignore=ignore,
            files_only=args.files_only,
            dirs_only=args.dirs_only
        )
    else:
        out_path = os.path.join(root_path, args.out)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(header)
            build_tree(
                root_path,
                f,
                ignore=ignore,
                files_only=args.files_only,
                dirs_only=args.dirs_only
            )
        print(f"Tree created: {out_path}")


if __name__ == "__main__":
    main()
