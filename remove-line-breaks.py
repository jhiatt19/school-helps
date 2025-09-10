import argparse
import os

def remove_line_breaks(input_filepath):
    """
    Reads a text file, removes all newline and carriage return characters,
    and saves the cleaned text to a new file.
    
    Args:
        input_filepath (str): The path to the input text file.
    """
    # Create the output filename. We'll add 'cleaned_' to the original name.
    directory, filename = os.path.split(input_filepath)
    output_filename = f"cleaned_{filename}"
    output_filepath = os.path.join(directory, output_filename)

    try:
        # Open the input file for reading
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            # Read the entire content of the file
            content = infile.read()
            
            # Replace all newline characters (\n) and carriage returns (\r) with a single space.
            # This prevents words from merging together.
            cleaned_content = content.replace('\n', ' ').replace('\r', '')

        # Open a new file for writing the cleaned content
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(cleaned_content)
        
        print(f"Successfully cleaned the file. The new file is located at:\n{output_filepath}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description='Removes newline characters from a text file.')
    parser.add_argument('file_path', type=str, help='The path to the text file to be cleaned.')

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the main function with the provided file path
    remove_line_breaks(args.file_path)