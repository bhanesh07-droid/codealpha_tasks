# Task 4 Explanation

### Pipeline
Webcam/video → OpenCV frame stream → YOLO detection → bounding boxes/classes → ByteTrack → persistent tracking IDs → annotated video.

### Detection
YOLO identifies objects and produces bounding boxes with class labels and confidence.

### Tracking
ByteTrack associates detections across frames so the same object can retain a tracking ID over time.

### Extensions
- Deep SORT
- Object counting
- Line-crossing analytics
- Speed estimation
- Custom YOLO training
- Edge deployment
