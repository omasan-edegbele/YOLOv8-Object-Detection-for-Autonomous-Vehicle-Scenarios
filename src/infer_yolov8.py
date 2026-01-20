from ultralytics import YOLO
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--conf", type=float, default=0.15)
    ap.add_argument("--imgsz", type=int, default=640)
    args = ap.parse_args()

    model = YOLO(args.weights)
    model.predict(args.source, conf=args.conf, imgsz=args.imgsz, save=True)

if __name__ == "__main__":
    main()
