# Signal Processing and Audio Signal Processor

A collection of projects that delve into the world of signal processing and audio analysis, featuring EEG data analysis and audio signal integrity tools. These projects showcase the application of Python in building effective signal filtering and visualization tools.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Future Enhancements](#future-enhancements)
7. [Contributors](#contributors)
8. [License](#license)

---

## **Overview**

### **Main Project: Signal Processing and Analysis of EEG Data**
Analyze EEG signals to study patterns and characteristics using Python-based signal processing techniques.

### **Derived Project: Audio Signal Integrity Analysis**
An audio-focused application that implements real-time filtering to process and enhance audio signals, such as separating voice from music.

---

## **Key Features**

- **Audio Signal Processing**:
  - Filters to separate voice from music by eliminating beats and tunes.
  - Real-time visualization of filtered signals.
  
- **Filters Implemented**:
  - High-pass, Low-pass, Band-pass, and Notch filters.
  
- **Interactive GUI**:
  - Real-time playback with options to modify filter settings dynamically.
  - Stop and restart playback after adjustments.

- **Signal Analysis**:
  - Frequency spectrum visualization for comparative analysis.
  - EEG signal pattern study using Python tools.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- Recommended IDE: PyCharm, VSCode, or Jupyter Notebook
- Libraries: Install the required libraries using the command:
  ```bash
  pip install -r requirements.txt

Setup
Clone the repository:

``git clone https://github.com/yourusername/signal-processing-projects.git``

Navigate to the project directory:

``cd signal-processing-projects``
Install dependencies:

``pip install -r requirements.txt``
Usage
Run the main script for EEG analysis:
``python eeg_analysis.py``

Run the GUI for audio signal processing:
python audio_processor.py

Filters Available
High-Pass Filter: Removes low-frequency noise.
Low-Pass Filter: Smoothens high-frequency noise.
Band-Pass Filter: Isolates specific frequency ranges.
Notch Filter: Removes specific frequencies (e.g., power line noise).

Controls
Load an audio file and apply filters interactively.
Stop or restart playback to preview changes dynamically.

Technologies Used
Programming Language: Python
Libraries:
numpy, scipy: For signal processing.
matplotlib: For visualization.
tkinter: For GUI development.

Tools:
Audio spectrum visualization.
Filter design and application.

Future Enhancements
Add AI-based adaptive filters for better noise isolation.
Extend EEG analysis for medical diagnostic support.
Incorporate machine learning models for audio classification.
Multi-language GUI support.

Contributors
Your Name (Project Lead)
Geetika Shekhawat, and Jayesh Chauriwar (Collaborators)

License
This project is licensed under the MIT License. See the LICENSE file for details.

