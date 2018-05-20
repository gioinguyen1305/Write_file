import numpy as np
import cv2
import yaml
rect = []
mot = False
hai = False
ba = False
bon = False
park =[]
i = -1
def write_data():
    global park
    with open('vidCrsShow.yml', 'w') as stream:
        yaml.dump(park, stream,default_flow_style=False)
    with open(r'vidCrsShow.yml', 'r') as infile, open(r'vi.yml', 'w') as outfile:
        data = infile.read()
        data = data.replace("'", "")
        outfile.write(data)

def on_mouse(event,x,y,flags,params):
    global rect,mot,hai,ba,bon
    if event == cv2.EVENT_LBUTTONDOWN:
        if mot == True and hai == True and ba == True and bon == True:
            mot = False
            hai = False
            ba = False
            bon = False
            rect = []

        if mot == False:
            rect.append([x,y])
            print (rect)
            mot = True
        elif hai == False:
            rect.append([x,y])
            print (rect)
            hai = True
        elif ba == False:
            rect.append([x,y])
            print (rect)
            ba = True
        elif bon == False:
            rect.append([x,y])
            print (rect)
            bon = True

cap = cv2.VideoCapture('test_video.mp4')
waitTime = 50

#Reading the first frame
(grabbed, frame) = cap.read()

while(cap.isOpened()):

    (grabbed, frame) = cap.read()
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', on_mouse)    
    #drawing rectangle
    if mot == True and hai == True and ba == True and bon == True:
        i = i+1
        abc = str(rect)
        if ( i == 0):
            park = [{'id': i, 'points': abc}]#, {'id': 1, 'points': 2}]
        else:
            park.append({'id': i, 'points': abc})
            print(park)
        mot = False
        hai = False
        ba = False
        bon = False
        rect = []
    if (i == 3):
        write_data()

    cv2.imshow('frame',frame)

    key = cv2.waitKey(waitTime) 

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()