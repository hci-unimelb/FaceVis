from furhat_remote_api import FurhatRemoteAPI
import json
import shutil




# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
furhat = FurhatRemoteAPI("10.100.237.184")
#furhat = FurhatRemoteAPI("localhost")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')

# load 
furhat.set_face(mask="adult",character="James")

# Say "Hi there!"
furhat.say(text="Hi there!")

# Play an audio file (with lipsync automatically added) 
furhat.say(url="https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg10.wav", lipsync=True)

# Listen to user speech and return ASR result
result = furhat.listen()

# Perform a named gesture
furhat.gesture(name="BrowRaise")

# Perform a custom gesture
furhat.gesture(body={
    "frames": [
        {
            "time": [
                0.33
            ],
            "params": {
                "BLINK_LEFT": 1.0
            }
        },
        {
            "time": [
                0.67
            ],
            "params": {
                "reset": True
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    })

def create_new_character_copy(source_folder,new_folder):

    # Copy the entire folder and its contents
    shutil.copytree(source_folder, new_folder)

    print(f"Folder '{source_folder}' copied to '{new_folder}'")

def create_new_texture_folder(texture_sbf, nex_texture_name, image_file):

    # Name of the new subfolder
    new_folder_name = os.path.join(os.path.dirname(texture_sbf), os.path.dirname(nex_texture_name))

    # Create a new subfolder
    new_folder_path = os.path.join(os.path.dirname(image_file), new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Move the image file to the new subfolder
    shutil.move(image_file, os.path.join(new_folder_path, os.path.basename(image_file)))


def update_json(jsonfile, new_texture_folder):

        # Read the JSON file
    with open('jsonfile', 'r') as file:
        data = json.load(file)
 

    # Modify the value of "facial-hair" overlay
    new_facial_hair_value = "new_facial_hair_value"
    for overlay in data["TextureController"]["Overlays"]:
        if overlay["CAT"] == "facial-hair":
            overlay["VAL"] = new_texture_folder
            break  # Assuming there's only one "facial-hair" overlay

    # Save the updated JSON data to a new file
    new_json_filename = "updated_data.json"
    with open(new_json_filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Updated JSON data saved to '{new_json_filename}'")


create_new_character_copy("models_src", "models")






import zipfile
import os 

zf = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk("mydirectory"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()


# Set the voice of the robot
furhat.set_voice(name='Brian')

# Say "Hi there!"
furhat.say(text="Bye now!")


#output = furhat.set_face(mask="adult", model="adult",character="Omar",texture= {"TextureController": {
#                 "Overlays": [{
#                "CAT": "facial-hair",
#                "VAL": "29_adult_male_middle_east_realistic",
#                "COLOR": "#FFFFFFff"
#            }]
#                 }}
#                 )

#output = furhat.set_face(model="adult_mask",texture= "Omar")

furhat.set_face(mask="adult",character="Victor/Victor")

#print(output)

# Get the users detected by the robot 
users = furhat.get_users()

# Attend the user closest to the robot
furhat.attend(user="CLOSEST")

# Attend a user with a specific id
furhat.attend(userid="virtual-user-1")

# Attend a specific location (x,y,z)
furhat.attend(location="0.0,0.2,1.0")

# Set the LED lights
furhat.set_led(red=200, green=50, blue=50)