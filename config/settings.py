# -*- coding: utf-8 -*-
"""
应用程序配置设置
"""

# 应用程序基本设置
APP_TITLE = "数学公式可视化工具"
APP_GEOMETRY = "1200x800"
APP_BACKGROUND = "#f0f0f0"

# 绘图设置
DEFAULT_X_RANGE = (-5, 5)
DEFAULT_Y_RANGE = (-5, 5)
PLOT_POINTS = 1000
FIGURE_SIZE = (10, 8)
FIGURE_DPI = 100
FIGURE_FACECOLOR = "#f8f8f8"
AXES_FACECOLOR = "#f5f5f5"

# 函数类型定义
FUNCTION_TYPES = [
    "二次函数", 
    "正弦函数", 
    "余弦函数", 
    "正切函数", 
    "指数函数", 
    "对数函数"
]

# 颜色设置
FUNCTION_COLORS = ['b', 'r', 'g', 'm', 'c', 'y', 'k']

# 字体设置
WINDOWS_CHINESE_FONTS = [
    'Microsoft YaHei',      # 微软雅黑
    'Microsoft YaHei UI',   # 微软雅黑 UI
    'SimHei',               # 黑体
    'SimSun',               # 宋体
    'KaiTi',                # 楷体
    'FangSong',             # 仿宋
    'Microsoft JhengHei',   # 微软正黑体
    'DengXian',             # 等线
    'YouYuan',              # 幼圆
]

MACOS_CHINESE_FONTS = [
    'PingFang SC',          # 苹方 简体
    'PingFang TC',          # 苹方 繁体
    'Hiragino Sans GB',     # 冬青黑体简体中文
    'STHeiti',              # 华文黑体
    'STSong',               # 华文宋体
    'STKaiti',              # 华文楷体
    'STFangsong',           # 华文仿宋
    'Arial Unicode MS',     # Arial Unicode MS
    'Apple LiGothic',       # 苹果丽黑
    'Heiti SC',             # 黑体-简
    'Songti SC',            # 宋体-简
]

LINUX_CHINESE_FONTS = [
    'WenQuanYi Micro Hei',  # 文泉驿微米黑
    'WenQuanYi Zen Hei',    # 文泉驿正黑
    'WenQuanYi Bitmap Song', # 文泉驿点阵宋体
    'Noto Sans CJK SC',     # 思源黑体 简体
    'Noto Serif CJK SC',    # 思源宋体 简体
    'Source Han Sans CN',   # 思源黑体
    'Source Han Serif CN',  # 思源宋体
    'AR PL UMing CN',       # 文鼎PL简中明
    'AR PL UKai CN',        # 文鼎PL简中楷
]

CHINESE_FONT_KEYWORDS = [
    'Chinese', 'CJK', 'Han', 'Hei', 'Song', 'Kai', 'Ming',
    'YaHei', 'SimHei', 'SimSun', 'PingFang', 'Hiragino',
    'WenQuanYi', 'Noto', 'Source', 'Droid'
]

FALLBACK_FONTS = ['Arial Unicode MS', 'Liberation Sans']

# matplotlib设置
MATPLOTLIB_CONFIG = {
    'text.usetex': False,
    'mathtext.fontset': 'stix',
    'mathtext.default': 'regular',
    'axes.unicode_minus': False
}

# GUI样式设置
TTK_THEME = "clam"
ACCENT_BUTTON_STYLE = {
    'background': "#4a90d9",
    'foreground': "white",
    'font': ("Arial", 10, "bold")
}

# 文件保存设置
DEFAULT_SAVE_FILENAME = "math_functions_plot.png"
SAVE_DPI = 150
