import cv2
import os

tasks_video = {}

# video = cv2.VideoCapture('videos\\hello_1.mp4')

# if not video.isOpened():
#     print('error')


for root, dirs, files in os.walk('videos'):
    for file in files:
        video = cv2.VideoCapture(file)
        success, img = video.read()
        tasks_video[file[:-4]] = img

for key, value in tasks_video.items():
    print(key, ' -> ', value)


# print(tasks_video)

# while True:
#     success, img = video.read()
#     cv2.imshow("Video", img)
#
#     if cv2.waitKey(25) & 0xFF == ord('u'):
#           break

# ======================================================================================
# === Словарь видео.
# ===



