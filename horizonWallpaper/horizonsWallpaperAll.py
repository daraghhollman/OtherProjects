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

def DrawImage(bodies, scale=1):
    image = Image.new('RGB', (1920, 1080), color='black')

    centerX, centerY = image.size[0] // 2, image.size[1] // 2

    draw = ImageDraw.Draw(image)

    radius = 3
    textOffsetX = 0
    textOffsetY = -15

    pixelCoords = []
    names = []
    for body in bodies:
        pixelCoords.append([centerX + body["position"][0]*scale, centerY + body["position"][1]*scale])
        names.append(body["name"])

    print("Locations found")

    for point, name in zip(pixelCoords, names):
        #print("Drawing Point")
        x, y = point
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill='white', outline='white')
        #draw.text((x + textOffsetX, y + textOffsetY), str(name), fill="white")
        #print(name)

    image.save('planets.png')

def ReadIDList(path):
    ids, names = np.loadtxt(path, unpack=True, dtype={'names': ('ID', 'Name'), "formats": (int, '|S15')}, delimiter=" ")
    return (ids, names)

ids, names = ReadIDList(r"/home/daraghhollman/Main/OtherProjects/horizonWallpaper/includedIDs.txt")

bodies = []
for id in range(634):
    print(f"\rStep: {id}")
    bodies.append(GetPosition(id, "500@10", today))

print("Drawing bodies...")
DrawImage(bodies, scale=30)
