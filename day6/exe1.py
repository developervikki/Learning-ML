def count_words_and_line(filename):
    try:
        with open(filename,"r") as file:
            lines=file.readlines()
            line_count=len(lines)
            word_count=sum(len(line.split())for line in lines)
            
            print(f"Number of line: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    
count_words_and_line("sample.text")