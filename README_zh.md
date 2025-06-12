# 📊 数学函数可视化工具 📈

[English README](../README.md) 🇬🇧🇺🇸

数学函数可视化工具是一款动态且用户友好的 Python 🐍 应用程序，让您能够可视化各种数学函数。您可以绘制函数、自定义其外观、分析其关键属性，甚至可以叠加多个函数进行比较！🥳

## ✨ 项目亮点 ✨

*   **动态函数绘图：** 轻松绘制二次函数、正弦函数、余弦函数、正切函数、指数函数和对数函数。📉📈
*   **多函数叠加：** 在同一图表上可视化多个函数，以便进行比较分析。🆚
*   **交互式分析：**
    *   自动识别并显示关键点：零点（根）🌳、极值点（顶点/峰谷）⛰️ 以及函数间的交点 🎯。
    *   在图表上为这些点提供清晰的注释。📝
*   **可自定义外观：**
    *   微调 X 轴和 Y 轴范围，以获得完美的视图。📏
    *   切换网格点以提高可读性。🏁
*   **高级字体管理：** 🖋️
    *   专用的字体设置窗口，提供实时预览。
    *   特别支持中文字体，确保在各种操作系统上正确显示。🌏
    *   即时将新字体应用于绘图！
*   **保存您的成果：** 轻松将绘图导出为图像文件 (PNG)。🖼️
*   **模块化与清晰的代码：** 结构组织良好，更易于理解和未来开发。🛠️

## 🚀 如何使用

### 配置开发环境

推荐使用 `venv` 创建一个虚拟环境运行. 
使用 `pip` 命令安装依赖. 
```
pip install -r requirements.txt
```

### 运行应用

1.  **运行应用程序：** 执行 `python main.py` 启动数学函数可视化工具。
2.  **选择函数类型：** 从下拉菜单中选择一个函数（例如，“二次函数”，“正弦函数”）。
3.  **输入参数：** 输入定义所选函数的系数（a, b, c）。
4.  **设置绘图范围：** 定义绘图的 X 轴和 Y 轴边界。
5.  **选择显示选项：**
    *   `显示极值点`：突出显示峰值和谷值。
    *   `显示零点`：标记函数与 x 轴的交点。
    *   `显示交点`：显示多个函数相交的点。
    *   `显示网格点`：向网格添加离散点。
6.  **绘制函数：** 点击“绘制函数”按钮绘制当前函数。这将清除先前的函数。
7.  **添加函数：** 点击“添加函数”按钮将当前函数叠加到现有绘图上。
8.  **清除绘图：** 点击“清除图形”按钮删除所有函数并重置绘图区域。
9.  **保存绘图：** 点击“保存图像”按钮保存您的杰作！
10. **字体设置：** 点击“字体设置”按钮自定义字体，特别适用于非英文字符。

## ⚙️ 工作原理

该应用程序利用 Python 的强大功能，结合 **Tkinter** 构建图形用户界面 (GUI)，并使用 **Matplotlib** 实现复杂的绘图功能。

*   **GUI 交互 (`gui` 模块)：** 用户通过 `ControlPanel` 进行交互，该面板提供用于选择函数类型、输入参数（a, b, c）、定义绘图范围（X, Y 最小值/最大值）和切换显示选项（如显示零点或极值点）的控件。这些交互会触发 `MathVisualizerApp` 内的特定操作。
*   **核心计算逻辑 (`core.math_functions`)：** `MathFunctionCalculator` 是数学运算背后的大脑。它接收函数类型和参数以：
    *   生成与一系列 x 值相对应的 y 值数组。
    *   生成函数公式的 LaTeX 样式字符串表示以供显示。
    *   计算重要特征，如零点（如果无法解析求解，则使用如二分法等数值方法）、极值点（通过分析导数或已知函数类型的特定公式）以及两个函数之间的交点（通过找到它们差值的零点）。
*   **绘图渲染 (`gui.plot_area`, `utils.plot_utils`)：** `PlotArea` 将 Matplotlib `FigureCanvasTkAgg` 嵌入到 Tkinter 窗口中。请求绘图时：
    *   `PlotUtils.setup_axes` 配置坐标轴、网格和标签。
    *   使用 `ax.plot()` 绘制计算出的函数点（x, y 数组）。
    *   如果启用了选项，则调用 `PlotUtils` 方法在图上标记和注释零点、极值点和交点。
    *   `FontManager` 确保所有文本元素（标题、标签、注释、图例）都使用当前选择的字体，并对中文字符进行特殊处理。
*   **字体管理 (`core.font_manager`)：** `FontManager` 类对于国际化和自定义至关重要。它：
    *   检测可用的系统字体，并为 Windows、macOS 和 Linux 提供预定义的常见中文字体列表。
    *   允许用户通过 `FontSettingsWindow` 选择字体。
    *   动态更新 Matplotlib 的 `rcParams` 以在应用程序的绘图中应用所选字体。这确保了数学符号和任何语言字符都能正确渲染。
*   **配置 (`config/settings.py`)：** 此文件集中管理静态配置，如默认窗口大小、主题颜色、UI 中可用的预定义函数类型以及不同操作系统的已知中文字体列表。这使得调整应用程序范围的设置更加容易。

## 📂 代码文件功能

*   **`main.py`**: 🏁 应用程序的主要入口点。初始化 Tkinter 根窗口并启动 `MathVisualizerApp`。

