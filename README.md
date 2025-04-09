# PULSE — Prompt Utilization for Library-based Synthesis Enhancement

## Overview

PULSE is a system that builds a library of prompts for solving program synthesis tasks. It uses LangChain to interact with LLMs to break down tasks, generate building blocks, and create Python Turtle programs to draw images based on descriptions.

## Project Structure

```
.
├── Data/
│   ├── logo_data/       # Contains logo images
│   └── input.json       # Input data with image descriptions and labels
├── library/
│   ├── library.json     # Library of prompts for building blocks
│   ├── circle.py        # Example circle building block
│   └── hexagon.py       # Example hexagon building block
├── output/              # Generated Python Turtle programs
├── src/
│   └── main.py          # Main implementation of the PULSE system
├── add_building_block.py # Script to add a new building block to the library
├── batch_process.py     # Script to process a batch of image descriptions
├── create_input.py      # Script to create a new input JSON file
├── example.py           # Example script to demonstrate how to use the system
├── export_library.py    # Script to export the library to a JSON file
├── import_library.py    # Script to import a library from a JSON file
├── run_custom_pulse.py  # Script to run the system with all customizations combined
├── run_pulse.py         # Script to run the PULSE system
├── run_turtle_program.py # Script to run a generated Turtle program
├── run_with_custom_input.py # Script to run the system with a custom input file
├── run_with_custom_library.py # Script to run the system with a custom library path
├── run_with_custom_output.py # Script to run the system with a custom output directory
├── run_with_custom_prompt.py # Script to run the system with custom prompt templates
├── run_with_model.py    # Script to run the system with a specific OpenAI model
├── test_pulse.py        # Script to test the PULSE system with a single image
├── view_library.py      # Script to view the contents of the library
├── visualize_library.py # Script to visualize the library structure
└── requirements.txt     # Project dependencies
```

## Setup

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```
   Or provide it when prompted by the program.

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
   python run_turtle_program.py output/img_0.py
   ```

### Utility Scripts

PULSE comes with several utility scripts to help you work with the system:

- **run_pulse.py**: Run the PULSE system with command-line arguments
  ```
  python run_pulse.py --api-key your_api_key_here --input Data/input.json
  ```

- **test_pulse.py**: Test the PULSE system with a single image description
  ```
  python test_pulse.py
  ```

- **batch_process.py**: Process a batch of image descriptions from a JSON file
  ```
  python batch_process.py --input Data/input.json
  ```

- **create_input.py**: Create a new input JSON file with image descriptions
  ```
  python create_input.py --output Data/new_input.json
  ```

- **view_library.py**: View the contents of the PULSE library
  ```
  python view_library.py
  ```

- **visualize_library.py**: Generate a visualization of the library structure
  ```
  python visualize_library.py --output library_visualization.md
  ```

- **add_building_block.py**: Add a new building block to the library
  ```
  python add_building_block.py
  ```

- **export_library.py**: Export the library to a JSON file for sharing
  ```
  python export_library.py --output library_export.json --include-programs
  ```

- **import_library.py**: Import a library from a JSON file
  ```
  python import_library.py library_export.json --overwrite
  ```

- **run_with_custom_input.py**: Run the PULSE system with a custom input file
  ```
  python run_with_custom_input.py --input Data/custom_input.json
  ```

- **run_with_custom_library.py**: Run the PULSE system with a custom library path
  ```
  python run_with_custom_library.py --library custom_library/library.json
  ```

- **run_with_custom_output.py**: Run the PULSE system with a custom output directory
  ```
  python run_with_custom_output.py --output custom_output
  ```

- **run_with_custom_prompt.py**: Run the PULSE system with custom prompt templates
  ```
  python run_with_custom_prompt.py
  ```

- **run_with_model.py**: Run the PULSE system with a specific OpenAI model
  ```
  python run_with_model.py --model gpt-3.5-turbo --temperature 0.5
  ```

- **run_custom_pulse.py**: Run the PULSE system with all customizations combined
  ```
  python run_custom_pulse.py --model gpt-3.5-turbo --temperature 0.5 --library custom_library/library.json --input Data/custom_input.json --output custom_output
  ```

- **run_turtle_program.py**: Run a generated Turtle program
  ```
  python run_turtle_program.py output/img_0.py
  ```

## How It Works

PULSE follows a four-stage process:

1. **Stage One**: Break down the task based on the image description and label.
2. **Stage Two**: Search the library for building blocks or treat the entire image as a building block.
3. **Stage Three**: Generate programs for missing building blocks and add them to the library.
4. **Stage Four**: Generate the final program that draws the original image.

The system maintains a library of prompts for drawing building blocks, which grows over time as new building blocks are encountered.

## Extending the Library

You can extend the library of building blocks in several ways:

1. **Automatically**: The system will automatically add new building blocks to the library when it encounters them during processing.

2. **Manually**: You can use the `add_building_block.py` script to add a new building block to the library.

3. **Importing**: You can import building blocks from a JSON file using the `import_library.py` script.

## Sharing Your Library

You can share your library of building blocks with others by exporting it to a JSON file using the `export_library.py` script. Others can then import your library using the `import_library.py` script.

## Customizing PULSE

PULSE is designed to be customizable to suit your specific needs. Here are some ways you can customize the system:

### Custom Models

You can use different OpenAI models with PULSE by using the `run_with_model.py` script. This allows you to experiment with different models to find the one that works best for your use case.

```
python run_with_model.py --model gpt-3.5-turbo --temperature 0.5
```

### Custom Prompts

You can customize the prompts used by PULSE to guide the LLM in generating building blocks and programs. The `run_with_custom_prompt.py` script demonstrates how to override the default prompt templates with your own.

```
python run_with_custom_prompt.py
```

### Custom Building Blocks

You can add your own building blocks to the library using the `add_building_block.py` script. This allows you to extend the library with your own custom shapes and patterns.

```
python add_building_block.py
```

### Custom Input Data

You can create your own input data with custom image descriptions using the `create_input.py` script. This allows you to test the system with your own descriptions.

```
python create_input.py --output Data/custom_input.json
```

### Multiple Libraries

You can use multiple libraries with PULSE by using the `run_with_custom_library.py` script. This allows you to test different library configurations or maintain separate libraries for different purposes.

```
python run_with_custom_library.py --library custom_library/library.json
```

The script will automatically create a copy of the default library if the specified library doesn't exist, or create a new empty library if the default library doesn't exist.

### Custom Output Directories

You can organize your generated programs in different directories by using the `run_with_custom_output.py` script. This allows you to keep your outputs organized by project, date, or any other criteria.

```
python run_with_custom_output.py --output custom_output
```

The script will automatically create the output directory if it doesn't exist.

### Combining Customizations

You can combine all the customization options by using the `run_custom_pulse.py` script. This allows you to use a custom model, temperature, library path, input file, and output directory all at once.

```
python run_custom_pulse.py --model gpt-3.5-turbo --temperature 0.5 --library custom_library/library.json --input Data/custom_input.json --output custom_output
```

The script will automatically create the necessary directories and files if they don't exist.
