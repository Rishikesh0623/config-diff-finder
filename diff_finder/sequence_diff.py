import difflib


def sequence_compare(file1, file2):

    lines1 = file1.read().decode("utf-8").splitlines()
    lines2 = file2.read().decode("utf-8").splitlines()

    diff = difflib.ndiff(lines1, lines2)

    result = []

    for line in diff:
        if line.startswith("- "):
            result.append({"type": "removed", "content": line[2:]})
        elif line.startswith("+ "):
            result.append({"type": "added", "content": line[2:]})
        elif line.startswith("  "):
            result.append({"type": "unchanged", "content": line[2:]})

    return result
