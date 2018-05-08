# Texture CSV 

This is a small addon for blender to export all image paths of a scene into a csv. These paths can be manipulated in an other software like Excel (search and replace) and afterward be reimported to change the actual image paths within the blend file as well. 
The second functionality this addon provides currently is to automatically create a material nodetree for EVERY material in the scene! This is currently destructive and applies to all materials! 

How could that help me?

I was working on a project with over 800 textures and I simply lost the overview after some time. I didn't have the time to spend a lot of energy and time into creating a fancy asset management tool. Writing this addon was really simple an being able to export the texture paths to excel made it much easier to keep an overview, check for missing textures and change file path.
I wrote this small addon especially for this project. It was never designed to be flexible. Nevertheless, I decided to publish it here as it really saved my life. Let me know what you think, if there are and bugs and if there is an interest I will probably continue working on it.

<img src="images/readMe_03.jpg" width="50%">

# UI

- Export Path: defines the folder the csv will be saved to and loaded from. Currently the csv name is set to blend file name + materialCsv. 
- Change All Image Extensions: Operator to change all image extensions (e.g. form jpg to png)
- Append To CSV: Doesn't overwrite the csv but appends the image paths at the bottom
- Import CSV: Imports the csv and replaces all image paths for the images found in the csv
<img src="images/readMe_04.png" width="60%">

# Example: 

The goal for this scene was to create a 3d set that works from every position. This meant a lot of huge textures. Loading all textures for rendering took about half an hour!!!! I don't need the full resolution for all textures at all time. Even for preview I had to wait that long. Therefore, I wanted to easily scale textures down. Using the jpg with a resolution of 25% reduced the loading of the textures from half an hour to about 1 minute. Which really saved my life when iterating and doing lighting. I am even able to get the scene onto my GPU for rendering if I spend some time in optimizing the texture resolutions. 
For changing the texture resolutions, I created several directories, the 100% png, 50% jpg, 25%jpg. I then replace with “search and replace” Excel the path for the texture I want to change and load the paths from the csv. Stupid but works great. 

<img src="images/readMe_01.png" width="50%">
<img src="images/readMe_02.png" width="50%">
