import cv2

from cap_from_youtube import cap_from_youtube


youtube_url = 'https://www.youtube.com/watch?v=7kI0tLO0GVw'

cap = cap_from_youtube(youtube_url, '1080p60')

cv2.namedWindow('Visual Tactility', cv2.WINDOW_NORMAL)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Visual Tactility', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break