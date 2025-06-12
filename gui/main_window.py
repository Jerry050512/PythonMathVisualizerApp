# -*- coding: utf-8 -*-
"""
主窗口模块 - 负责创建和管理主界面
"""

import tkinter as tk
from tkinter import ttk, messagebox
from config.settings import THEMES, DEFAULT_THEME, APP_TITLE
from core.font_manager import FontManager
from core.math_functions import MathFunctionCalculator
from gui.plot_area import PlotArea
from gui.font_settings import FontSettingsWindow
from gui.control_panel import ControlPanel
from utils.math_utils import MathUtils


class MathVisualizerApp:
    """数学函数可视化应用主窗口"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.current_theme = DEFAULT_THEME
        self.themes = THEMES
        
        # 初始化核心组件
        self.font_manager = FontManager()
        self.math_calculator = MathFunctionCalculator()
        
        self.setup_window()
        self.create_interface()
        
    def setup_window(self):
        """设置窗口"""
        theme = self.themes[self.current_theme]
        
        # 设置窗口属性
        self.root.title("📊 " + APP_TITLE)
        self.root.geometry("1400x900")
        self.root.minsize(1200, 800)
        self.root.configure(bg=theme['background'])
        
        # 居中显示窗口
        self._center_window()
    
    def _center_window(self):
        """将窗口居中显示"""
        self.root.update_idletasks()
        width = 1400
        height = 900
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_interface(self):
        """创建界面"""
        theme = self.themes[self.current_theme]
        
        # 主框架
        main_frame = tk.Frame(self.root, bg=theme['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 标题
        title_label = tk.Label(
            main_frame,
            text="📊 数学函数可视化工具",
            font=('Segoe UI', 16, 'bold'),
            fg=theme['primary'],
            bg=theme['background']
        )
        title_label.pack(pady=(0, 10))
        
        # 创建水平分割布局
        content_frame = tk.Frame(main_frame, bg=theme['background'])
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # 左侧控制面板（固定宽度350px）
        control_frame = tk.Frame(content_frame, bg=theme['surface'], width=350)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        control_frame.pack_propagate(False)  # 防止收缩
        
        # 右侧绘图区域（占用剩余空间）
        plot_frame = tk.Frame(content_frame, bg=theme['surface'])
        plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 创建绘图区域
        self.create_plot_content(plot_frame, theme)
        
        # 创建控制面板
        self.control_panel = ControlPanel(
            control_frame, 
            theme, 
            self.font_manager, 
            self.math_calculator, 
            self.plot_area,
            self.on_font_changed
        )
        
        # 设置默认函数
        self.control_panel.set_default_function()
    
    def create_plot_content(self, parent, theme):
        """创建绘图区域内容"""
        # 标题
        title = tk.Label(
            parent,
            text="📈 函数图形",
            font=('Segoe UI', 12, 'bold'),
            fg=theme['primary'],
            bg=theme['surface']
        )
        title.pack(pady=(10, 5))
        
        # 绘图区域
        plot_container = tk.Frame(parent, bg=theme['surface'])
        plot_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # 创建绘图区域
        self.plot_area = PlotArea(plot_container, self.font_manager)

    def on_font_changed(self):
        """字体更改后的回调"""
        try:
            # 重新绘制图形以应用新字体
            if self.math_calculator.functions:
                ranges = {'x_range': (-5, 5), 'y_range': (-5, 5)}
                options = {'show_extrema': True, 'show_roots': True, 'show_intersection': True, 'show_grid_points': False}
                self.plot_area.plot_functions(self.math_calculator.functions, ranges, options)
            else:
                # 如果没有函数，重新绘制默认函数以显示字体效果
                self.control_panel.plot_function()
        except Exception as e:
            print(f"字体更改回调错误: {e}")
    
    def run(self):
        """运行应用程序"""
        print("🚀 启动数学函数可视化工具...")
        print("✅ 启动成功！")
        self.root.mainloop()
