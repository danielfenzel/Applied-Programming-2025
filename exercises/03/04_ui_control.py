# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy==2.2.4",
#     "scipy==1.15.2",
#     "matplotlib==3.10.1",
#     "pandas==2.2.3",
#     "ipython==9.1.0",
#     "vispy==0.14.3",
#     "pyqt5==5.15.11",
# ]
# ///

import marimo

__generated_with = "0.13.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    return mo, np


@app.cell
def _(mo):
    # Title for Exercise 4
    mo.md("# Live EMG Signal Plotting")
    return


@app.cell
def _(mo):
    # Intro to Live Plotting
    mo.md("""
    ## Exercise 4: Simulated Live Plotting of EMG

    In this exercise, you will learn how to create a live-updating plot of EMG data.
    This simulates how you might visualize EMG signals in a real-time application.

    ### Understanding Windows in Signal Processing

    When working with continuous signals like EMG, we often use different types of windows:

    #### 1. Fixed Windows
    - A fixed window is a segment of the signal with a constant size
    - Example: A 2-second window of EMG data
    - Used for: Analyzing a specific portion of the signal, calculating features over a fixed time period

    #### 2. Moving/Sliding Windows
    - A moving window slides across the signal, analyzing overlapping segments
    - Example: A 2-second window that moves forward by 0.1 seconds each time
    - Used for: Real-time processing, continuous monitoring, feature extraction over time

    #### 3. Overlapping vs. Non-overlapping Windows
    - Overlapping: Windows share some data points (e.g., 90% overlap)
    - Non-overlapping: Windows are adjacent but don't share data points
    - Overlapping provides smoother transitions and better temporal resolution

    ### Real-time Visualization with Moving Windows

    For real-time visualization, we use a moving window approach:
    1. Display a fixed-size window of the most recent data
    2. As new data arrives, the window "slides" forward
    3. Old data exits the window as new data enters
    4. This creates the illusion of a continuous, real-time display

    This approach is essential for:
    - Monitoring EMG signals during experiments
    - Real-time biofeedback applications
    - Interactive signal processing systems

    ### Why Use PyQt5 for Live Plotting?

    PyQt5 is a powerful framework for creating desktop applications with graphical user interfaces. 
    We use it for live plotting because:

    1. **Standalone Application**: It allows us to create a standalone window that can run independently of Jupyter notebooks
    2. **Responsive UI**: PyQt5 provides a responsive user interface that can handle real-time updates
    3. **Integration with Matplotlib**: It integrates well with Matplotlib for plotting, allowing us to create interactive visualizations
    4. **Custom Controls**: We can add custom controls (buttons, sliders, etc.) to interact with the visualization
    5. **Professional Look**: It provides a professional-looking application that can be distributed to users

    ### Learning Objectives:
    - Load and structure EMG data
    - Create a sliding window visualization
    - Implement a live-updating plot using PyQt5 and Matplotlib
    - Understand the concept of real-time data visualization

    ### Tasks:
    1. Load the EMG data from the pickle file
    2. Restructure the data for continuous plotting
    3. Create a PyQt5 window with a matplotlib canvas
    4. Implement a live-updating plot with both raw and filtered signals
    """)
    return


@app.cell
def _(mo):
    # Step 1: Loading the Data
    mo.md("""
    ## Step 1: Loading the Data

    First, let's load the EMG data from the pickle file. The data contains:
    - `biosignal`: The EMG data in a 3D array format (channels × windowsize × window)
    - `device_information`: Contains metadata about the recording, including the sampling rate

    TODO:
    1. Load the data from the pickle file 'recording.pkl' using pandas
    2. Extract the EMG signal and sampling rate from the data dictionary
    3. Print information about the data structure to verify it was loaded correctly

    Hint: Use pd.read_pickle() to load the data and access dictionary keys using square brackets
    """)
    return


@app.cell
def _():
    # Code cell for loading data
    # TODO: Load the data from the pickle file
    data = None  # Replace with your code

    # TODO: Extract the EMG signal and sampling rate
    emg_signal = None  # Replace with your code
    sampling_rate = None  # Replace with your code

    # Display basic information about the data structure
    print("Data structure:")
    print("-" * 50)
    print(f"Data type: {type(data)}")
    print(f"Data shape: {data.shape if hasattr(data, 'shape') else 'N/A'}")
    print("\nAvailable keys in data:")
    print("-" * 50)
    for key in data.keys():
        print(f"- {key}")
    print("-" * 50)

    # Display information about the EMG signal
    print("\nEMG Signal information:")
    print("-" * 50)
    print(f"Signal shape: {emg_signal.shape}")
    print(f"Number of channels: {emg_signal.shape[0]}")
    print(f"Window size: {emg_signal.shape[1]}")
    print(f"Number of windows: {emg_signal.shape[2]}")
    print(f"Sampling rate: {sampling_rate} Hz")
    return emg_signal, sampling_rate


