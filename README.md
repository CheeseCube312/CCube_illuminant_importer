# CCube_illuminant_importer
Turns WebPlotDigitizer-csv files for illuminants into a format my Plotter can use

What it does

    Opens GUI to loads CSV files that use semicolon (;) separators and commas (,) as decimal marks.

    Interpolates the spectral data onto a fixed wavelength range from 300 nm to 1100 nm at 1 nm steps.

    Normalizes the intensities to a relative 0–100 scale.

    Asks for description for the illuminant (optional)

    Saves the result as a tab-separated .tsv file to the folder this .py is in



How to use

    Use WebPlotDigitizer to extract spectral data from a graph and export as .csv.

    Run this script (or a .bat wrapper) and select your exported CSV.

    Enter a short description for the illuminant when prompted.

    The script creates a .tsv file in the same folder as the script.

    Copy or move the generated .tsv file into your filters_data folder to use it in the plotter.



Setup

Just use the .bat file. It creates a virtual environment, installs the libraries and runs the script.

Alternatively you can manually create and activate a Python virtual environment, then install dependencies:
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
pip install pandas numpy


Links

    My plotter: https://github.com/CheeseCube312/CheeseCubes-Filter-Plotter

    WebPlotDigitizer: https://apps.automeris.io/wpd4/
