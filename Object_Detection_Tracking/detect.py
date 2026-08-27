
import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="YOLO object detection")
    parser.add_argument("--source", default="0", help="0 for webcam, or path to image/video")
    parser.add_argument("--model", default="yolo26n.pt")
    parser.add_argument("--conf", type=float, default=0.35)
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    model = YOLO(args.model)
    model.predict(source=source, conf=args.conf, show=True)

if __name__ == "__main__":
    main()
