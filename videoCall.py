import time

class Call:
    def __init__(self, type, source, destination):
           self.type = type
           self.source = source
           self.destination = destination
           
    def performCall(self):
        print("Request is being made ......")
        time.sleep(3)
        print(f"Reached {self.destination}")
        time.sleep(2)
        print("Handshake completed")
        
v1 = Call("TCP", "127.0.0.1", "192.168.116.146") 


v1.performCall()      
        
        
              
           
           
           