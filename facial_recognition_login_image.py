import face_recognition
import argparse
import imutils
import pickle
import cv2
import json

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
ap.add_argument("-l", "--login", required=True,
	help="name login")

args = vars(ap.parse_args())

print("[INFO] loading encodings + face detector + image...")
data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])
image = cv2.imread(args["image"]);
login = args["login"];

# Clone the image
frame = image.copy();

frame = imutils.resize(frame, width=500)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

rects = detector.detectMultiScale(gray, scaleFactor=1.1,
								  minNeighbors=5, minSize=(30, 30),
								  flags=cv2.CASCADE_SCALE_IMAGE)

boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

encodings = face_recognition.face_encodings(rgb, boxes)
names = []

for encoding in encodings:

	matches = face_recognition.compare_faces(data["encodings"],
											 encoding)
	name = "Unknown"

	if True in matches:

		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts = {}

		for i in matchedIdxs:
			name = data["names"][i]
			counts[name] = counts.get(name, 0) + 1

		name = max(counts, key=counts.get)

	names.append(name)

loginSuccess = False

if login in names:
	loginSuccess = True

x = {
  "name": login,
  "loginSuccess": loginSuccess
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
