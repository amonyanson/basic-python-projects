import cv2
import numpy as np
from sklearn import svm
import tkinter as tk
from tkinter import filedialog
(x_train, y_train) = (np.load("dataset_x.npy"), np.load("dataset_y.npy"))
clf = svm.SVC()
clf.fit(x_train, y_train)
def upload_image():
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img = cv2.resize(img, (32, 32))
    analysis_result = clf.predict(img.reshape(1, -1))
    print(f"Analysis result: {analysis_result[0]}")
window = tk.Tk()
window.title("Image Analysis")
btn = tk.Button(window, text="Upload Image", command=upload_image)
btn.pack()
window.mainloop()