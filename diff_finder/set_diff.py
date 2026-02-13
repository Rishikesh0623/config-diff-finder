def normalize(file_obj):
    lines = set()

    for line in file_obj:
        decoded = line.decode("utf-8").strip()
        if decoded:
            lines.add(decoded)

    return lines


def set_compare(file1, file2):
    lines1 = normalize(file1)
    lines2 = normalize(file2)

    added = sorted(lines2 - lines1)
    removed = sorted(lines1 - lines2)

    return {"added": added, "removed": removed}
