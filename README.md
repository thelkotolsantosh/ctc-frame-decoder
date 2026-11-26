# CTC Frame Decoder

Inspect the greedy token sequence from a speech or handwriting recognition model trained with connectionist temporal classification (CTC). The frame spans help diagnose where repeated letters disappeared or a blank split a run.

## Run the example

Download this repository and open its directory with Python 3.10 or newer. Everything runs locally using the standard library.

```sh
python decode.py examples/letter.csv
python -m unittest discover -s tests -v
```

The sample emits L, L, O across five frames. The first L occupies frames 0 and 1. Frame 2 is blank and allows the second L at frame 3 to survive collapse.

## Use a model export

Supply one CSV per utterance. The first row lists unique token names in model output order. Each subsequent row holds finite numeric scores for one frame in chronological order. Set the blank symbol with --blank (default underscore). Labels are case-sensitive. Ties favor the leftmost column.

The decode function in decode.py reads rows sequentially, selects the highest-scoring token, merges adjacent identical winners and omits blanks. JSON includes tokens and zero-based, half-open frame spans. Invalid input exits with status 2. examples/ contains the sample export and tests/ exercises decoding and validation.

Greedy decoding traces one path. It does not sum scores over alternative paths, infer word boundaries or convert frames to seconds. A future beam decoder could compare alternative sequences. Protect model exports and decoded text as you would the original recordings. See faq.md and CONTRIBUTING.md. MIT licensed.
