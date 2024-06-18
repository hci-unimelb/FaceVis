import zmq
import zmq.ssh
import json
import time
from time import sleep

class fcclient:
    
    osock=None
    isock=None
    
    def __init__(self):
        pass
    
    def open(self,addr):
        context = zmq.Context()
        self.osock = context.socket(zmq.PUSH)
        res = self.osock.connect('tcp://'+addr+':30001')
        #zmq.ssh.tunnel_connection(self.osock, "tcp://locahost:3001", "root@r"+addr)
        #print(res)
        #self.isock = context.socket(zmq.SUB)
        #self.isock.setsockopt_string(zmq.SUBSCRIBE,'FaceCore_')
        #self.isock.connect('tcp://'+addr+':30002')

    def call_servo(self,cmd,args=''):
        if cmd == '':
            msg = 'To_Servo_' + ' '.join([str(x) for x in args])
        else:
            msg = 'To_Servo_' + cmd + ' ' + json.dumps(args)
        self.osock.send_string(msg)

    
    def pub(self,cmd,args='',timeout=2000):

        if cmd.startswith('set'):
            timeout=0
    
        if args == '':
            str = 'To_FaceCore_' + cmd
        else:
            str = 'To_FaceCore_' + cmd + ' ' + json.dumps(args)
        
        res = self.osock.send_string(str)
        recieved = []
        print(str)
        print(res)

   
    def call(self,cmd,args='',timeout=2000):

        if cmd.startswith('set'):
            timeout=0
    
        if args == '':
            str = 'To_FaceCore_' + cmd
        else:
            str = 'To_FaceCore_' + cmd + ' ' + json.dumps(args)
        
        self.osock.send_string(str)
        recieved = []
        print(str)

        #while  #self.isock.poll(timeout) == zmq.POLLIN:
        timer = 20
        while True:    
            #reply = self.isock.recv().decode('utf-8').split(' ',1)
            #recieved.append(reply)
            #print('recieved',len(reply[1]),'bytes:')
            #print(reply[0],reply[1][:50]+'...')
            
            #if (reply[0].lower().endswith(cmd.lower())):
            #    res = reply[1]
            #continue
            time.sleep(timer)
            break
        print('over')
        try:
            parsed = json.loads(res)
        except:
            if len(recieved):
                print('*** got this that I couldnt digest: ***')
                print(recieved)
            parsed = ''

        return parsed
    

#IP='localhost'
#IP = '10.100.239.37'
#IP = '172.20.10.2'
IP='192.168.137.1'
face_client =fcclient()
face_client.open(IP)
sleep(10)
face_client.pub('setCharacter {"NAME":"Omar"}')
sleep(0.5)
#face_client.pub('setCharacter {"NAME":"Patricia"}')
#sleep(0.5)
#face_client.pub('setCharacter {"NAME":"Maurice"}')
#sleep(0.5)
#face_client.pub('setCharacter {"NAME":"Jane"}')
#sleep(0.5)
#face_client.pub('setCharacter {"NAME":"Chen"}')