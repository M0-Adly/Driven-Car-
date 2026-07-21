from tkinter import *
import cv2
from PIL import Image, ImageTk
import imutils
from scipy.spatial import distance
from imutils import face_utils
import dlib
from pygame import mixer
import os
import time

# ================== مسار ديناميكي ==================
current_dir = os.path.dirname(os.path.abspath(__file__))

# ================== الصوت ==================
mixer.init()
music_path = os.path.join(current_dir, "Driver Drowsiness Detection", "music.wav")
mixer.music.load(music_path)

# ================== EAR ==================
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# ================== إعدادات ==================
thresh = 0.25
sleep_time_threshold = 2   # بالثواني
sleep_start_time = None
camera_on = False

detect = dlib.get_frontal_face_detector()

model_path = os.path.join(
    current_dir,
    "Driver Drowsiness Detection",
    "models",
    "shape_predictor_68_face_landmarks.dat"
)
predict = dlib.shape_predictor(model_path)

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# ================== GUI ==================
root = Tk()
root.title("Driver Drowsiness Detection")
root.geometry("520x600")
root.resizable(False, False)

title = Label(root, text="Driver Drowsiness Detection", font=("Helvetica", 16, "bold"))
title.pack(pady=5)

video_label = Label(root)
video_label.pack(pady=10)

info_label = Label(root, text="Eyes Closed Time: 0.0 sec", font=("Helvetica", 14))
info_label.pack(pady=5)

# ================== التحكم ==================
control_frame = Frame(root)
control_frame.pack(pady=10)

def start_camera():
    global camera_on
    camera_on = True

def stop_camera():
    global camera_on, sleep_start_time
    camera_on = False
    sleep_start_time = None
    mixer.music.stop()
    info_label.config(text="Eyes Closed Time: 0.0 sec")

def toggle_music():
    if mixer.music.get_busy():
        mixer.music.stop()
    else:
        mixer.music.play()

Button(control_frame, text="Start Camera", bg="green", fg="white",
       width=12, command=start_camera).pack(side=LEFT, padx=5)

Button(control_frame, text="Stop Camera", bg="red", fg="white",
       width=12, command=stop_camera).pack(side=LEFT, padx=5)

Button(control_frame, text="Toggle Alarm", bg="orange", fg="white",
       width=12, command=toggle_music).pack(side=LEFT, padx=5)

# ================== الفيديو ==================
def update_frame():
    global sleep_start_time

    if camera_on:
        ret, frame = cap.read()
        if ret:
            frame = imutils.resize(frame, width=450)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            subjects = detect(gray, 0)

            for subject in subjects:
                shape = predict(gray, subject)
                shape = face_utils.shape_to_np(shape)

                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                ear = (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0

                if ear < thresh:
                    if sleep_start_time is None:
                        sleep_start_time = time.time()

                    elapsed = time.time() - sleep_start_time
                    info_label.config(text=f"Eyes Closed Time: {elapsed:.2f} sec")

                    if elapsed >= sleep_time_threshold:
                        cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                        if not mixer.music.get_busy():
                            mixer.music.play()
                else:
                    sleep_start_time = None
                    info_label.config(text="Eyes Closed Time: 0.0 sec")

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            video_label.imgtk = img
            video_label.config(image=img)

    video_label.after(10, update_frame)

# ================== إغلاق آمن ==================
def on_closing():
    cap.release()
    mixer.music.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
update_frame()
root.mainloop()
