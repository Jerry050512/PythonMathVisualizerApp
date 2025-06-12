# 📊 Math Visualizer 📈

[中文版 README](README_zh.md) 🇨🇳

Check out the AI wiki page [here](https://deepwiki.com/Jerry050512/PythonMathVisualizerApp). 

Math Visualizer is a dynamic and user-friendly Python application 🐍 that allows you to visualize various mathematical functions. You can plot functions, customize their appearance, analyze their key properties, and even overlay multiple functions for comparison! 🥳

## ✨ Project Highlights ✨

*   **Dynamic Function Plotting:** Easily plot Quadratic, Sine, Cosine, Tangent, Exponential, and Logarithmic functions. 📉📈
*   **Multi-Function Overlay:** Visualize multiple functions on the same graph for comparative analysis. 🆚
*   **Interactive Analysis:**
    *   Automatically identify and display key points: Zeros (roots) 🌳, Extrema (vertices/peaks/valleys) ⛰️, and Intersection points 🎯 between functions.
    *   Clear annotations for these points directly on the plot. 📝
*   **Customizable Appearance:**
    *   Fine-tune X and Y axis ranges for the perfect view. 📏
    *   Toggle grid points for better readability. 🏁
*   **Advanced Font Management:** 🖋️
    *   Dedicated font settings window with live preview.
    *   Specialized support for Chinese fonts, ensuring correct display on various operating systems. 🌏
    *   Apply new fonts instantly to plots!
*   **Save Your Work:** Export plots as image files (PNG) with ease. 🖼️
*   **Modular & Clean Code:** Well-organized structure for better understanding and future development. 🛠️

## 🚀 How to Use

### Setup Environment

Use `venv` to create a virtual environment. (Recommend)
Use `pip` to install the requirements. 
```
pip install -r requirements.txt
```

### Run the App

1.  **Run the application:** Execute `python main.py` to start the Math Visualizer.
2.  **Select function type:** Choose a function from the dropdown menu (e.g., "二次函数" for Quadratic, "正弦函数" for Sine).
3.  **Enter parameters:** Input the coefficients (a, b, c) that define your chosen function.
4.  **Set plot ranges:** Define the X and Y axis boundaries for your plot.
5.  **Choose display options:**
    *   `显示极值点` (Show Extrema): Highlights peaks and valleys.
    *   `显示零点` (Show Roots): Marks where the function crosses the x-axis.
    *   `显示交点` (Show Intersections): Shows points where multiple functions meet.
    *   `显示网格点` (Show Grid Points): Adds discrete points to the grid.
6.  **Plot Function:** Click "绘制函数" (Plot Function) to draw the current function. This clears previous functions.
7.  **Add Function:** Click "添加函数" (Add Function) to overlay the current function onto the existing plot.
8.  **Clear Plot:** Click "清除图形" (Clear Plot) to remove all functions and reset the plot area.
9.  **Save Plot:** Click "保存图像" (Save Plot) to save your masterpiece!
10. **Font Settings:** Click "字体设置" (Font Settings) to customize fonts, especially for non-English characters.

### Windows Display Scaling

To ensure text and UI elements appear sharp on high-DPI displays on Windows, this application attempts to set itself as DPI-aware. This is done by calling Windows API functions using the `ctypes` library at startup. If you encounter any issues with display scaling, this is the mechanism responsible for it. On other operating systems like macOS and Linux, DPI scaling is generally handled more automatically by the system or toolkit.

## ⚙️ How It Works

The application leverages the power of Python with **Tkinter** for its graphical user interface (GUI) and **Matplotlib** for sophisticated plotting capabilities.

*   **GUI Interaction (`gui` module):** The user interacts with the `ControlPanel`, which provides widgets for selecting function types, inputting parameters (a, b, c), defining plot ranges (X, Y min/max), and toggling display options (like showing roots or extrema). These interactions trigger specific actions within the `MathVisualizerApp`.
*   **Core Calculation Logic (`core.math_functions`):** The `MathFunctionCalculator` is the brain behind the mathematical operations. It takes the function type and parameters to:
    *   Generate an array of y-values corresponding to a range of x-values.
    *   Produce a LaTeX-style string representation of the function's formula for display.
    *   Calculate important features like roots (using numerical methods like bisection if not analytically solvable), extrema (by analyzing derivatives or specific formulas for known function types), and intersection points between two functions (by finding roots of their difference).
*   **Plot Rendering (`gui.plot_area`, `utils.plot_utils`):** The `PlotArea` embeds a Matplotlib `FigureCanvasTkAgg` into the Tkinter window. When a plot is requested:
    *   `PlotUtils.setup_axes` configures the axes, grid, and labels.
    *   The calculated function points (x, y arrays) are plotted using `ax.plot()`.
    *   If options are enabled, `PlotUtils` methods are called to mark and annotate roots, extrema, and intersections on the plot.
    *   The `FontManager` ensures that all text elements (titles, labels, annotations, legend) use the currently selected font, with special handling for Chinese characters.
*   **Font Management (`core.font_manager`):** The `FontManager` class is crucial for internationalization and customization. It:
    *   Detects available system fonts, with a predefined list of common Chinese fonts for Windows, macOS, and Linux.
    *   Allows the user to select a font via the `FontSettingsWindow`.
    *   Updates Matplotlib's `rcParams` dynamically to apply the chosen font across the application's plots. This ensures that mathematical symbols and any language characters render correctly.
*   **Configuration (`config/settings.py`):** This file centralizes static configurations like default window size, theme colors, predefined function types available in the UI, and lists of known Chinese fonts for different operating systems. This makes it easier to tweak application-wide settings.

## 📂 Code File Functions

*   **`main.py`**: 🏁 The main entry point of the application. It creates an instance of `MathVisualizerApp` from the `gui.main_window` module and calls its `run()` method to start the application.

*   **`config/__init__.py`**: Marks the `config` directory as a Python package.
*   **`config/settings.py`**: ⚙️ Stores all static configuration data for the application. This includes:
    *   `APP_TITLE`, `APP_GEOMETRY`: Basic window properties.
    *   `TTK_THEME`, `ACCENT_BUTTON_STYLE`: Styling for Tkinter widgets.
    *   `FUNCTION_TYPES`: List of math functions supported by the UI.
    *   `DEFAULT_X_RANGE`, `DEFAULT_Y_RANGE`: Initial plot axis limits.
    *   `WINDOWS_CHINESE_FONTS`, `MACOS_CHINESE_FONTS`, `LINUX_CHINESE_FONTS`: Lists of preferred Chinese font names to search for on different OSes. This is key for good CJK character rendering.
    *   `MATPLOTLIB_CONFIG`: Default Matplotlib settings (e.g., enabling anti-aliasing for axes).

*   **`core/__init__.py`**: Marks the `core` directory as a Python package.
*   **`core/font_manager.py`**: 🖋️ Manages font detection, selection, and application for Matplotlib plots.
    *   `FontManager`: Detects system fonts, prioritizes known Chinese fonts based on OS, and provides methods to get/set the current font. It directly interacts with Matplotlib's `rcParams` to apply font changes globally to plots. This is critical for ensuring Chinese characters display correctly.
*   **`core/math_functions.py`**: 🧮 Defines `MathFunctionCalculator` for all mathematical logic.
    *   `MathFunctionCalculator`:
        *   `get_function_values()`: Computes y-values for a given function type and its parameters (a,b,c) over a range of x-values. Handles domain issues for functions like `log` or `tan`.
        *   `get_function_expression()`: Generates a LaTeX-formatted string for displaying the function formula.
        *   `add_function()`, `clear_functions()`: Manages the list of functions to be plotted.
        *   `calculate_quadratic_features()`, `calculate_trig_features()`: Methods to find specific features (e.g., vertex, period).
        *   `find_roots()`, `find_extrema()`, `find_intersections()`: Implements numerical or analytical methods to locate these important points on the function curves.

*   **`gui/__init__.py`**: Marks the `gui` directory as a Python package.
*   **`gui/main_window.py`**: 🖼️ Defines `MathVisualizerApp`, the main application class that encapsulates the entire GUI.
    *   `MathVisualizerApp`: Initializes its own Tkinter root window (`tk.Tk()`), sets up styles, and creates instances of `ControlPanel` and `PlotArea`. It manages the application's main event loop through its `run()` method. It also connects callbacks from the control panel to actions that update the plot area or calculator.
*   **`gui/control_panel.py`**: 🎛️ Defines `ControlPanel` for user inputs and actions.
    *   `ControlPanel`: Creates all UI elements (dropdowns for function type, entry fields for parameters a,b,c and plot ranges, checkboxes for display options, action buttons). It gathers user input and calls the appropriate callback functions in `MathVisualizerApp`.
*   **`gui/plot_area.py`**: 📊 Defines `PlotArea` for displaying Matplotlib plots.
    *   `PlotArea`: Embeds a Matplotlib `FigureCanvasTkAgg` in the Tkinter frame.
        *   `plot_functions()`: Clears the previous plot, sets up axes (via `PlotUtils`), iterates through functions from `MathFunctionCalculator`, plots their curves, and calls `PlotUtils` to display features like roots or extrema if selected.
        *   `clear_plot()`: Resets the plot.
        *   `save_plot()`: Saves the current figure to a file.
*   **`gui/font_settings.py`**: ⚙️📄 Defines `FontSettingsWindow` for font customization.
    *   `FontSettingsWindow`: A dialog that lists available (especially Chinese) fonts, shows a preview, and allows the user to apply a new font or reset to default. Changes are propagated via the `FontManager`.

*   **`utils/__init__.py`**: Marks the `utils` directory as a Python package.
*   **`utils/math_utils.py`**: ➕➖ Contains static helper methods for mathematical computations and validations.
    *   `MathUtils`:
        *   `calculate_function_features()`: Formats calculated features (like vertex, roots) into human-readable strings for display.
        *   `validate_function_parameters()`: Checks for invalid inputs (e.g., `a=0` for a quadratic function).
        *   `get_optimal_range()`: (Potentially used for auto-ranging, though not explicitly seen in `ControlPanel`'s current logic).
        *   `is_valid_range()`: Validates user-inputted plot ranges.
*   **`utils/plot_utils.py`**: 📈🎨 Contains static helper methods for Matplotlib plotting tasks.
    *   `PlotUtils`:
        *   `setup_axes()`: Configures plot titles, labels, limits, and grid.
        *   `plot_extrema_points()`, `plot_roots()`, `plot_intersections()`: Handles the visual marking (e.g., with 'ro' for red circles) and annotation of these specific points on the plot, using the current font settings.
        *   `plot_grid_points()`: Draws discrete points on the plot if enabled.
        *   `save_plot()`: Manages saving the Matplotlib figure.

*   **`requirements.txt`**: 📜 Lists necessary Python packages (e.g., `numpy`, `matplotlib`).
*   **`.gitignore`**: 🚫 Specifies files and directories for Git to ignore (e.g., `__pycache__/`, `*.pyc`).
*   **`__init__.py` (in root and other package directories)**: Standard Python files to make directories importable as packages.
