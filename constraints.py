from pathlib import Path

_root = Path(__file__).resolve().parent
_constraints = _root.parent / "constraints"
_content = _root / "content"

(_content / "boards").mkdir(exist_ok=True)

for item in (_constraints / "board").glob("**/*.yml"):

    if item.name != "info.yml":
        name = item.stem
        prefix = ".todo/"
        suffix = ".yml"
        print("·", name)
    else:
        name = item.parent.name
        prefix = ""
        suffix = ""
        print("-", name)

    with (_content / "boards" / (name + ".md")).open("w") as wfptr:
        wfptr.write("---\n")
        wfptr.write(item.read_text())
        wfptr.write(
            "ref: https://github.com/hdl/constraints/tree/main/board/%s%s%s\n"
            % (prefix, name, suffix)
        )
        wfptr.write("---\n")

for item in (_constraints / "board").glob("**/*.md"):

    if item.name != "README.md":
        name = item.stem
        prefix = ".todo/"
        suffix = ".md"
        print("·", name)
    else:
        name = item.parent.name
        prefix = ""
        suffix = ""
        print("-", name)

    with item.open("r") as rfptr:
        with (_content / "boards" / (name + ".md")).open("w") as wfptr:
            for line in [
                "---",
                "ref: https://github.com/hdl/constraints/tree/main/board/%s%s%s"
                % (prefix, name, suffix),
            ] + rfptr.read().splitlines()[1:]:
                wfptr.writelines("{}\n".format(line))
