# Week 9 -- Variance Study Results

## Why we did this

In the original bubble sort benchmark the n=30,000 timing looked wrong
(35.0 s in one run against 23.8 s in another, so the 20k -> 30k ratio came out
near 3.4x instead of 2.25x). This study sorts the same list 20 times at three
sizes so that any spread is timer and machine noise, not algorithmic or data
variance.

## Results by size

```
=== VARIANCE STUDY: n=5,000 (20 trials) ===
min:     0.6168s   trial #9
max:     0.6564s   trial #1
mean:    0.6272s
median:  0.6215s
std dev: 0.0130s
CV:      2.07%   <-- coefficient of variation
range:   0.0396s

trial 1: 0.6564s
trial 2: 0.6503s
trial 3: 0.6494s
trial 4: 0.6498s
trial 5: 0.6284s
trial 6: 0.6307s
trial 7: 0.6188s
trial 8: 0.6197s
trial 9: 0.6168s
trial 10: 0.6225s
trial 11: 0.6185s
trial 12: 0.6174s
trial 13: 0.6182s
trial 14: 0.6205s
trial 15: 0.6243s
trial 16: 0.6190s
trial 17: 0.6172s
trial 18: 0.6198s
trial 19: 0.6235s
trial 20: 0.6236s

=== VARIANCE STUDY: n=10,000 (20 trials) ===
min:     2.5098s   trial #19
max:     2.6579s   trial #1
mean:    2.5667s
median:  2.5639s
std dev: 0.0392s
CV:      1.53%   <-- coefficient of variation
range:   0.1480s

trial 1: 2.6579s
trial 2: 2.5529s
trial 3: 2.5909s
trial 4: 2.5686s
trial 5: 2.5934s
trial 6: 2.5979s
trial 7: 2.5515s
trial 8: 2.5883s
trial 9: 2.6068s
trial 10: 2.6061s
trial 11: 2.5592s
trial 12: 2.6079s
trial 13: 2.5324s
trial 14: 2.5239s
trial 15: 2.5532s
trial 16: 2.5699s
trial 17: 2.5174s
trial 18: 2.5147s
trial 19: 2.5098s
trial 20: 2.5310s

=== VARIANCE STUDY: n=30,000 (20 trials) ===
min:     23.0040s   trial #12
max:     24.9556s   trial #16
mean:    24.1859s
median:  24.3270s
std dev: 0.6423s
CV:      2.66%   <-- coefficient of variation
range:   1.9515s

trial 1: 24.6742s
trial 2: 23.7964s
trial 3: 24.8445s
trial 4: 24.4652s
trial 5: 24.2486s
trial 6: 24.9386s
trial 7: 24.1310s
trial 8: 24.3814s
trial 9: 23.7209s
trial 10: 23.1128s
trial 11: 23.1664s
trial 12: 23.0040s
trial 13: 23.8836s
trial 14: 24.6681s
trial 15: 24.8899s
trial 16: 24.9556s
trial 17: 24.2726s
trial 18: 23.3319s
trial 19: 24.6357s
trial 20: 24.5972s
```

## What the data actually showed

- The "small jobs are noisier" prediction did **not** hold cleanly: CV was
  2.07 % at n=5,000, 1.53 % at n=10,000, and 2.66 % at n=30,000. With one
  20-trial run per size, those differences are not strong evidence either way.
- Trial 1 was the slowest at n=5,000 and n=10,000, which fits warm-up effects
  (and the 5,000 case drifts down over the first dozen trials).
- Typical run-to-run spread at n=30,000 was 23.0-25.0 s. The original
  benchmark's 35.0 s is far outside that range, so it was a one-off
  interference event (a `pip install` was running at the time), not ordinary
  timer noise.

## Why the numbers lie

The operating system can pause a running sort at any moment to service a timer interrupt, a network packet, or an antivirus scan, and perf_counter() keeps counting while we are paused. A fixed-size interruption is a large fraction of a short job and a small fraction of a long one, so small n tends to show a HIGH coefficient of variation and large n a LOW one. The first trial may also run slower or faster than later ones because of CPU cache and branch predictor warm-up, and a long run of sorts can heat the chip until it lowers its clock speed, which makes later trials slower on identical data. Python's garbage collector can pause execution too, though bubble sort allocates almost nothing, so it is an unlikely culprit here. Other programs matter most of all: in our original benchmark the 20,000 to 30,000 row came out near 3.4x instead of the theoretical 2.25x because a pip install was running during that measurement and stealing CPU time, which is an extreme case of the same scheduling noise. This study cannot say which cause hit which trial; it only measures how big the spread is.

## Comparison table

```
      n |  mean (s) |    CV% | interpretation
--------+-----------+--------+-----------------------------------------
  5,000 |    0.6272 |  2.07% | baseline; a short job, so fixed-size hiccups loom large
 10,000 |    2.5667 |  1.53% | medium; a few seconds per trial
 30,000 |   24.1859 |  2.66% | large; long job, hiccups should be a small fraction
```

## World Bible entry

```
Adds: repeated timing of bubble sort, coefficient of variation, and a noise explanation.
Finding: highest CV at n=30,000 (2.66%), lowest at n=10,000 (1.53%). Short jobs are expected to be noisier, because a fixed hiccup is a bigger share of them; compare the numbers above to that prediction.
Debt: this measured timer noise on one fixed list, not algorithmic variance; repeating with different seeds is a separate study.
```
