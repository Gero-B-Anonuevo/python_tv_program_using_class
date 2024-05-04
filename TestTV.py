from TV import TV #to import the file as module
def main():
    tv1 = TV(30, 3) #using the class as module while giving parameters
    print(f"TV1 \nYour TV is {tv1.status}, on channel {tv1.getChannel()}, with the volume of {tv1.getVolume()}")

    tv2 = TV(3, 2)
    print(f"TV2 \nYour TV is {tv2.status}, on channel {tv2.getChannel()}, with the volume of {tv2.getVolume()}")

main() #calling the main function to start the program