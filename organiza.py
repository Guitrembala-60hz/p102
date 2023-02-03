import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/elien/OneDrive/Documentos/pasta Gui"  #pasta de origem         
to_dir = "C:/Users/elien/OneDrive/Documentos/pasta Gui"   #pasta de destino
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.docx', '.txt']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "documentos"
        path3 = to_dir + '/' + "documentos" + '/' + file_name
        
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          
          shutil.move(path1, path3)
          
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)