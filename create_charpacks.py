from furhat_remote_api import FurhatRemoteAPI
import json
import shutil
import os
import zipfile

texture_sources = "plot_src"
char_mane = "Amauri"
texture_type = "facial-hair"
texture_name = "boxplot"

def list_files_in_directory(directory):
    files = os.listdir(directory)
    sorted_files = sorted(files)
    return sorted_files

def remove_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' has been removed.")
    except FileNotFoundError:
        print(f"Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been removed.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_new_character_copy(source_folder,new_folder):
    # Copy the entire folder and its contents
    shutil.copytree(source_folder, new_folder)

    print(f"Folder '{source_folder}' copied to '{new_folder}'")


def move_and_rename_image(image_path, new_folder_name, new_image_name):
    print(image_path)
    print(new_folder_name)
    print(new_image_name)
    # Create a new subfolder if it doesn't exist
    if not os.path.exists(new_folder_name):
        print(new_folder_name)
        os.mkdir(new_folder_name)

    # Form the new path for the image in the new folder with the new name
    new_path = os.path.join(new_folder_name, new_image_name)

    # Move and rename the image
    shutil.copy(image_path, new_path)


## Updates the character profile and points to the new texture
def update_json(jsonfile, new_texture_folder,new_json_filename):
    # Read the JSON file
    with open(jsonfile, 'r') as file:
        data = json.load(file)
 

    # Modify the value of "facial-hair" overlay
    new_facial_hair_value = "new_facial_hair_value"
    for overlay in data["TextureController"]["Overlays"]:
        if overlay["CAT"] == "facial-hair":
            overlay["VAL"] = new_texture_folder
            break  # Assuming there's only one "facial-hair" overlay

    # Save the updated JSON data to a new file
    with open(new_json_filename, 'w') as outfile:
        json.dump(data, outfile, separators=(',', ':'))

    print(f"Updated JSON data saved to '{new_json_filename}'")

### Clean previous build
remove_folder("models")
remove_file(char_mane+".charpack")
            
### Copy data to create a new character pack into the models folder based on the models src
create_new_character_copy("models_src", "models")


# for each png image in the plot_src folder, created a new character profile linking to that png as a texture
counter =1
files_in_directory = list_files_in_directory(texture_sources)
for file in files_in_directory:
    print(file)
    txt_name = texture_name+""+str(counter)
    move_and_rename_image(texture_sources+"/"+file, "./models/adult/textures/"+texture_type+"/"+txt_name, new_image_name="albedo.png")
    update_json('models_src/adult/profiles/characters/Victor.json',txt_name, 'models/adult/profiles/characters/'+char_mane+str(counter)+".json")
    counter+=1


### zip all the characters into a charpack
zf = zipfile.ZipFile(char_mane+".charpack", "w")
for dirname, subdirs, files in os.walk("models"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
