import cv2
import numpy as np
choice = -1
while choice != 1 and choice != 2:
    choice = int(input("Which set would you like to use? Enter 1 or 2:"))
# Training #
if choice == 2:
    samples = np.loadtxt('set2generalsamples.data', np.float32)
    responses = np.loadtxt('set2generalresponses.data', np.float32)
elif choice == 1:
    samples = np.loadtxt('/home/xilinx/project_files/set1generalsamples.data', np.float32)
    responses = np.loadtxt('/home/xilinx/project_files/set1generalresponses.data', np.float32)
responses = responses.reshape((responses.size, 1))
model = cv2.ml.KNearest_create()
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

# Testing #
if choice == 2:
    im = cv2.imread('set2test.png')
elif choice == 1:
    im = cv2.imread('/home/xilinx/project_files/set1test.png')

out = np.zeros(im.shape, np.uint8)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)

images, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        [x, y, w, h] = cv2.boundingRect(cnt)
        if h > 28:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = thresh[y:y + h, x:x + w]
            roismall = cv2.resize(roi, (10, 10))
            roismall = roismall.reshape((1, 100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.findNearest(roismall, k=1)
            string = str(int((results[0][0])))
            cv2.putText(out, string, (x, y + h), 0, 1, (0, 255, 0))

# cv2.imshow('im', im)
cv2.imwrite("/home/xilinx/project_files/in.png", im)
cv2.imwrite("/home/xilinx/project_files/out.png", out)
# cv2.imshow('out', out)
