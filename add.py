import dlib
import numpy as np
import imageio
import cv2

face_detector = dlib.get_frontal_face_detector()
pose_predictor_68_point = dlib.shape_predictor('./models/shape_predictor_68_face_landmarks.dat')
face_encoder = dlib.face_recognition_model_v1('./models/dlib_face_recognition_resnet_model_v1.dat')

def whirldata_face_detectors(img, number_of_times_to_upsample=1):
 return face_detector(img, number_of_times_to_upsample)

def whirldata_face_encodings(face_image,num_jitters=1):
 face_locations = whirldata_face_detectors(face_image)
 if(len(face_locations) == 0 or len(face_locations)>1):
     print("No faces or more than one faces")
     return []
 else:
    face_location = face_locations[0]
    pose_predictor = pose_predictor_68_point
    predictor = pose_predictor(face_image, face_location) 
    return np.array(face_encoder.compute_face_descriptor(face_image, predictor, num_jitters))

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
         break	
small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
rgb_small_frame = small_frame[:, :, ::-1]
enc = whirldata_face_encodings(rgb_small_frame)
if(len(enc)!=0):
    print("Enter the name for the student")
    name = input()
    np.savetxt("./dataset/"+name+".csv",enc,delimiter=",")
video_capture.release()
cv2.destroyAllWindows()