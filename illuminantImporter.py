import os
import pandas as pd
import numpy as np
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# Constants
SCRIPT_DIR = Path(__file__).parent.resolve()

def parse_webplot_csv(path):
    """
    Load and parse CSV from WebPlotDigitizer with ; separator and , decimals.
    Returns: wavelengths, intensities
    """
    raw_df = pd.read_csv(path, sep=";", header=None, engine="python")
    raw_df = raw_df.applymap(lambda x: str(x).strip().replace(",", "."))
    raw_df = raw_df.astype(float)

    wavelengths = raw_df.iloc[:, 0].values
    intensity = raw_df.iloc[:, 1].values
    return wavelengths, intensity

def convert_to_tsv(csv_path, description=""):
    try:
        # Parse and clean CSV
        wl, intensity = parse_webplot_csv(csv_path)

        # Define full desired range from 200 to 1100 nm
        full_range = np.arange(200, 1101, 1)

        # Interpolate original data onto full_range, with left and right fill as 0
        intensity_interp = np.interp(full_range, wl, intensity, left=0, right=0)

        # Normalize to relative (0–100) scale and round to 0.001
        max_val = np.max(intensity_interp)
        if max_val > 0:
            intensity_rel = np.round((intensity_interp / max_val) * 100, 3)
        else:
            intensity_rel = intensity_interp

        # Create output DataFrame
        df_out = pd.DataFrame({
            "Wavelength (nm)": full_range,
            "Relative Power": intensity_rel,
            "Description": [description] + [""] * (len(full_range) - 1)
        })

        # Save as .tsv
        out_name = Path(csv_path).stem + ".tsv"
        out_path = SCRIPT_DIR / out_name
        df_out.to_csv(out_path, sep="\t", index=False)

        messagebox.showinfo("Success", f"✅ Converted and saved:\n{out_path}")
    except Exception as e:
        messagebox.showerror("Error", f"⚠️ Failed to convert file:\n{e}")


def main():
    root = tk.Tk()
    root.withdraw()

    csv_path = filedialog.askopenfilename(
        title="Select WebPlotDigitizer CSV",
        filetypes=[("CSV files", "*.csv")]
    )
    if not csv_path:
        return

    description = simpledialog.askstring("Description", "Enter a short illuminant description:")
    if description is None:
        return

    convert_to_tsv(csv_path, description)

if __name__ == "__main__":
    main()
