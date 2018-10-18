from module.RemoveBackgrounds import RemoveBackground
from module.ResizeImages import ResizeImage
from module.DetectBoundingBox import DetectBoundingBox

Defecttest='D:/JBM/YE358311_Fender_apron/YE358311_defects/test/*.jpg'
NormalTest='D:/JBM/YE358311_Fender_apron/YE358311_Healthy/test/*.jpg'
DefectTrain='D:/JBM/YE358311_Fender_apron/YE358311_defects/train/*.jpg'
NormalTrain='D:/JBM/YE358311_Fender_apron/YE358311_Healthy/train/*.jpg'


ResizeImage(Defecttest)
ResizeImage(NormalTest)
ResizeImage(DefectTrain)
ResizeImage(NormalTrain)

#DetectBoundingBox(DefectedPartDir)
#DetectBoundingBox(NormalPartDir)
#RemoveBackground(DefectedPartDir)
#RemoveBackground(NormalPartDir)
