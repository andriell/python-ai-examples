from PIL import Image

im = Image.open('colordiff_in.jpg') # Can be many different formats.
pix = im.load()
out = Image.new('RGB', (im.size[0]-1, im.size[1]-1))
outi = out.load()
print(im.size)  # Get the width and hight of the image for iterating over
for y in range(1, im.size[1]):
    for x in range(1, im.size[0]):
        # print(pix[x,y])
        # outi[x-1, y-1] = (pix[x, y][0], pix[x, y][1], pix[x, y][2])
        outi[x-1, y-1] = (
            max(abs(pix[x,y][0]-pix[x-1,y][0]), abs(pix[x,y][0]-pix[x,y-1][0]), abs(pix[x,y][0]-pix[x-1,y-1][0])),
            max(abs(pix[x,y][1]-pix[x-1,y][1]), abs(pix[x,y][1]-pix[x,y-1][1]), abs(pix[x,y][1]-pix[x-1,y-1][1])),
            max(abs(pix[x,y][2]-pix[x-1,y][2]), abs(pix[x,y][2]-pix[x,y-1][2]), abs(pix[x,y][2]-pix[x-1,y-1][2])),
        )

out.save('colordiff_out.jpg')  # Save the modified pixels as .png
print("End")
exit()
