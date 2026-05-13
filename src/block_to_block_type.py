from block_type import BlockType


def block_to_block_type(block: str) -> BlockType:
    if not block:
        return BlockType.PARAGRAPH

    lines = block.split("\n")

    if block.startswith("#") and len(block) > 1:
        hash_count = 0
        for char in block:
            if char == "#":
                hash_count += 1
            else:
                break
        if 1 <= hash_count <= 6 and block[hash_count] == " ":
            return BlockType.HEADING

    if block.startswith("```") and block.endswith("```") and len(block) >= 6:
        return BlockType.CODE

    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if lines and lines[0].strip().startswith("1. "):
        is_ordered = True
        for i, line in enumerate(lines):
            expected = f"{i+1}. "
            if not line.strip().startswith(expected):
                is_ordered = False
                break
        if is_ordered:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH