# Prompt the user to enter the file name
file_name = input("Please enter the file name: ") or "printf.py"

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read and print the file contents
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

with open (file_name, 'r') as file:
    content = file.read()
    print(content)