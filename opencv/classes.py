import cv2
import numpy as np

image_x, image_y = 64,64
cam = cv2.VideoCapture(0)

img_counter = 0

from keras.models import load_model
classifier = load_model('opencv/Trained_model.h5')
classifier._make_predict_function()
class TextPrint: 
	def __init__(self,val1):
		img_text = ''
		while True:
				ret, frame = cam.read()
				frame = cv2.flip(frame,1)

				img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)
				imcrop = img[102:298, 427:623]
				img_ycrcb = cv2.cvtColor(imcrop, cv2.COLOR_BGR2YCR_CB)
				blur = cv2.GaussianBlur(img_ycrcb,(11,11),0)

				lower_blue = np.array([20, 133, 77])
				upper_blue = np.array([255, 173, 127])
				
				# hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
				mask = cv2.inRange(blur, lower_blue, upper_blue)
				
				cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
				cv2.imshow("test", frame)
				cv2.imshow("mask", mask)
				
				#if cv2.waitKey(1) == ord('c'):
						
				img_name = "1.png"
				save_img = cv2.resize(mask, (image_x, image_y))
				cv2.imwrite(img_name, save_img)
				print("{} written!".format(img_name))
				img_text = predictor()
						

				if cv2.waitKey(1) == 27:
					break
				self.i=val1
				self.text=val1
				for i in range(1,10):
					self.text  = self.i + self.text
def predictor():
	import numpy as np
	from keras.preprocessing import image
	test_image = image.load_img('1.png', target_size=(64, 64))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict(test_image)
	if result[0][0] == 1:
		return 'A'
	elif result[0][1] == 1:
		return 'B'
	elif result[0][2] == 1:
		return 'C'
	elif result[0][3] == 1:
		return 'D'
	elif result[0][4] == 1:
		return 'E'
	elif result[0][5] == 1:
		return 'F'
	elif result[0][6] == 1:
		return 'G'
	elif result[0][7] == 1:
		return 'H'
	elif result[0][8] == 1:
		return 'I'
	elif result[0][9] == 1:
		return 'J'
	elif result[0][10] == 1:
		return 'K'
	elif result[0][11] == 1:
		return 'L'
	elif result[0][12] == 1:
		return 'M'
	elif result[0][13] == 1:
		return 'N'
	elif result[0][14] == 1:
		return 'O'
	elif result[0][15] == 1:
		return 'P'
	elif result[0][16] == 1:
		return 'Q'
	elif result[0][17] == 1:
		return 'R'
	elif result[0][18] == 1:
		return 'S'
	elif result[0][19] == 1:
		return 'T'
	elif result[0][20] == 1:
		return 'U'
	elif result[0][21] == 1:
		return 'V'
	elif result[0][22] == 1:
		return 'W'
	elif result[0][23] == 1:
		return 'X'
	elif result[0][24] == 1:
		return 'Y'
	elif result[0][25] == 1:
		return 'Z'