
📂 Contents
🔹 Script 1: output.txt — Write, Append & Read
This script demonstrates how to:

Write user input to a file (output.txt)

Append more user input to the same file

Read and display the final contents of the file

Key Features:

Appending new lines using \n

Using open() in different modes: 'a' (append), 'r' (read)

Simple, interactive user input handling

Example Output:

vbnet
Copy
Edit
Enter text to write to the file: Hello World!
Data Successfully written to output.txt

Enter additional text to append to the file: This is appended.
data successfully appended 

Final content of output.txt:
Hello World!
This is appended.
🔹 Script 2: sample.txt — Write & Read Static Content
This part creates a new file sample.txt and writes two static lines to it, then reads and prints its content.

What It Does:

Uses 'w' (write mode) to create or overwrite the file

Demonstrates how to write multiple lines using file.write()

Displays the file content using read()

Example Output:

arduino
Copy
Edit
This is a sample text File
It contains multiple lines
🔧 Requirements
Python 3.x

No external libraries required

▶️ How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/python-file-handling.git
Navigate to the project folder:

bash
Copy
Edit
cd python-file-handling
Run the script:

bash
Copy
Edit
python filename.py
Replace filename.py with the name of your script file.

🧠 Learning Objectives
Understand basic file operations: read, write, append

Learn file modes: 'r', 'w', 'a'

Practice writing and reading string data using Python

📎 License
This project is open-source and available under the MIT License.

