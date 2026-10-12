import os

def load_ascii(path):
    if not os.path.exists(path):
        print(f"File not found at '{path}'.")
        return None, 0, 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        height = len(lines)
        width = max(len(line) for line in lines)

        adjusted_lines = [line.ljust(width) for line in lines]
        one_line_data = "".join(adjusted_lines)

        return one_line_data, width, height
    
    except Exception as e:
        print(f"Unexpected Error: {e}")

    return None, 0, 0
