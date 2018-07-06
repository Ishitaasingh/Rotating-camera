import cv2
import numpy as np

def main():
	w=800
	h=600

	cap=cv2.VideoCapture(0)

	cap.set(3,w)
	cap.set(4,h)

	print(cap.get(3))
	print(cap.get(4))

	if cap.isOpened():
		ret,frame=cap.read()
	else:
		ret=false

	ret,frame1=cap.read()
	
	frame1.shape
	i=0
	mode=True

	while ret:

		M = cv2.getRotationMatrix2D((w/2,h/2), i,1.0)
		ret,frame1=cap.read()
		frame1 = cv2.warpAffine(frame1, M, (800,600))
		cv2.imshow("dhun dhun dhun",frame1)
		if (mode):
			i=i+2
		else:
			i=i-2
		
		k = cv2.waitKey(1) & 0xFF
		if k==27:
			break;
		elif k == ord('m'):
			mode = not mode
		

	cv2.destroyAllWindows()
	cap.release()


	
	
	
main()