## 1. What does it decode?

Frame scores exported from a CTC recognizer.

## 2. What issue can I investigate?

Check whether consecutive letters collapsed because the model omitted a separating blank.

## 3. Who is the trace for?

Engineers inspecting model output before integrating a recognition pipeline.

## 4. What information is retained?

Every emitted token has a start frame and an exclusive stop frame.

## 5. Which language runs the decoder?

Python implements the command and importable decode function.

## 6. Which framework is required?

Only standard library modules are imported. Export scores from your training framework separately.

## 7. What runtime should I use?

Use Python 3.10 or later with read access to a CSV.

## 8. How do I install it?

Download the source and open its directory. No packages are required.

## 9. How do I choose a blank label?

Use --blank followed by the exact header label.

## 10. How do I run the sample?

Run python decode.py examples/letter.csv.

## 11. Where is the logic?

decode.py contains decoding and CLI handling. tests holds the regression cases.

## 12. In what order are repeats and blanks handled?

Adjacent identical winners merge before blanks disappear from the result.

## 13. Can I use negative logits?

Yes. Only relative ordering within each frame matters.

## 14. How can I save a trace?

Redirect stdout to a JSON file and check the process exit code.

## 15. Can I use subword tokens?

Yes. Each header cell is a token and outputs remain a list.

## 16. What happens on malformed frames?

An invalid number or mismatched score count stops decoding with an error.

## 17. Why is my blank missing from the report?

Blank frames separate runs but have no emitted span of their own.

## 18. How can I diagnose ties?

Inspect the input scores. The earliest column among equal maxima wins.

## 19. How do I run tests?

Execute python -m unittest discover -s tests -v from the repository root.

## 20. How can I contribute?

Provide a minimal frame sequence and an expected trace with the proposed change.

## 21. Does the trace give word timestamps?

Spans use model frames. Time conversion requires the model frame stride and alignment convention.

## 22. Is this a serving system?

It is an offline inspection command. It handles one utterance per file.

## 23. Which extensions are possible?

A beam search implementation could explore sequences overlooked by greedy selection.

## 24. What privacy precautions apply?

Store decoded text and score files with access controls appropriate to the source material.

## 25. Where is the worked example?

README.md explains how the blank in examples/letter.csv preserves a repeated L.