@app.cell
def _(mo):
    # Step 2: Reconstructing the EMG Signal
    mo.md("""
    ## Step 2: Reconstructing the EMG Signal

    Now that we understand the data structure, we need to restructure the EMG signal.
    Currently, it's in the format: channels × windowsize × window

    TODO:
    1. Get the number of channels from the EMG signal shape
    2. Transpose the data to get windows × samples × channels
    3. Reshape to combine all windows for each channel
    4. Transpose back to get channels × samples

    Hint: Use numpy's transpose() and reshape() functions. The final shape should be (channels, total_samples)
    """)
    return


@app.cell
def _(emg_signal, num_channels):
    # Code cell for restructuring EMG data
    # TODO: Get the number of channels
    # num_channels = ...  # Replace with your code

    # TODO: Restructure the data
    channel_data = None  # Replace with your code

    print("\nRestructured EMG Data:")
    print("-" * 50)
    print(f"Original shape: {emg_signal.shape}")
    print(f"New shape: {channel_data.shape}")
    print(f"Number of channels: {num_channels}")
    print(f"Total samples per channel: {channel_data.shape[1]}")
    return (channel_data,)


@app.cell
def _(mo):
    # PyQt Guide
    mo.md("""
    ## PyQt Guide: Understanding Layouts and Widgets

    Before we create our EMG signal viewer, let's understand the basics of PyQt5, which is a powerful framework for creating desktop applications with graphical user interfaces.

    ### What is PyQt5?

    PyQt5 is a set of Python bindings for the Qt framework, which is a comprehensive set of tools for building cross-platform applications. It provides:

    - **Widgets**: UI elements like buttons, text fields, and plots
    - **Layouts**: Ways to arrange widgets in a window
    - **Signals and Slots**: A mechanism for communication between widgets
    - **Event Handling**: Ways to respond to user interactions

    ### Basic PyQt5 Structure

    A typical PyQt5 application consists of:

    1. **Application Object**: The core of any PyQt application
    2. **Main Window**: The top-level window that contains all other widgets
    3. **Widgets**: UI elements that are arranged in the window
    4. **Layouts**: Managers that arrange widgets in a specific way

    ### Essential Imports

    ```python
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
    import sys
    ```

    ### Creating a Basic Window

    ```python
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    window.setWindowTitle("My Application")
    window.setGeometry(100, 100, 800, 600)  # x, y, width, height
    ```

    ### Layouts in PyQt5

    Layouts are used to arrange widgets in a window. The most common layouts are:

    #### 1. QVBoxLayout (Vertical Layout)

    A vertical layout arranges widgets in a column, one below the other.

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

    #### 2. QHBoxLayout (Horizontal Layout)

    A horizontal layout arranges widgets in a row, one next to the other.

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

    #### 3. QGridLayout (Grid Layout)

    A grid layout arranges widgets in a grid of rows and columns.

    ```
    +-------+-------+
    |Widget1|Widget2|
    +-------+-------+
    |Widget3|Widget4|
    +-------+-------+
    ```

    ```python
    layout = QGridLayout()
    layout.addWidget(widget1, 0, 0)  # row 0, column 0
    layout.addWidget(widget2, 0, 1)  # row 0, column 1
    layout.addWidget(widget3, 1, 0)  # row 1, column 0
    layout.addWidget(widget4, 1, 1)  # row 1, column 1
    ```

    #### 4. Nested Layouts

    You can nest layouts to create complex arrangements.

    ```
    +------------------+
    |     Widget 1     |
    +------------------+
    |  +----+----+    |
    |  |W2  |W3  |    |
    |  +----+----+    |
    |     Widget 4     |
    +------------------+
    ```

    ```python
    # Main vertical layout
    main_layout = QVBoxLayout()
    main_layout.addWidget(widget1)

    # Nested horizontal layout
    h_layout = QHBoxLayout()
    h_layout.addWidget(widget2)
    h_layout.addWidget(widget3)

    # Add the horizontal layout to the main layout
    main_layout.addLayout(h_layout)
    main_layout.addWidget(widget4)
    ```

    ### Common Widgets in PyQt5

    - **QPushButton**: A clickable button
    ```python
    button = QPushButton("Click Me")
    button.clicked.connect(some_function)  # Connect to a function
    ```

    - **QLabel**: A text or image label
    ```python
    label = QLabel("Hello World")
    ```

    - **QLineEdit**: A single-line text input
    ```python
    text_input = QLineEdit()
    text_input.setPlaceholderText("Enter text here")
    ```

    - **QComboBox**: A dropdown selection box
    ```python
    combo = QComboBox()
    combo.addItems(["Option 1", "Option 2", "Option 3"])
    ```

    - **QSlider**: A slider for selecting a value
    ```python
    slider = QSlider(Qt.Horizontal)
    slider.setMinimum(0)
    slider.setMaximum(100)
    ```

    - **QCheckBox**: A checkbox for toggling options
    ```python
    checkbox = QCheckBox("Enable feature")
    checkbox.setChecked(True)
    ```

    - **QRadioButton**: A radio button for selecting one option from many
    ```python
    radio1 = QRadioButton("Option 1")
    radio2 = QRadioButton("Option 2")
    radio1.setChecked(True)
    ```

    ### Signals and Slots

    PyQt5 uses a signals and slots mechanism for communication between widgets:

    ```python
    # Create a button
    button = QPushButton("Plot Data")

    # Connect the button's clicked signal to a function
    button.clicked.connect(plot_function)

    def plot_function():
        # This function will be called when the button is clicked
        ax.clear()
        ax.plot(data)
        canvas.draw()
    ```

    ### Integrating Matplotlib with PyQt5

    For our EMG signal viewer, we'll integrate Matplotlib with PyQt5 using the `FigureCanvas` widget:

    ```python
    # Create a Matplotlib figure
    fig = Figure(figsize=(8, 6))
    ax = fig.add_subplot(111)

    # Create a canvas and add it to the layout
    canvas = FigureCanvas(fig)
    layout.addWidget(canvas)

    # Example of updating the plot
    def update_plot():
        ax.clear()
        ax.plot(data)
        ax.set_title("My Plot")
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        canvas.draw()
    ```

    ### Running the Application

    ```python
    # Show the window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
    ```

    ### Complete Example

    Here's a simple example that combines all these concepts:

    ```python
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
    import sys
    import numpy as np

    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    window.setWindowTitle("Simple Plot Viewer")
    window.setGeometry(100, 100, 800, 600)

    # Create central widget and layout
    central_widget = QWidget()
    window.setCentralWidget(central_widget)
    layout = QVBoxLayout(central_widget)

    # Create a button
    button = QPushButton("Plot Sine Wave")

    # Create matplotlib figure and canvas
    fig = Figure(figsize=(8, 6))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)

    # Add widgets to layout
    layout.addWidget(button)
    layout.addWidget(canvas)

    # Define plotting function
    def plot_sine():
        ax.clear()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        canvas.draw()

    # Connect button to function
    button.clicked.connect(plot_sine)

    # Show window and start application
    window.show()
    sys.exit(app.exec_())
    ```

    Now that we understand the basics of PyQt5, let's create our EMG signal viewer!
    """)
    return


