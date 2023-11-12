import os
import shutil



from_dir = "C:/Users/Asus/Downloads"
to_dir = 'C:/Adithya/document_files'



# List of allowed extensions
allowed_extensions = ['.txt', '.doc', '.docx', '.pdf' , '.skp']

list_of_files = os.listdir(from_dir)

for files in list_of_files:
    file_name, file_extension = os.path.splitext(files)

    # Check if the extension is blank (empty string)
    if file_extension == " ":
        continue

    # Check if the extension is one of the allowed extensions
    if file_extension in allowed_extensions:
        # Your code for processing files with allowed extensions
        # You can copy or move the file to the target directory here

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document files"
        path3 = to_dir + '/' + "Document files" +  '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + ".......")

            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving "+ file_name + '......')
            shutil.move(path1,path3)


