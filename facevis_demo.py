from furhat_remote_api import FurhatRemoteAPI
from time import sleep

# "Sweating": 43,

frame_count_dict = {
    "Mask": 25,
    "Landscape": 35,
    "Flowers": 32,
    "Tears": 24,
    # "Sweating": 43,
    "Sweating": 30,
    "Battery": 13,
    "Eyes": 23,
    "Clock": 25
}

###### demo order ######
# Landscape
# Mask
# Sweating
# Flowers

CHAR_NAME = "Flowers"
CHAR_FRAME_COUNT = frame_count_dict[CHAR_NAME]
DELAY_TIME = 1.5      # seconds


def check_flowers(index):
    # Flowers: frame count = 32
    frame_count = 32
    sadness = float(index/frame_count) * 3
    # Perform a custom gesture
    furhat.gesture(body={
        "frames": [
            {
                "time": [
                    0.5
                ],
                "params": {
                    "EXPR_SAD": sadness
                }
            }
        ],
        "class": "furhatos.gestures.Gesture"
    })

def check_sweating(index):
    # Sweating: frame count = 30
    frame_count = 30
    happiness = float(index/frame_count) * 1.5 - 0.5
    # Perform a custom gesture
    furhat.gesture(body={
        "frames": [
            {
                "time": [
                    0.5
                ],
                "params": {
                    "SMILE_OPEN": happiness
                }
            }
        ],
        "class": "furhatos.gestures.Gesture"
    })
    

def check_clock(index):
    # Clock: frame count = 25
    if index % 3 == 0:
        # 3, 6, 9, 12, 15, 18, 21, 24
        furhat.gesture(name="BrowFrown")
    else:
        if index % 4 == 0:
            # 4, 8, 16, 20
            furhat.gesture(name="ExpressFear")
        else:
            if index % 5 == 0:
                # 5, 10, 15, 25
                furhat.gesture(name="ExpressSad")

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
# furhat = FurhatRemoteAPI("localhost")
# furhat = FurhatRemoteAPI("10.100.238.89")
furhat = FurhatRemoteAPI("10.100.239.12")
# furhat = FurhatRemoteAPI("192.168.0.100")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
# furhat.set_voice(name='Matthew')
# if CHAR_NAME == "Landscape":
#     furhat.set_voice(name='Matthew')

# load 
# furhat.set_face(mask="adult",character="James")

# Say "Hi there!"
# furhat.say(text="Top of the morning to ya!")
# furhat.say(text="I am in the Telstra Creator Space")

# Perform a named gesture
# furhat.gesture(name="BrowRaise")


# Loop through faces to create animation
start_index = 1
end_index = CHAR_FRAME_COUNT+1
step = 1
if CHAR_NAME == "Battery":
    start_index = CHAR_FRAME_COUNT
    end_index = 0
    step = -1
    
for i in range(start_index, end_index, step):
    # furhat.set_face(mask="adult",character="Amauri/Amauri"+str(i))
    curr_face = CHAR_NAME+"/"+CHAR_NAME+str(i)
    print("Setting face to %s" % curr_face)
    furhat.set_face(mask="adult",character=curr_face)
    
    # check if need to perform gestures
    if CHAR_NAME == "Mask":
        if i >= 26:
            furhat.gesture(name="CloseEyes")
    if CHAR_NAME == "Sweating":
        check_sweating(i)
    if CHAR_NAME == "Flowers":
        check_flowers(i)
    if CHAR_NAME == "Clock":
        check_clock(i)
            
    # delay
    sleep(DELAY_TIME)

# furhat.set_face(mask="adult", character="Amauri/Victor")
# furhat.set_face(mask="adult", character="StandardExtras/Luna")

# Set the voice of the robot
# furhat.set_voice(name='Brian')

# Say "Hi there!"
# furhat.say(text="See ya later aligator!")