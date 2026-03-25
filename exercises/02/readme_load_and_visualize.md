# EMG Signal Processing Exercise (Extended Guide)

---

## Overview

In this exercise, you will implement a **complete EMG signal processing pipeline**.

Beyond coding, the goal is to understand:
- how biomedical signals are structured
- how to transform raw data into meaningful information
- why each processing step is necessary

---

## Goal

You will transform raw EMG data into an interpretable signal using:

1. Data loading
2. Reshaping
3. Filtering
4. RMS computation
5. Visualization

---

## Expected Data Structure

The `.pkl` file contains:

- `biosignal` → shape `(channels, window_size, n_windows)`
- `device_information["sampling_frequency"]`

---

## Why is the data 3D?

Real-world systems often stream data in **chunks**:

(channels, samples_per_window, number_of_windows)

Instead of:

(channels, total_samples)

This is efficient for:
- real-time processing
- buffering
- memory management

👉 Your job is to reconstruct a continuous signal.

---

# Step 1 — Loading Data

### What you do
- Load `.pkl` file
- Inspect keys
- Extract signal + sampling rate

### Important concept: Pickle

Pickle stores Python objects exactly:
- dictionaries
- arrays
- nested structures

### Example access pattern

```python
data = pd.read_pickle("file.pkl")

x = data["x"]
z = data["x"]["z"]
```

---

# Step 2 — Reshaping the Signal

### Goal

Convert:

(channels, window_size, n_windows)

→

(channels, total_samples)

---

### Why?

We want:
👉 one continuous signal per channel

Instead of fragmented chunks.

---

### Conceptual view

Before:

Window1 → Window2 → Window3

After:

[W1 | W2 | W3]

---

### How?

You will:
1. reorder axes (transpose)
2. merge dimensions (reshape)

---

### Key idea

You are not changing data — only how it is **organized in memory**.

---

# Step 3 — Bandpass Filtering

---

## Why filtering?

Raw EMG contains:
- motion artifacts (low frequency)
- electrical noise (50 Hz)
- high-frequency noise

We isolate the **physiological signal band**.

---

## EMG Frequency Range

Typical:
- 20 Hz → remove movement artifacts
- 450 Hz → remove high-frequency noise

---

## Nyquist Theorem (CRITICAL)

The highest valid frequency is:

Nyquist = sampling_rate / 2

---

### Example

If sampling_rate = 1000 Hz:

Nyquist = 500 Hz

👉 You cannot filter above 500 Hz

---

## Why validation matters

Bad filter parameters can:
- crash your program
- produce invalid results
- silently corrupt your data

---

## Example: Raising an Error

```python
if x >= y:
    raise ValueError(
        f"Error"
    )
```

---

## What is happening here?

- You check a condition
- If invalid → stop execution
- Provide clear explanation

👉 This is **defensive programming**

---

## Normalization

Filters expect values between 0 and 1:

```python
normalized = frequency / nyquist
```

---

## Butterworth Filter

Why use it?
- smooth response
- no ripples
- widely used in EMG

---

## filtfilt vs lfilter

```python
signal.filtfilt(b, a, data)
```

Advantages:
- zero phase shift
- no time delay

---

# Step 4 — RMS (Root Mean Square)

---

## Why RMS?

EMG is oscillatory:

+ - + - + -

Mean ≈ 0 → useless

👉 RMS gives signal **power / amplitude**

---

## RMS Formula

RMS = sqrt(mean(signal²))

---

## Intuition

- square → remove sign
- average → smooth
- sqrt → restore scale

---

## Why use a window?

We want a **time-varying amplitude**

Not a single value.

---

## Moving Window Concept

Instead of:

RMS of entire signal

We compute:

RMS over short segments (e.g. 100 ms)

---

## Convert ms → samples

Example:

sampling_rate = 1000 Hz  
window = 100 ms = 0.1 s  

→ 100 samples

---

## Example Code Pattern

```python
window_size = int(0.1 * sampling_rate)
kernel = np.ones(window_size) / window_size

squared = signal ** 2
mean = np.convolve(squared, kernel, mode="same")
rms = np.sqrt(mean)
```

---

## Why convolution?

It computes a **moving average efficiently**.

---

# Step 5 — Visualization

---

## Time axis

```python
t = np.arange(n_samples) / sampling_rate
```

---

## Why?

Without time:
- x-axis = sample index
- not meaningful

With time:
- x-axis = seconds
- physically interpretable

---

# Key Learning Points

After this exercise, you should understand:

- how real signals are stored
- how to reshape multi-dimensional data
- why validation is critical
- how filtering works
- what RMS represents
- how signal processing builds meaning from raw data

---

# How to Work

Only modify:

```python
# TODO
```

---

# How to Run

```bash
python emg_student_exercise.py
```

---

# Final Thought

This exercise is the foundation for:

- real-time visualization (VisPy)
- GUI applications (PySide6)
- streaming data (TCP)

👉 Everything in your final project builds on this.
