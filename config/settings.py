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

# 现代化主题配色方案
THEMES = {
    'modern_blue': {
        'name': '现代蓝',
        'primary': '#2563eb',           # 主色调 - 现代蓝
        'primary_dark': '#1d4ed8',      # 深蓝
        'primary_light': '#3b82f6',     # 浅蓝
        'secondary': '#64748b',         # 次要色 - 石板灰
        'accent': '#8b5cf6',            # 强调色 - 紫色
        'success': '#10b981',           # 成功色 - 绿色
        'warning': '#f59e0b',           # 警告色 - 橙色
        'danger': '#ef4444',            # 危险色 - 红色
        'background': '#f8fafc',        # 背景色
        'surface': '#ffffff',           # 表面色
        'surface_variant': '#f1f5f9',   # 表面变体
        'on_surface': '#1e293b',        # 表面文字
        'on_primary': '#ffffff',        # 主色文字
        'border': '#e2e8f0',            # 边框色
        'shadow': 'rgba(0, 0, 0, 0.1)', # 阴影色
    },
    'elegant_dark': {
        'name': '优雅暗色',
        'primary': '#6366f1',           # 主色调 - 靛蓝
        'primary_dark': '#4f46e5',      # 深靛蓝
        'primary_light': '#818cf8',     # 浅靛蓝
        'secondary': '#9ca3af',         # 次要色 - 灰色
        'accent': '#ec4899',            # 强调色 - 粉色
        'success': '#34d399',           # 成功色 - 绿色
        'warning': '#fbbf24',           # 警告色 - 黄色
        'danger': '#f87171',            # 危险色 - 红色
        'background': '#111827',        # 背景色 - 深灰
        'surface': '#1f2937',           # 表面色 - 灰色
        'surface_variant': '#374151',   # 表面变体
        'on_surface': '#f9fafb',        # 表面文字 - 白色
        'on_primary': '#ffffff',        # 主色文字
        'border': '#4b5563',            # 边框色
        'shadow': 'rgba(0, 0, 0, 0.3)', # 阴影色
    },
    'nature_green': {
        'name': '自然绿',
        'primary': '#059669',           # 主色调 - 翠绿
        'primary_dark': '#047857',      # 深绿
        'primary_light': '#10b981',     # 浅绿
        'secondary': '#6b7280',         # 次要色 - 灰色
        'accent': '#d97706',            # 强调色 - 橙色
        'success': '#22c55e',           # 成功色 - 绿色
        'warning': '#eab308',           # 警告色 - 黄色
        'danger': '#dc2626',            # 危险色 - 红色
        'background': '#f0fdf4',        # 背景色 - 浅绿
        'surface': '#ffffff',           # 表面色
        'surface_variant': '#ecfdf5',   # 表面变体
        'on_surface': '#14532d',        # 表面文字 - 深绿
        'on_primary': '#ffffff',        # 主色文字
        'border': '#bbf7d0',            # 边框色
        'shadow': 'rgba(0, 0, 0, 0.08)', # 阴影色
    }
}

# 默认主题
DEFAULT_THEME = 'modern_blue'

# 按钮样式配置
BUTTON_STYLES = {
    'primary': {
        'relief': 'flat',
        'borderwidth': 0,
        'font': ('', 10, 'bold'),
        'cursor': 'hand2',
        'padx': 20,
        'pady': 8
    },
    'secondary': {
        'relief': 'flat',
        'borderwidth': 1,
        'font': ('', 10),
        'cursor': 'hand2',
        'padx': 16,
        'pady': 6
    },
    'icon': {
        'relief': 'flat',
        'borderwidth': 0,
        'font': ('', 12),
        'cursor': 'hand2',
        'padx': 8,
        'pady': 8
    }
}

# 卡片样式
CARD_STYLE = {
    'relief': 'flat',
    'borderwidth': 1,
    'padx': 20,
    'pady': 15
}

# 动画配置
ANIMATION_CONFIG = {
    'duration': 200,  # 毫秒
    'steps': 10,
    'easing': 'ease_out'
}

# 文件保存设置
DEFAULT_SAVE_FILENAME = "math_functions_plot.png"
SAVE_DPI = 150
