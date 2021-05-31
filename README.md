# PageOpener
PageOpener is a Python script for opening a series of web pages where the urls are identical expect for the final query parameter. 
The script takes as parameters: <ID> "<link>", where the ID is the maximum value of the integer at the end of the urls, and link is the common part of the urls.
The links are in the following format: http://alinkname.com?QueryParameter=0, http://alinkname.com?QueryParameter=50, http://alinkname.com?QueryParameter=100...
with the value at the end of the url starting at 0 and incrementing by 50 until the ID inputted by the user is met or exceeded (if the user inputs 1188, the last integer value will be 1150)
All the web pages will be opened in the same window.

## Usage 
1. Download the VPE_script.py script from this repository and place it into a new folder

2. Go to the terminal and change the directory to the folder containing VPE_script.py

3. Run the following command (link should be in quotes): python VPE_script.py  <ID> "<link>"
    Ex: to open the link (http://alinkname.com?QueryParameter=) with the maximum integer value (130), use the following command:
```batch
    python VPE_script.py 130 "http://alinkname.com?QueryParameter="
```
the urls http://alinkname.com?QueryParameter=0, http://alinkname.com?QueryParameter=50, and http://alinkname.com?QueryParameter=100 will then be opened.

## Notes
For all non-Windows operating systems or Windows without Chrome, the links will open in the most recently used browser window. For Windows (if Chrome is installed), a new chrome window will be opened with a tab per link.
The link must be the full link including the url scheme: i.e. http://alinkname.com?QueryParameter=