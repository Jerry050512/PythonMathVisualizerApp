# -*- coding: utf-8 -*-
"""
控制面板模块 - 负责创建和管理控制面板界面
"""

import tkinter as tk
from tkinter import ttk, messagebox
from gui.font_settings import FontSettingsWindow
from utils.math_utils import MathUtils


class ControlPanel:
    """控制面板类"""
    
    def __init__(self, parent, theme, font_manager, math_calculator, plot_area, font_changed_callback):
        self.parent = parent
        self.theme = theme
        self.font_manager = font_manager
        self.math_calculator = math_calculator
        self.plot_area = plot_area
        self.font_changed_callback = font_changed_callback
        
        self.create_control_content()
        
    def create_control_content(self):
        """创建控制面板内容"""
        # 标题
        title = tk.Label(
            self.parent,
            text="🎛️ 控制面板",
            font=('Segoe UI', 12, 'bold'),
            fg=self.theme['primary'],
            bg=self.theme['surface']
        )
        title.pack(pady=10)
        
        # 函数类型选择
        self.create_function_selector()
        
        # 参数输入区域
        self.param_frame = tk.Frame(self.parent, bg=self.theme['surface'])
        self.param_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # 操作按钮
        self.create_buttons()
        
        # 字体信息显示
        self.create_font_info()

        # 初始化参数
        self.update_parameters()
    
    def create_function_selector(self):
        """创建函数类型选择器"""
        type_frame = tk.Frame(self.parent, bg=self.theme['surface'])
        type_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            type_frame,
            text="函数类型:",
            font=('Segoe UI', 10),
            fg=self.theme['on_surface'],
            bg=self.theme['surface']
        ).pack(anchor=tk.W)
        
        self.function_type = tk.StringVar(value="二次函数")
        function_menu = ttk.Combobox(
            type_frame,
            textvariable=self.function_type,
            values=["二次函数", "正弦函数", "余弦函数", "正切函数", "指数函数", "对数函数"],
            state="readonly",
            width=25
        )
        function_menu.pack(fill=tk.X, pady=5)
        function_menu.bind("<<ComboboxSelected>>", self.update_parameters)
    
    def create_buttons(self):
        """创建操作按钮"""
        button_frame = tk.Frame(self.parent, bg=self.theme['surface'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        buttons = [
            ("📊 绘制函数", self.plot_function, self.theme['primary']),
            ("➕ 添加函数", self.add_function, self.theme['secondary']),
            ("🗑️ 清除图形", self.clear_plot, self.theme['danger']),
            ("💾 保存图像", self.save_plot, self.theme['success']),
            ("🔤 字体设置", self.show_font_settings, self.theme['accent'])
        ]

        for i, (text, command, color) in enumerate(buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                bg=color,
                fg='white',
                font=('Segoe UI', 9, 'bold'),
                relief='flat',
                padx=5,
                pady=3,
                cursor='hand2'
            )
            btn.pack(fill=tk.X, pady=2)
    
    def create_font_info(self):
        """创建字体信息显示区域"""
        font_frame = tk.Frame(self.parent, bg=self.theme['surface'])
        font_frame.pack(fill=tk.X, padx=10, pady=5)

        # 字体信息标题
        tk.Label(
            font_frame,
            text="📝 当前字体:",
            font=('Segoe UI', 9, 'bold'),
            fg=self.theme['on_surface'],
            bg=self.theme['surface']
        ).pack(anchor=tk.W)

        # 当前字体显示
        current_font = self.font_manager.get_current_font()
        self.font_info_label = tk.Label(
            font_frame,
            text=current_font,
            font=('Segoe UI', 8),
            fg=self.theme['secondary'],
            bg=self.theme['surface']
        )
        self.font_info_label.pack(anchor=tk.W, padx=(10, 0))

        # 字体预览
        self.font_preview_label = tk.Label(
            font_frame,
            text="中文测试: 数学函数",
            font=(current_font, 9),
            fg=self.theme['primary'],
            bg=self.theme['surface']
        )
        self.font_preview_label.pack(anchor=tk.W, padx=(10, 0), pady=(2, 0))

    def update_font_info(self):
        """更新字体信息显示"""
        try:
            current_font = self.font_manager.get_current_font()
            self.font_info_label.config(text=current_font)
            self.font_preview_label.config(font=(current_font, 9))
        except Exception as e:
            print(f"更新字体信息失败: {e}")

    def update_parameters(self, event=None):
        """更新参数输入"""
        # 清除现有参数
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        
        func_type = self.function_type.get()
        
        # 显示函数公式
        formula_text = self.get_formula_text(func_type)
        formula_label = tk.Label(
            self.param_frame,
            text=formula_text,
            font=('Segoe UI', 10, 'bold'),
            fg=self.theme['primary'],
            bg=self.theme['surface']
        )
        formula_label.pack(anchor=tk.W, pady=(0, 10))
        
        # 参数输入
        self.a = tk.DoubleVar(value=1.0)
        self.b = tk.DoubleVar(value=1.0 if func_type in ["正弦函数", "余弦函数", "指数函数", "对数函数"] else 0.0)
        self.c = tk.DoubleVar(value=0.0)
        
        params = [("a", self.a), ("b", self.b), ("c", self.c)]
        
        for param, var in params:
            param_frame = tk.Frame(self.param_frame, bg=self.theme['surface'])
            param_frame.pack(fill=tk.X, pady=2)
            
            tk.Label(
                param_frame,
                text=f"{param}:",
                font=('Segoe UI', 9),
                fg=self.theme['on_surface'],
                bg=self.theme['surface'],
                width=3
            ).pack(side=tk.LEFT)
            
            entry = tk.Entry(
                param_frame,
                textvariable=var,
                font=('Segoe UI', 9),
                width=15
            )
            entry.pack(side=tk.LEFT, padx=(5, 0))
    
    def get_formula_text(self, func_type):
        """获取函数公式文本"""
        formulas = {
            "二次函数": "📐 y = a·x² + b·x + c",
            "正弦函数": "〰️ y = a·sin(b·x + c)",
            "余弦函数": "〰️ y = a·cos(b·x + c)",
            "正切函数": "📈 y = a·tan(b·x + c)",
            "指数函数": "📊 y = a·e^(b·x) + c",
            "对数函数": "📉 y = a·log(b·x + c)"
        }
        return formulas.get(func_type, "")
    
    def plot_function(self):
        """绘制函数"""
        try:
            func_type = self.function_type.get()
            params = (self.a.get(), self.b.get(), self.c.get())
            
            # 验证参数
            is_valid, error_msg = MathUtils.validate_function_parameters(func_type, *params)
            if not is_valid:
                messagebox.showerror("参数错误", error_msg)
                return
            
            # 清除之前的函数
            self.math_calculator.clear_functions()
            
            # 添加当前函数
            self.math_calculator.add_function(func_type, params, 'b')
            
            # 绘制函数
            ranges = {'x_range': (-5, 5), 'y_range': (-5, 5)}
            options = {'show_extrema': True, 'show_roots': True, 'show_intersection': False, 'show_grid_points': False}
            
            self.plot_area.plot_functions(self.math_calculator.functions, ranges, options)
            
        except Exception as e:
            messagebox.showerror("绘制错误", f"绘制函数时发生错误: {str(e)}")
    
    def add_function(self):
        """添加函数"""
        try:
            func_type = self.function_type.get()
            params = (self.a.get(), self.b.get(), self.c.get())
            
            # 验证参数
            is_valid, error_msg = MathUtils.validate_function_parameters(func_type, *params)
            if not is_valid:
                messagebox.showerror("参数错误", error_msg)
                return
            
            # 选择颜色
            from config.settings import FUNCTION_COLORS
            color = FUNCTION_COLORS[self.math_calculator.get_function_count() % len(FUNCTION_COLORS)]
            
            # 添加函数
            self.math_calculator.add_function(func_type, params, color)
            
            # 重新绘制
            ranges = {'x_range': (-5, 5), 'y_range': (-5, 5)}
            options = {'show_extrema': True, 'show_roots': True, 'show_intersection': True, 'show_grid_points': False}
            
            self.plot_area.plot_functions(self.math_calculator.functions, ranges, options)
            
        except Exception as e:
            messagebox.showerror("添加错误", f"添加函数时发生错误: {str(e)}")
    
    def clear_plot(self):
        """清除图形"""
        self.math_calculator.clear_functions()
        self.plot_area.clear_plot()
    
    def save_plot(self):
        """保存图像"""
        success, message = self.plot_area.save_plot()
        if success:
            messagebox.showinfo("保存成功", message)
        else:
            messagebox.showerror("保存错误", message)

    def show_font_settings(self):
        """显示字体设置窗口"""
        try:
            FontSettingsWindow(
                self.parent,
                self.font_manager,
                self.on_font_changed
            )
        except Exception as e:
            messagebox.showerror("字体设置错误", f"打开字体设置窗口失败: {str(e)}")

    def on_font_changed(self):
        """字体更改后的回调"""
        try:
            # 更新字体信息显示
            self.update_font_info()
            # 调用主窗口的字体更改回调
            self.font_changed_callback()
        except Exception as e:
            print(f"字体更改回调错误: {e}")

    def set_default_function(self):
        """设置默认函数并绘制"""
        self.function_type.set("二次函数")
        self.update_parameters()
        self.plot_function()
