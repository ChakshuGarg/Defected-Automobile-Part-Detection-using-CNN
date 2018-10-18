import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cv2
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
import glob
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

 


def DetectBoundingBox(DirPath):
   for filepath in glob.iglob(DirPath):
      image = cv2.imread(filepath)
      image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

      thresh = threshold_otsu(image)
      bw = closing(image > thresh, square(20))


      cleared = clear_border(bw)


      label_image = label(cleared)
      image_label_overlay = label2rgb(label_image, image=image)
      
      #fig, ax = plt.subplots(figsize=(10, 6))
      #ax.imshow(image_label_overlay)
      areas=[]
      for region in regionprops(label_image):
         areas.append(region.area)
      
      maxarea=0
      for area in areas:
         if area>maxarea:
            maxarea=area
          
      
      for region in regionprops(label_image):
          
          if region.area == maxarea and region.area>700:
              
              minr, minc, maxr, maxc = region.bbox
              rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                        fill=False, edgecolor='red', linewidth=2)
              #ax.add_patch(rect)
              print("Bounding Box Coordinates")
              print ("x1 "+str(minr)+" ,y1 "+str(minc)+" ,x2 "+str(maxr)+" ,y2 "+str(maxc))
              CroppedImg=ImgCrop(minc, minr, maxc - minc, maxr - minr,filepath,'',filepath)

      #ax.set_axis_off()
      #plt.tight_layout()
      #plt.show()
