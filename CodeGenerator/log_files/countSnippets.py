def count_snippets(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        snippets = content.split("-----")
        # Filter out any empty strings that may occur from splitting
        snippets = [snippet for snippet in snippets if snippet.strip()]
        return len(snippets)

if __name__ == "__main__":
    valid_snippets_count = count_snippets('valid_py.txt')
    #invalid_snippets_count = count_snippets('invalid_py_test.txt')

    print(f"Number of valid snippets: {valid_snippets_count}")
    #print(f"Number of invalid snippets: {invalid_snippets_count}")