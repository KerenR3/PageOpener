# PageOpener
PageOpener is a Python script for opening a series of web pages where the urls all end in an incrementing number ID.
The script takes as parameters: <ID> "<link>", where the ID is the maximum location ID of the urls to open, and link is the name of the url.
The links are in the following format: link/locationID=0, link/locationID=50,link/locationID=100...
with the location ID starting at 0 and incrementing by 50 unitl the ID inputted by the user is met or exceeded (if the user inputs 1188, the last location ID will be 1150)
All the web pages will be opened in the same window.

## Usage 
1. Download the VPE_script.py script from this repository and place it into a new folder

2. Go to the terminal and change the directory to the directory containing the folder which has VPE.script.py

3. Run the following command (link should be in quotes): python VPE_script.py  <ID> "<link>"
    Ex: to open the link (link/locationID=) with the maximum location ID (130), use the following command:
```batch
    python VPE_script.py 130 "link/locationID="
```
    the urls link/locationID=0, link/locationID=50, and link/locationID=100 will then be opened.

## Notes
For all non-Windows operating systems or Windows without Chrome, the links will open in the most recently used browser window. For Windows (if Chrome is installed), a new window will be opened where all the links will appear in.
