from astroquery.jplhorizons import Horizons
from datetime import datetime, timedelta, date
from PIL import Image, ImageDraw
import numpy as np

today = str(date.today())

def Yesterday(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    previous_date = date - timedelta(days=1)
    return previous_date.strftime('%Y-%m-%d')

def GetPosition(id, centre, date):

    body = Horizons(id=id, location=centre, epochs={'start':Yesterday(date), 'stop':date, 'step':'1'})

    bodyVectors = body.vectors()
    currentVector = bodyVectors[-1]
    name = currentVector["targetname"]
    currentPosition = [currentVector["x"], currentVector["y"], currentVector["z"]]

    bodyDict = {
        "id": id,
        "name": name,
        "position": currentPosition
    }

    return bodyDict

def DrawImage(bodies, names, scale=1):
    image = Image.new('RGB', (1920, 1080), color='black')

    centerX, centerY = image.size[0] // 2, image.size[1] // 2

    draw = ImageDraw.Draw(image)

    radius = 3
    textOffsetX = 0
    textOffsetY = -15

    pixelCoords = []
    for body in bodies:
        pixelCoords.append([centerX + body["position"][0]*scale, centerY + body["position"][1]*scale])

    print("Locations found")

    for point, name in zip(pixelCoords, names):
        #print("Drawing Point")
        x, y = point
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill='#008000', outline='#008000')
        draw.text((x + textOffsetX, y + textOffsetY), name, fill="#008000")

    radius=radius*2
    image.save('planets.png')

def ReadIDList(path):
    ids, names = np.loadtxt(path, unpack=True, dtype={'names': ('ID', 'Name'), "formats": (int, '|S15')}, delimiter=" ")
    return (ids, names)

ids, names = ReadIDList(r"/home/daraghhollman/Main/OtherProjects/horizonWallpaper/includedIDs.txt")

bodies = []
for id in ids:
    print(f"\rStep: {id}")
    bodies.append(GetPosition(id, "500@5", today))

print("Drawing bodies...")
DrawImage(bodies, names, scale=40)
