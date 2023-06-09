# PDF File Finder

This script will give the list of file in a given folder

This repository contains a simple Python script that finds and prints the names of all PDF files in the current directory.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python (version 3.x)
- `glob` module (comes pre-installed with Python)

## Usage

1. Clone the repository to your local machine or download the script file.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

   ```bash
   python A_list_of_file_in_a_directory.py
   ```

   The script will search for all PDF files in the current directory and print their names.

## Contributing

If you have any suggestions or improvements for the script, feel free to contribute! You can:

- Open an issue to discuss potential changes.
- Fork the repository, make your improvements, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The `glob` module in Python makes it easy to find files based on patterns.
- This script is a simple example and can be expanded upon for more complex file search functionality.

That's it! You can customize this README file to include any additional information or instructions specific to your repository.


**command usage**

python A_list_of_file_in_a_directory.py &>list_of_files.txt
** **

_A method to open a file in a python_

f = open('file.txt')

a = f.read()

print a

f.close()

** **

_Alternative method to open a file _

with open('file.txt') as f:

for line in f:

print line
