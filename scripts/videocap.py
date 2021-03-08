import cv2
import numpy as np

import filename


def videoRecord():
    videoCap = cv2.VideoCapture(0)
    videoCod = cv2.VideoWriter_fourcc(*'DIVX')
    videoFileName = filename.namingFile()+".avi"
    print(videoFileName)
    output = cv2.VideoWriter("temp.avi", videoCod, 20.0, (640,480))


    while(True):
        # Capture each frame of webcam video
        ret,frame = videoCap.read()
        cv2.imshow("My cam video", frame)
        output.write(frame)
        # Close and break the loop after pressing "x" key
        if cv2.waitKey(1) &0XFF == ord('x'):
            break

    # close the already opened camera
    videoCap.release()
    # close the already opened file
    output.release()
    # close the window and de-allocate any associated memory usage
    cv2.destroyAllWindows()
    


videoRecord()