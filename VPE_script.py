import sys
import webbrowser
import os
import platform

#A program which opens a series of webpages which have urls that differ only in the last query parameter. This parameter is an integer which starts
# at 0 and is incremented by 50 until the value specified by the user is reached. All the webpages are opened in the same browser window.

#The program uses two command-line arguments (the common part of the url and the max value of the integer at the end of the link) 
def main():
    if (len(sys.argv) != 3): #The program expects to receive two arguments
        print("usage: VPE_script.py <ID> \"<link>\"")
    else:
        #sys.argv[1] is the link url and sys.argv[2] is the maximum value of the integer at the end of the link
        open_file(sys.argv[2],sys.argv[1])


#Runs a loop which opens all the webpage
def open_file(link, max_id):
    if (platform.system() == "Windows"):
        os.system("start chrome") #opens a new chrome window (on Windows) in which all the other links will appear
    count =0
    for i in range(0,int(max_id), 50):
      webbrowser.open("{}{}".format(link, i)) #Opens a web page in the default browser
      count += 1
    if (count < 2):
        print(str(count) + " page has been opened")
    else:
        print(str(count) + " pages have been opened")

main()
