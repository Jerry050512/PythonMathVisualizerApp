# -*- coding: utf-8 -*-
"""
控制面板模块
"""

import tkinter as tk
from tkinter import ttk
from typing import Tuple, Dict, Any, Callable
from config.settings import FUNCTION_TYPES, DEFAULT_X_RANGE, DEFAULT_Y_RANGE
from utils.math_utils import MathUtils
# 暂时注释掉现代化组件，避免启动错误
# from .theme_manager import theme_manager
# from .modern_widgets import ModernButton, ModernCard, ModernEntry


class ControlPanel:
    """控制面板类"""
    
    def __init__(self, parent, math_calculator, font_manager, 
                 plot_callback: Callable, add_callback: Callable, 
                 clear_callback: Callable, save_callback: Callable,
                 font_settings_callback: Callable):
        """
        初始化控制面板
        
        Args:
            parent: 父容器
            math_calculator: 数学计算器实例
            font_manager: 字体管理器实例
            plot_callback: 绘制函数回调
            add_callback: 添加函数回调
            clear_callback: 清除图形回调
            save_callback: 保存图形回调
            font_settings_callback: 字体设置回调
        """
        self.parent = parent
        self.math_calculator = math_calculator
        self.font_manager = font_manager
        self.plot_callback = plot_callback
        self.add_callback = add_callback
        self.clear_callback = clear_callback
        self.save_callback = save_callback
        self.font_settings_callback = font_settings_callback
        
        self.plot_area = None  # 将在后面设置
        
        # 创建控制面板
        self.create_control_panel()
    
    def set_plot_area(self, plot_area):
        """设置绘图区域引用"""
        self.plot_area = plot_area
    
    def create_control_panel(self):
        """创建控制面板"""
        # 创建控制面板主框架
<<<<<<< HEAD
        self.control_frame = ttk.LabelFrame(self.parent, text="🎛️ 函数控制面板", padding=(15, 10))
        self.control_frame.pack(fill=tk.X, pady=(0, 15))

=======
        self.control_frame = ttk.LabelFrame(self.parent, text="函数控制面板", padding=(15, 10))
        self.control_frame.pack(fill=tk.X, pady=(0, 15))
        
>>>>>>> 9f560dc (init repo)
        # 创建各个区域
        self.create_function_type_area()
        self.create_parameter_area()
        self.create_range_area()
        self.create_options_area()
        self.create_button_area()
        self.create_info_area()
    
    def create_function_type_area(self):
        """创建函数类型选择区域"""
        ttk.Label(self.control_frame, text="选择函数类型:", font=('', 10)).grid(
            row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        self.function_type = tk.StringVar()
        self.function_menu = ttk.Combobox(
            self.control_frame, 
            textvariable=self.function_type, 
            values=FUNCTION_TYPES, 
            state="readonly", 
            width=15, 
            font=('', 9)
        )
        self.function_menu.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.function_menu.bind("<<ComboboxSelected>>", self.update_function_options)
    
    def create_parameter_area(self):
        """创建参数输入区域"""
        self.param_frame = ttk.Frame(self.control_frame)
        self.param_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky=tk.W)
    
    def create_range_area(self):
        """创建绘图范围设置区域"""
        range_frame = ttk.Frame(self.control_frame)
        range_frame.grid(row=2, column=0, columnspan=4, pady=5, sticky=tk.W)
        
        # X轴范围设置
        ttk.Label(range_frame, text="X范围:", font=('', 9)).grid(row=0, column=0, padx=5, sticky=tk.W)
        self.x_min = tk.DoubleVar(value=DEFAULT_X_RANGE[0])
        self.x_max = tk.DoubleVar(value=DEFAULT_X_RANGE[1])
        ttk.Entry(range_frame, textvariable=self.x_min, width=5, font=('', 9)).grid(row=0, column=1, padx=5)
        ttk.Entry(range_frame, textvariable=self.x_max, width=5, font=('', 9)).grid(row=0, column=2, padx=5)
        
        # Y轴范围设置
        ttk.Label(range_frame, text="Y范围:", font=('', 9)).grid(row=0, column=3, padx=(15, 5), sticky=tk.W)
        self.y_min = tk.DoubleVar(value=DEFAULT_Y_RANGE[0])
        self.y_max = tk.DoubleVar(value=DEFAULT_Y_RANGE[1])
        ttk.Entry(range_frame, textvariable=self.y_min, width=5, font=('', 9)).grid(row=0, column=4, padx=5)
        ttk.Entry(range_frame, textvariable=self.y_max, width=5, font=('', 9)).grid(row=0, column=5, padx=5)
    
    def create_options_area(self):
        """创建显示选项区域"""
        options_frame = ttk.Frame(self.control_frame)
        options_frame.grid(row=3, column=0, columnspan=4, pady=10, sticky=tk.W)
        
        self.show_extrema = tk.BooleanVar(value=True)
        self.show_roots = tk.BooleanVar(value=True)
        self.show_intersection = tk.BooleanVar(value=True)
        self.show_grid_points = tk.BooleanVar(value=False)
        
        ttk.Checkbutton(options_frame, text="显示极值点", variable=self.show_extrema).grid(row=0, column=0, padx=5)
        ttk.Checkbutton(options_frame, text="显示零点", variable=self.show_roots).grid(row=0, column=1, padx=5)
        ttk.Checkbutton(options_frame, text="显示交点", variable=self.show_intersection).grid(row=0, column=2, padx=5)
        ttk.Checkbutton(options_frame, text="显示网格点", variable=self.show_grid_points).grid(row=0, column=3, padx=5)
    
    def create_button_area(self):
        """创建操作按钮区域"""
        button_frame = ttk.Frame(self.control_frame)
        button_frame.grid(row=4, column=0, columnspan=4, pady=10)
