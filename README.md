# PULSE — Prompt Utilization for Library-based Synthesis Enhancement

## Overview

PULSE is a system that builds a library of prompts for solving program synthesis tasks. It uses LangChain to interact with LLMs to break down tasks, generate building blocks, and create Python Turtle programs to draw images based on descriptions.


## Setup

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key in a `.env` file in the roof of the project: 
   ```
   OPENAI_API_KEY=YOUR_API_KEY
   ```

## Usage

### Basic Usage

1. Prepare your input data in `Data/input.json` with the following format:
   ```json
   [
     {
       "file_name": "img_0.png",
       "label": "compositional",
       "description": "a small hexagon separated by a big space from a small circle"
     },
     ...
   ]
   ```

2. Run the PULSE system:
   ```
   python run_pulse.py
   ```

3. The system will process each image description and generate Python Turtle programs in the `output/` directory.

4. Run the generated programs to see the drawings:
   ```
   python output/img_0.py
   ```


## How It Works

PULSE follows a four-stage process:

1. **Stage One**: Break down the task based on the image description and label.
2. **Stage Two**: Search the library for building blocks or treat the entire image as a building block.
3. **Stage Three**: Generate programs for missing building blocks and add them to the library.
4. **Stage Four**: Generate the final program that draws the original image.

The system maintains a library of prompts for drawing building blocks, which grows over time as new building blocks are encountered.
