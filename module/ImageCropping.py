import cv2
from PIL import Image

def roi_selection(event, x, y, flags, param):
	#Refernce to the global variables
	global selection, roi
	selection = False
	#On Left mouse button click records roi with mouse selection status to True
	if event == cv2.EVENT_LBUTTONDOWN:
		selection = True
		roi = [x, y, x, y]
	#On Mouse movement records roi with mouse selection status to True
	elif event == cv2.EVENT_MOUSEMOVE:
		if selection == True:
			roi[2] = x
			roi[3] = y			

	#If Left mouse button is released changes mouse selection status to False
	elif event == cv2.EVENT_LBUTTONUP:
		selection = False
		roi[2] = x
		roi[3] = y
			
		
			
def ImgCrop(x1,y1,x2,y2,image_read_path,TempFolderPath,CropImageName):
    selection = False
    roi = [x1,y1,x2,y2]
    window_name='Input Image'
    window_crop_name='Cropped Image'
    esc_keycode=27
    wait_time=1


    input_img = cv2.imread(image_read_path,cv2.IMREAD_UNCHANGED)


    if input_img is not None:
	
	clone = input_img.copy()
	
	#cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
	
	#cv2.setMouseCallback(window_name, roi_selection)

	
	while True:
	
		#cv2.imshow(window_name,input_img)
		
	
		if len(roi) == 4:
	
			input_img = clone.copy()
	
			roi = [0 if i < 0 else i for i in roi]
			cv2.rectangle(input_img, (roi[0],roi[1]), (roi[2],roi[3]), (0, 255, 0), 2)	
			if roi[0] > roi[2]:
				x1 = roi[2]
				x2 = roi[0]
	
			else:
				x1 = roi[0]
				x2 = roi[2]
			
			if roi[1] > roi[3]:
				y1 = roi[3]
				y2 = roi[1]
			
			else:
				y1 = roi[1]
				y2 = roi[3]	
				
			
			crop_img = clone[y1 : y2 , x1 : x2]

			
			if len(crop_img):
				
				#cv2.namedWindow(window_crop_name,cv2.WINDOW_AUTOSIZE)
				#cv2.imshow(window_crop_name,crop_img)
				im = Image.fromarray(crop_img)
				im.save(CropImageName)
                
		
	
		#k = cv2.waitKey(wait_time)
	
		#if k == esc_keycode:  
	
			cv2.destroyAllWindows()
			return CropImageName
			
    else:
	    print 'Please Check The Path of Input File'

 
