import sys

def count_lines(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)
    except:
        print(f"Error: could not read file '{filename}'.")
        sys.exit(1)

    count = 0
    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue
        count += 1

    return count

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python lines.py <filename.py>')
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith('.py'):
        print(f"Error: file '{filename}' is not a Python file.")
        sys.exit(1)

    count = count_lines(filename)
    print(f"{filename}: {count} lines of code")
