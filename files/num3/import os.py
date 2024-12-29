import os

def merge_files(folder_path, output_file):

    file_data = []  # List to store file data (name, line count, content)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith((".txt")): 
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    line_count = len(lines)
                    file_data.append((filename, line_count, lines))
            except Exception as e:
                print(f"Error reading file '{filename}': {e}")
    
    file_data.sort(key=lambda item: item[1])

    try:
         with open(output_file, 'w', encoding='utf-8') as outfile:
                for filename, line_count, lines in file_data:
                    outfile.write(filename + "\n")
                    outfile.write(str(line_count) + "\n")
                    outfile.writelines(lines)
    except Exception as e:
        print(f"Error writing to output file: {e}")
    print(f"Файлы успешно объединены в '{output_file}'")

folder_path = "Files"   
output_file = "merged.txt" 

merge_files(folder_path, output_file)
