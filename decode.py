"""Trace greedy CTC decoding from frame-level scores in CSV."""
import argparse
import csv
import json
import math


def decode(stream, blank="_"):
    rows = csv.reader(stream, strict=True)
    labels = next(rows, [])
    if blank not in labels or len(set(labels)) != len(labels) or not all(labels):
        raise ValueError("header needs unique nonempty labels including blank")
    spans = []
    previous = None
    frames = 0
    for frame, row in enumerate(rows):
        if len(row) != len(labels):
            raise ValueError(f"wrong score count at frame {frame}")
        try:
            scores = list(map(float, row))
        except ValueError as exc:
            raise ValueError(f"invalid number at frame {frame}") from exc
        if not all(map(math.isfinite, scores)):
            raise ValueError(f"nonfinite score at frame {frame}")
        label = labels[max(range(len(scores)), key=scores.__getitem__)]
        if label != blank:
            if label != previous:
                spans.append({"token": label, "start": frame, "stop": frame + 1})
            else:
                spans[-1]["stop"] = frame + 1
        previous = label
        frames += 1
    return {"frames": frames, "tokens": [s["token"] for s in spans], "spans": spans}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv")
    parser.add_argument("--blank", default="_")
    args = parser.parse_args()
    try:
        with open(args.csv, encoding="utf-8-sig", newline="") as stream:
            print(json.dumps(decode(stream, args.blank), indent=2))
    except (OSError, ValueError, csv.Error) as exc:
        parser.exit(2, f"decode error: {exc}\n")
