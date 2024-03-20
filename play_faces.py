from furhat_remote_api import FurhatRemoteAPI
from time import sleep

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

# Perform a named gesture
furhat.gesture(name="BrowRaise")


for i in range(1,11,1):
    furhat.set_face(mask="adult",character="Amauri/Amauri"+str(i))
    sleep(0.5)

# Set the voice of the robot
furhat.set_voice(name='Brian')

# Say "Hi there!"
furhat.say(text="Bye now!")