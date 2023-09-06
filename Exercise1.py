def replace_words(input_text):
    words = input_text.split()
    count = words.count("terrible")
    replace_terrible = False

    for i in range(len(words)):
        if words[i] == "terrible":
            if replace_terrible:
                words[i] = "pathetic"
            else:
                words[i] = "marvellous"
            replace_terrible = not replace_terrible

    output_text = ' '.join(words)
    return count, output_text

def main():
    # Read the file
    with open("file_to_read.txt", "r") as file:
        input_text = file.read()

    count, output_text = replace_words(input_text)

    # Write to a new file
    with open("result.txt", "w") as file:
        file.write(output_text)

    print(f"The total times 'terrible' appears: {count+1}")

if __name__ == "__main__":
    main()