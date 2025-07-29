import cv2

video = cv2.VideoCapture("cars_video.mp4")
if not video.isOpened():
    print("Video not found.")
    exit()

ret, frame = video.read()
if not ret:
    print("Could not read the first frame from the video.")
    exit()

bbox = cv2.selectROI("Select object to track", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select object to track")

if bbox == (0, 0, 0, 0):
    print("No object selected. Exiting.")
    exit()

try:
    tracker = cv2.TrackerCSRT_create()
except AttributeError:
    tracker = cv2.legacy.TrackerCSRT_create()

tracker.init(frame, bbox)

output = cv2.VideoWriter("output.mp4",
                         cv2.VideoWriter_fourcc(*"mp4v"),
                         video.get(cv2.CAP_PROP_FPS),
                         (frame.shape[1], frame.shape[0]))

while True:
    ret, frame = video.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # تصغير الإطار قبل العرض
    small_frame = cv2.resize(frame, (640, 360))
    cv2.imshow("Object Tracking", small_frame)
    output.write(frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
output.release()
cv2.destroyAllWindows()