<<<<<<< HEAD

        # 使用美化的按钮文本（带图标）
        ttk.Button(button_frame, text="📊 绘制函数", command=self.plot_callback).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="➕ 添加函数", command=self.add_callback).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="🗑️ 清除图形", command=self.clear_callback).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="💾 保存图像", command=self.save_callback).grid(row=0, column=3, padx=5)
        ttk.Button(button_frame, text="🔤 字体设置", command=self.font_settings_callback).grid(row=0, column=4, padx=5)

=======
        
        ttk.Button(button_frame, text="绘制函数", command=self.plot_callback, 
                  style="Accent.TButton").grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="添加函数", command=self.add_callback).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="清除图形", command=self.clear_callback).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="保存图像", command=self.save_callback).grid(row=0, column=3, padx=5)
        ttk.Button(button_frame, text="字体设置", command=self.font_settings_callback).grid(row=0, column=4, padx=5)
        
>>>>>>> 9f560dc (init repo)
        # 分隔线
        ttk.Separator(self.control_frame, orient=tk.HORIZONTAL).grid(
            row=5, column=0, columnspan=4, pady=15, sticky=tk.EW)
    
    def create_info_area(self):
        """创建函数信息显示区域"""
        info_frame = ttk.Frame(self.control_frame)
        info_frame.grid(row=6, column=0, columnspan=4, pady=5, sticky=tk.W)
        
        ttk.Label(info_frame, text="函数表达式:", font=('', 10)).grid(row=0, column=0, padx=5, sticky=tk.W)
        self.function_label = ttk.Label(info_frame, text="", font=("Arial", 10, "bold"), foreground="#3366cc")
        self.function_label.grid(row=0, column=1, padx=5, sticky=tk.W)
        
        ttk.Label(info_frame, text="关键点:", font=('', 10)).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.key_points = ttk.Label(info_frame, text="", font=('', 9), foreground="#333333")
        self.key_points.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    def update_function_options(self, event=None):
        """根据选择的函数类型更新参数输入界面"""
        # 清除现有的参数输入组件
        for widget in self.param_frame.winfo_children():
            widget.destroy()

        func_type = self.function_type.get()

        if func_type == "二次函数":
            ttk.Label(self.param_frame, text="y = a·x² + b·x + c", font=('', 10)).grid(
                row=0, column=0, columnspan=3, pady=5)

            ttk.Label(self.param_frame, text="a:", font=('', 9)).grid(row=1, column=0, padx=5, pady=5)
            self.a = tk.DoubleVar(value=1.0)
            ttk.Entry(self.param_frame, textvariable=self.a, width=5, font=('', 9)).grid(row=1, column=1, padx=5)

            ttk.Label(self.param_frame, text="b:", font=('', 9)).grid(row=1, column=2, padx=5, pady=5)
            self.b = tk.DoubleVar(value=0.0)
            ttk.Entry(self.param_frame, textvariable=self.b, width=5, font=('', 9)).grid(row=1, column=3, padx=5)

            ttk.Label(self.param_frame, text="c:", font=('', 9)).grid(row=1, column=4, padx=5, pady=5)
            self.c = tk.DoubleVar(value=0.0)
            ttk.Entry(self.param_frame, textvariable=self.c, width=5, font=('', 9)).grid(row=1, column=5, padx=5)

        elif func_type in ["正弦函数", "余弦函数", "正切函数"]:
            func_symbol = "sin" if func_type == "正弦函数" else "cos" if func_type == "余弦函数" else "tan"
            ttk.Label(self.param_frame, text=f"y = a·{func_symbol}(b·x + c)", font=('', 10)).grid(
                row=0, column=0, columnspan=3, pady=5)

            ttk.Label(self.param_frame, text="a:", font=('', 9)).grid(row=1, column=0, padx=5, pady=5)
            self.a = tk.DoubleVar(value=1.0)
            ttk.Entry(self.param_frame, textvariable=self.a, width=5, font=('', 9)).grid(row=1, column=1, padx=5)

            ttk.Label(self.param_frame, text="b:", font=('', 9)).grid(row=1, column=2, padx=5, pady=5)
            self.b = tk.DoubleVar(value=1.0)
            ttk.Entry(self.param_frame, textvariable=self.b, width=5, font=('', 9)).grid(row=1, column=3, padx=5)

            ttk.Label(self.param_frame, text="c:", font=('', 9)).grid(row=1, column=4, padx=5, pady=5)
            self.c = tk.DoubleVar(value=0.0)
            ttk.Entry(self.param_frame, textvariable=self.c, width=5, font=('', 9)).grid(row=1, column=5, padx=5)

        elif func_type == "指数函数":
            ttk.Label(self.param_frame, text="y = a·e^(b·x) + c", font=('', 10)).grid(
                row=0, column=0, columnspan=3, pady=5)

            ttk.Label(self.param_frame, text="a:", font=('', 9)).grid(row=1, column=0, padx=5, pady=5)
            self.a = tk.DoubleVar(value=1.0)
            ttk.Entry(self.param_frame, textvariable=self.a, width=5, font=('', 9)).grid(row=1, column=1, padx=5)

            ttk.Label(self.param_frame, text="b:", font=('', 9)).grid(row=1, column=2, padx=5, pady=5)
            self.b = tk.DoubleVar(value=1.0)
            ttk.Entry(self.param_frame, textvariable=self.b, width=5, font=('', 9)).grid(row=1, column=3, padx=5)

            ttk.Label(self.param_frame, text="c:", font=('', 9)).grid(row=1, column=4, padx=5, pady=5)
            self.c = tk.DoubleVar(value=0.0)
            ttk.Entry(self.param_frame, textvariable=self.c, width=5, font=('', 9)).grid(row=1, column=5, padx=5)

        elif func_type == "对数函数":
            ttk.Label(self.param_frame, text="y = a·log(b·x + c)", font=('', 10)).grid(
                row=0, column=0, columnspan=3, pady=5)

            ttk.Label(self.param_frame, text="a:", font=('', 9)).grid(row=1, column=0, padx=5, pady=5)
            self.a = tk.DoubleVar(value=1.0)
            ttk.Entry(self.param_frame, textvariable=self.a, width=5, font=('', 9)).grid(row=1, column=1, padx=5)

            ttk.Label(self.param_frame, text="b:", font=('', 9)).grid(row=1, column=2, padx=5, pady=5)
            self.b = tk.DoubleVar(value=1.0)
            ttk.Entry(self.param_frame, textvariable=self.b, width=5, font=('', 9)).grid(row=1, column=3, padx=5)

            ttk.Label(self.param_frame, text="c:", font=('', 9)).grid(row=1, column=4, padx=5, pady=5)
            self.c = tk.DoubleVar(value=0.0)
            ttk.Entry(self.param_frame, textvariable=self.c, width=5, font=('', 9)).grid(row=1, column=5, padx=5)

    def get_current_function(self) -> Tuple[str, Tuple[float, float, float]]:
        """
        获取当前函数类型和参数

        Returns:
            (函数类型, (a, b, c))
        """
        func_type = self.function_type.get()
        a = self.a.get()
        b = self.b.get()
        c = self.c.get()

        # 验证参数有效性
        is_valid, error_msg = MathUtils.validate_function_parameters(func_type, a, b, c)
        if not is_valid:
            raise ValueError(error_msg)

        return func_type, (a, b, c)

    def get_plot_ranges(self) -> Dict[str, Tuple[float, float]]:
        """
        获取绘图范围

        Returns:
            包含x和y范围的字典
        """
        x_min = self.x_min.get()
        x_max = self.x_max.get()
        y_min = self.y_min.get()
        y_max = self.y_max.get()

        # 验证范围有效性
        is_valid, error_msg = MathUtils.is_valid_range(x_min, x_max, y_min, y_max)
        if not is_valid:
            raise ValueError(error_msg)

        return {
            'x_range': (x_min, x_max),
            'y_range': (y_min, y_max)
        }

    def get_display_options(self) -> Dict[str, bool]:
        """
        获取显示选项

        Returns:
            显示选项字典
        """
        return {
            'show_extrema': self.show_extrema.get(),
            'show_roots': self.show_roots.get(),
            'show_intersection': self.show_intersection.get(),
            'show_grid_points': self.show_grid_points.get()
        }

    def set_default_function(self):
        """设置默认函数并绘制"""
        self.function_type.set("二次函数")
        self.update_function_options()
        self.plot_callback()

    def update_function_info(self, expression: str, func_type: str, params: Tuple[float, float, float]):
        """
        更新函数信息显示

        Args:
            expression: 函数表达式
            func_type: 函数类型
            params: 函数参数
        """
        self.function_label.config(text=expression)

        # 计算并显示关键点信息
        key_points = MathUtils.calculate_function_features(func_type, *params)

        if self.math_calculator.get_function_count() >= 2:
            key_points.append(f"共有 {self.math_calculator.get_function_count()} 个函数")

        self.key_points.config(text="\n".join(key_points))

    def clear_function_info(self):
        """清除函数信息显示"""
        self.function_label.config(text="")
        self.key_points.config(text="")
