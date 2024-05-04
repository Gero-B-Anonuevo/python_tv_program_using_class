class TV:
    def __init__(self, channel = 1, volumeLevel = 0, status = True): #setting parameters with default value
        self.channel = channel
        self.volumeLevel = volumeLevel
        if status == True: #setting the tv on or off base on the boolean value
            self.status = "On"
        else:
            self.status = "Off"
    
    def turnOn(self): #function to set the value on true to turn on
        self.status = True
        return self.status
    
    def turnOff(self): #function to set the value on false to turn off
        self.status = False
        return self.status
    
    def getChannel(self): 
        return self.channel 
        
    def setChannel(self):
        try: #using try and except to prevent unsuitable inputs
            #input function to ask user input when called in other programs
            self.channel = int(input("What channel do you want to watch (1-120): ")) 
        except ValueError:
            return "Not a number"
        else:
            if self.channel > 120 or self.channel < 1: #checking if the number given is within the range of the channel
                return "Invalid"
            else:
                return self.channel
        
    def getVolume(self):
        return self.volumeLevel
        
    def setVolume(self):
        try: #another try and except to prevent errors
            self.volumeLevel = int(input("What new volume do you want (1-7): "))
        except ValueError:
            return "Not a number"
        else:
            if self.volumeLevel > 7 or self.volumeLevel < 1: #making sure that the user input is within the range of volume
                return "Invalid"
            else:
                return self.volumeLevel
        
    def channelUp(self):
        self.channel = self.channel + 1 #plus one for upward
        return self.channel
            
    def channelDown(self):
        self.channel = self.channel - 1 #minus one for downward
        return self.channel
        
    def volumeUp(self):
        self.volumeLevel = self.volumeLevel + 1 #plus one for increase
        return self.volumeLevel
        
    def volumeDown(self):
        self.volumeLevel = self.volumeLevel - 1 #minus one for decrease
        return self.volumeLevel