*   **`config/__init__.py`**: 将 `config` 目录标记为 Python 包。
*   **`config/settings.py`**: ⚙️ 存储应用程序的所有静态配置数据。包括：
    *   `APP_TITLE`, `APP_GEOMETRY`: 基本窗口属性。
    *   `TTK_THEME`, `ACCENT_BUTTON_STYLE`: Tkinter 小部件的样式。
    *   `FUNCTION_TYPES`: UI 支持的数学函数列表。
    *   `DEFAULT_X_RANGE`, `DEFAULT_Y_RANGE`: 初始绘图轴限制。
    *   `WINDOWS_CHINESE_FONTS`, `MACOS_CHINESE_FONTS`, `LINUX_CHINESE_FONTS`: 在不同操作系统上搜索的首选中文字体名称列表。这是良好 CJK 字符渲染的关键。
    *   `MATPLOTLIB_CONFIG`: 默认 Matplotlib 设置（例如，为坐标轴启用抗锯齿）。

*   **`core/__init__.py`**: 将 `core` 目录标记为 Python 包。
*   **`core/font_manager.py`**: 🖋️ 管理 Matplotlib 绘图的字体检测、选择和应用。
    *   `FontManager`: 检测系统字体，根据操作系统优先选择已知的中文字体，并提供获取/设置当前字体的方法。它直接与 Matplotlib 的 `rcParams` 交互，以全局应用于绘图的字体更改。这对于确保中文字符正确显示至关重要。
*   **`core/math_functions.py`**: 🧮 定义 `MathFunctionCalculator`，处理所有数学逻辑。
    *   `MathFunctionCalculator`:
        *   `get_function_values()`: 计算给定函数类型及其参数 (a,b,c) 在一系列 x 值上的 y 值。处理 `log` 或 `tan` 等函数的定义域问题。
        *   `get_function_expression()`: 生成用于显示函数公式的 LaTeX 格式字符串。
        *   `add_function()`, `clear_functions()`: 管理要绘制的函数列表。
        *   `calculate_quadratic_features()`, `calculate_trig_features()`: 用于查找特定特征（例如顶点、周期）的方法。
        *   `find_roots()`, `find_extrema()`, `find_intersections()`: 实现数值或解析方法来定位函数曲线上的这些重要点。

*   **`gui/__init__.py`**: 将 `gui` 目录标记为 Python 包。
*   **`gui/main_window.py`**: 🖼️ 定义 `MathVisualizerApp`，即主要的应用程序类，负责协调 GUI。
    *   `MathVisualizerApp`: 初始化主 Tkinter 窗口，设置样式，并创建 `ControlPanel` 和 `PlotArea` 的实例。它将控制面板的回调（例如，“绘图按钮点击”）连接到更新绘图区域或计算器的操作。
*   **`gui/control_panel.py`**: 🎛️ 定义 `ControlPanel`，用于用户输入和操作。
    *   `ControlPanel`: 创建所有 UI 元素（用于函数类型的下拉列表，用于参数 a,b,c 和绘图范围的输入字段，用于显示选项的复选框，操作按钮）。它收集用户输入并调用 `MathVisualizerApp` 中相应的回调函数。
*   **`gui/plot_area.py`**: 📊 定义 `PlotArea`，用于显示 Matplotlib 绘图。
    *   `PlotArea`: 将 Matplotlib `FigureCanvasTkAgg` 嵌入到 Tkinter 框架中。
        *   `plot_functions()`: 清除先前的绘图，设置坐标轴（通过 `PlotUtils`），遍历 `MathFunctionCalculator` 中的函数，绘制它们的曲线，并在选中时调用 `PlotUtils` 显示零点或极值点等特征。
        *   `clear_plot()`: 重置绘图。
        *   `save_plot()`: 将当前图形保存到文件。
*   **`gui/font_settings.py`**: ⚙️📄 定义 `FontSettingsWindow`，用于字体自定义。
    *   `FontSettingsWindow`: 一个对话框，列出可用的（尤其是中文）字体，显示预览，并允许用户应用新字体或重置为默认字体。更改通过 `FontManager` 传播。

*   **`utils/__init__.py`**: 将 `utils` 目录标记为 Python 包。
*   **`utils/math_utils.py`**: ➕➖ 包含用于数学计算和验证的静态辅助方法。
    *   `MathUtils`:
        *   `calculate_function_features()`: 将计算出的特征（如顶点、零点）格式化为人类可读的字符串以供显示。
        *   `validate_function_parameters()`: 检查无效输入（例如，二次函数的 `a=0`）。
        *   `get_optimal_range()`: (可能用于自动调整范围，但在 `ControlPanel` 当前逻辑中未明确使用)。
        *   `is_valid_range()`: 验证用户输入的绘图范围。
*   **`utils/plot_utils.py`**: 📈🎨 包含用于 Matplotlib 绘图任务的静态辅助方法。
    *   `PlotUtils`:
        *   `setup_axes()`: 配置绘图标题、标签、限制和网格。
        *   `plot_extrema_points()`, `plot_roots()`, `plot_intersections()`: 处理这些特定点在绘图上的视觉标记（例如，用 'ro' 表示红色圆圈）和注释，使用当前字体设置。
        *   `plot_grid_points()`: 如果启用，则在绘图上绘制离散点。
        *   `save_plot()`: 管理保存 Matplotlib 图形。

*   **`requirements.txt`**: 📜 列出必需的 Python 包（例如 `numpy`, `matplotlib`）。
*   **`.gitignore`**: 🚫 指定 Git 要忽略的文件和目录（例如 `__pycache__/`, `*.pyc`）。
*   **`__init__.py` (在根目录和其他包目录中)**: 标准 Python 文件，使目录可作为包导入。
