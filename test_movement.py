from furhat_remote_api import FurhatRemoteAPI

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
# furhat = FurhatRemoteAPI("localhost")
furhat = FurhatRemoteAPI("10.100.238.89")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')

# Say "Hi there!"
furhat.say(text="Hi there!")

# Play an audio file (with lipsync automatically added) 
# furhat.say(url="https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg10.wav", lipsync=True)

# Listen to user speech and return ASR result
result = furhat.listen()

# Perform a named gesture
furhat.gesture(name="BrowRaise")

# Perform a custom gesture
furhat.gesture(body={
    "frames": [
        {
            "time": [
                4.0
            ],
            "params": {
                # "BLINK_LEFT": 1.0
                "SMILE_OPEN": 1.0
            }
        },
        {
            "time": [
                2.0
            ],
            "params": {
                "reset": True
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
})

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