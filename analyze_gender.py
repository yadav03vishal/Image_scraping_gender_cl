
from deepface import DeepFace
import cv2
import os
import pandas as pd

df = pd.DataFrame(columns=['Image', 'Gender'])


directory = 'myntra_images'


for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  
        img_path = os.path.join(directory, filename)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Failed to load image {filename}")
        else:
            try:
                result = DeepFace.analyze(img, actions=['gender'], enforce_detection = False)
                gender = result[0]['gender']
                dominant_gender = max(gender, key=gender.get) 
                df.loc[len(df)] = [filename, dominant_gender]  
            except Exception as e:
                print(f"Failed to analyze image {filename}. Error: {str(e)}")


df.to_csv('gender_results.csv', index=False)
