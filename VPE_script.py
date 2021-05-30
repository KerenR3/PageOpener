import sys
import webbrowser

def main():
    if (len(sys.argv) != 3):
        print("usage: VPE_script.py <ID> \"<link>\"")
    else:
        openFile(sys.argv[2],sys.argv[1])



def openFile(link, maxID):
    count =0
    for i in range(0,int(maxID), 50):
      webbrowser.open("{}{}".format(link, i))
      count += 1
    print(str(count) + " pages have been opened")

    


main()
