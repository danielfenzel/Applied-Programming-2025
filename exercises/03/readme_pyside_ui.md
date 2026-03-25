# Exercise 3 — PySide6 UI Programming & Embedded Matplotlib

---

## Overview

In this exercise, you will learn how to build a **desktop application** using **PySide6** and integrate it with Matplotlib for signal visualization.

This is a key transition in the course:

* From **scripts → applications**
* From **static plots → interactive UI**
* From **sequential code → event-driven programming**

---

## Why GUI Programming?

So far, your programs:

* run once
* produce output
* exit

Now we want:

* persistent applications
* user interaction
* dynamic updates

👉 This is exactly what GUIs enable.

---

## What is PySide6?

PySide6 is the **official Python binding of Qt**, a powerful cross-platform UI framework.

It provides:

* **Widgets** → UI elements (buttons, dropdowns, labels)
* **Layouts** → how elements are arranged
* **Signals & Slots** → communication between components
* **Event loop** → handles user interaction

---

## Structure of a PySide6 Application

Every PySide6 application has the same core structure:

### 1. Create the application

```python
app = QApplication(sys.argv)
```

* Manages the **event loop**
* Required for every GUI app

---

### 2. Create the main window

```python
window = QMainWindow()
```

This is the **top-level container**.

---

### 3. Add a central widget

```python
central_widget = QWidget()
window.setCentralWidget(central_widget)
```

👉 Important:

* `QMainWindow` **cannot directly contain layouts**
* Everything goes inside a `QWidget`

---

### 4. Create layouts

Layouts control how widgets are arranged.

---

## Layouts in Detail

### QVBoxLayout (Vertical Layout)

Arranges widgets top to bottom:

```
+------------------+
|     Widget 1     |
+------------------+
|     Widget 2     |
+------------------+
|     Widget 3     |
+------------------+
```

```python
layout = QVBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)
layout.addWidget(widget3)
```

---

### QHBoxLayout (Horizontal Layout)

Arranges widgets side by side:

```
+-------+-------+-------+
|Widget1|Widget2|Widget3|
+-------+-------+-------+
```

```python
layout = QHBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)
layout.addWidget(widget3)
```

---

### Nested Layouts (Very Important)

You can combine layouts:

```
+------------------------+
|     Plot Area          |
+------------------------+
| Channel | Signal | Btn |
+------------------------+
```

```python
main_layout = QVBoxLayout()
controls_layout = QHBoxLayout()

controls_layout.addWidget(widget1)
controls_layout.addWidget(widget2)

main_layout.addLayout(controls_layout)
main_layout.addWidget(plot_widget)
```

👉 Standard pattern:

* Vertical layout → overall structure
* Horizontal layout → control row

---

## Common Widgets

### QLabel (Text)

```python
label = QLabel("Channel:")
```

---

### QComboBox (Dropdown)

```python
combo = QComboBox()
combo.addItems(["Option 1", "Option 2"])
```

Used for:

* channel selection
* signal type selection

---

### QPushButton (Button)

```python
button = QPushButton("Change Color")
```

Used for:

* triggering actions
* user interaction

---

## Signals and Slots (Core Concept)

This is the **most important concept in GUI programming**.

Instead of calling functions directly:

```python
do_something()
```

We connect events to functions:

```python
button.clicked.connect(do_something)
```

👉 Meaning:

> “When this event happens → execute this function”

---

## Signals vs Slots

| Concept | Meaning                    |
| ------- | -------------------------- |
| Signal  | Something happened (event) |
| Slot    | Function that reacts to it |

---

### Example

```python
button.clicked.connect(update_plot)
```

* `clicked` → signal (event)
* `update_plot` → slot (function)

---

### Multiple Signals

You can connect multiple UI elements to the same function:

```python
combo.currentIndexChanged.connect(update_plot)
button.clicked.connect(update_plot)
```

👉 This is very powerful:

* one function controls the logic
* multiple UI elements trigger it

---

### Important Mental Model

GUI code works like this:

```text
WAIT → EVENT → FUNCTION → UPDATE UI
```

NOT like this:

```text
RUN → FINISH
```

---

## Event-Driven Programming

Unlike normal scripts:

❌ Code does NOT run once from top to bottom

Instead:

* program waits
* user interacts
* program reacts

Examples:

* button click
* dropdown change
* slider movement

👉 This is called **event-driven programming**

---

## Integrating Matplotlib into PySide6

Normally, Matplotlib opens its own window.

We embed it into the UI:

```python
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
```

---

### Setup

```python
fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
```

Add to layout:

```python
layout.addWidget(canvas)
```

---

### Updating the Plot

```python
ax.clear()
ax.plot(x, y)
canvas.draw()
```

---

## Your Task in This Exercise

You will implement the UI by completing the TODOs.

### Step-by-step tasks

### 1. Window Setup

* Set window title
* Set window size

---

### 2. Central Widget

* Create `QWidget`
* Assign it using `setCentralWidget()`

---

### 3. Layouts

* Create:

  * `QVBoxLayout` → main layout
  * `QHBoxLayout` → control layout

---

### 4. Channel Selection

* Create `QLabel`
* Create `QComboBox`
* Fill with:

  ```
  Channel 1, Channel 2, ...
  ```

---

### 5. Signal Selection

* Create dropdown with:

  ```
  Original, Filtered, RMS
  ```

---

### 6. Button

* Create:

  ```
  QPushButton("Change Color")
  ```

---

### 7. Layout Assembly

* Add all controls to horizontal layout
* Add horizontal layout to vertical layout

---

### 8. Matplotlib Integration

* Create:

  * `Figure`
  * `FigureCanvas`
  * `Axes`
* Add canvas to layout

---

### 9. Connect Signals

Connect:

```python
channel_combo.currentIndexChanged → update_plot
signal_combo.currentIndexChanged → update_plot
color_button.clicked → change_color
```

---

### 10. Initial Plot

* Call `update_plot()` once

---

## Interaction Flow

1. User selects channel

2. User selects signal type

3. Plot updates automatically

4. User clicks button
   → plot color changes

---

## Why This Matters

This exercise teaches:

* UI structure
* layout composition
* event-driven logic
* interaction design

These are essential for:

👉 Exercise 4 (VisPy real-time plotting)
👉 Final project (full application with TCP + MVVM)

---

## Key Takeaway

👉 GUI programming is **event-driven**, not sequential.

This is the most important conceptual shift in this exercise.
