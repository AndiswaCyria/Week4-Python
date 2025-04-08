import os
def modify_content(content):
    return content.upper()

def main():
    print("Welcome to the File Modifier!")    
    filename = input("Enter the name of the file to read: ").strip()
    print(f"Reading from {filename}...")
    
    try:
        with open(filename, "r") as file:
            print("File opened successfully!")
            content = file.read()
            print("File read successfully!")
            print(content)
            
            modified_content = modify_content(content)
            new_filename = f"modified_{filename}"
            with open(new_filename, "w") as new_file:
                new_file.write(modified_content)
                print(f"Modified content written to {new_filename}")
                
    except FileNotFoundError:  
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read or write file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
    