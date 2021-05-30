import sys
import webbrowser
import os
import platform

#uses two commandline arugments (the url name and the max id number at the end of thel ink) 
#to run the open_file method
def main():
    if (len(sys.argv) != 3): #sys.argv returns an array of the commandline arguments
        print("usage: VPE_script.py <ID> \"<link>\"")
    else:
        #sys.argv[1] is the link url and sys.argv[1] is the maximum ID at the end of the link
        open_file(sys.argv[2],sys.argv[1])


#Runs a loop which opens a webpege with the ID at the end of the link starting at 0 and incremening by 50 until the ID specified by the user is reached
def open_file(link, max_id):
    if (platform.system() == "Windows"):
        os.system("start chrome") #opens a new chrome window (on Windows) which all the other links will be opened in
    count =0
    for i in range(0,int(max_id), 50):
      webbrowser.open("{}{}".format(link, i)) #method that opens a web page in the default browser
      count += 1
    if (count < 2):
        print(str(count) + " page has been opened")
    else:
        print(str(count) + " pages have been opened")

main()
