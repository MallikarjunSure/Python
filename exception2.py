file_path="rockyn.txt"
try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)
#except FileNotFoundError:
 #   print("File not found!")
except Exception as e:
    print(f"An error ocuured: {e}")
finally:
    print("Closing the file")
    
    
    
file_path="rockyn.txt"
try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error ocuured: {e}")
finally:
    print("Closing the file")