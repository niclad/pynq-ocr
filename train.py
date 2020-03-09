import sys
import numpy as np
import cv2
choice = -1
while choice != 1 and choice != 2:
    choice = int(raw_input("Which set would you like to use? Enter 1 or 2:"))
if choice == 1:
    im = cv2.imread('set1train.png')
elif choice == 2:
    im = cv2.imread('set2train.png')
im3 = im.copy()

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

# Finding Contours #
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

samples = np.empty((0, 100))
responses = []
keys = [i for i in range(48, 58)]

for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        [x, y, w, h] = cv2.boundingRect(cnt)

        if h > 28:
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
            roi = thresh[y:y+h, x:x+w]
            roismall = cv2.resize(roi, (10, 10))
            cv2.imshow('norm', im)
            key = cv2.waitKey(0)

            if key == 27:  # (escape to quit)
                sys.exit()
            elif key in keys:
                responses.append(int(chr(key)))
                sample = roismall.reshape((1, 100))
                samples = np.append(samples, sample, 0)

responses = np.array(responses, np.float32)
responses = responses.reshape((responses.size, 1))
print "training complete"

samples = np.float32(samples)
responses = np.float32(responses)

if choice == 2:
    cv2.imwrite("set2train_result.png", im)
    np.savetxt('set2generalsamples.data', samples)
    np.savetxt('set2generalresponses.data', responses)
elif choice == 1:
    cv2.imwrite("set1train_result.png", im)
    np.savetxt('set1generalsamples.data', samples)
    np.savetxt('set1generalresponses.data', responses)
