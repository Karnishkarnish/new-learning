def count_file_stats(filename):
    lines = 0
    words = 0
    characters = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)
        return lines, words, characters
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

file_name = input("Enter the filename: ")
result = count_file_stats(file_name)

if result:
    lines, words, characters = result
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {characters}")