@app.cell
def _(mo):
    # Step 3: Creating the PyQt Widget
    mo.md("""
    ## Step 3: Creating the PyQt Widget

    Now, let's create a PyQt5 window that will contain our EMG signal viewer.

    TODO:
    1. Create the main window:
       - Create a QMainWindow with title "EMG Signal Viewer"
       - Set window size to 800x600 pixels
       Hint: Use setWindowTitle() and setGeometry()

    2. Create the UI layout:
       - Create a central widget
       - Create a vertical layout (QVBoxLayout)
       - Create three buttons for different signal views:
         * "Show Original Signal"
         * "Show Filtered Signal"
         * "Show RMS Signal"
       Hint: Use QWidget() for central widget and QVBoxLayout() for layout

    3. Set up the plotting area:
       - Create a matplotlib Figure
       - Create a FigureCanvas
       - Add a subplot to the figure
       - Add the canvas to the layout
       Hint: Use Figure() and FigureCanvas()

    4. Connect the buttons to their respective functions
       Hint: Use clicked.connect() for each button

    The plotting functions are provided for you below. You just need to create the UI and connect the buttons to these functions.
    """)
    return


@app.cell
def _(channel_data, np, sampling_rate, win):
    # Code cell for creating a PyQt5 window
    from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
    import sys
    from scipy import signal

    # Define plotting functions (provided for you)
    def plot_original():
        ax.clear()
        t = np.arange(channel_data.shape[1]) / sampling_rate
        ax.plot(t, channel_data[20, :])
        ax.set_title("Original EMG Signal")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        canvas.draw()

    def plot_filtered():
        ax.clear()
        t = np.arange(channel_data.shape[1]) / sampling_rate
        # Apply bandpass filter
        nyquist = sampling_rate / 2
        low = 20 / nyquist
        high = 450 / nyquist
        b, a = signal.butter(4, [low, high], btype='band')
        filtered_data = signal.filtfilt(b, a, channel_data[20, :])
        ax.plot(t, filtered_data)
        ax.set_title("Filtered EMG Signal")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        canvas.draw()

    def plot_rms():
        ax.clear()
        t = np.arange(channel_data.shape[1]) / sampling_rate
        # Calculate RMS with 100ms window
        window_size = int(0.1 * sampling_rate)
        squared = channel_data[20, :] ** 2
        window = np.ones(window_size) / window_size
        rms = np.sqrt(np.convolve(squared, window, mode='same'))
        ax.plot(t, rms)
        ax.set_title("RMS EMG Signal")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        canvas.draw()

    # Create the Qt application instance
    app = QApplication(sys.argv)

    # TODO: Create the main window
    # win = ...


    # TODO: Create the central widget and layout
    # central_widget = ...


    # TODO: Create the buttons


    # TODO: Create the matplotlib figure and canvas
    fig = ...
    canvas = ...
    ax = ...

    # TODO: Add widgets to the layout


    # TODO: Connect buttons to their respective functions


    # Show initial plot
    plot_original()

    # Show the window
    win.show()

    # Start the application event loop
    sys.exit(app.exec_())

    print("PyQt5 window created successfully.")
    return


if __name__ == "__main__":
    app.run()
