#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学函数可视化工具 - 美化版启动器（简化版）
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from config.settings import THEMES, DEFAULT_THEME
    from core.font_manager import FontManager
    from core.math_functions import MathFunctionCalculator
    from gui.plot_area import PlotArea
    from utils.math_utils import MathUtils
    from utils.plot_utils import PlotUtils
except ImportError as e:
    print(f"导入模块失败: {e}")
    sys.exit(1)


class BeautifulControlPanel:
    """美化版控制面板（简化版）"""
    
    def __init__(self, parent, math_calculator, font_manager, plot_area):
        self.parent = parent
        self.math_calculator = math_calculator
        self.font_manager = font_manager
        self.plot_area = plot_area
        
        # 当前主题
        self.current_theme = DEFAULT_THEME
        self.themes = THEMES
        
        self.create_beautiful_panel()
    
    def create_beautiful_panel(self):
        """创建美化的控制面板"""
        # 获取主题颜色
        theme = self.themes[self.current_theme]
        
        # 主框架
        self.main_frame = tk.Frame(
            self.parent, 
            bg=theme['background'],
            relief='flat'
        )
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # 创建标题区域
        self.create_title_area(theme)
        
        # 创建控制面板
        self.create_control_area(theme)
        
        # 创建绘图区域
        self.create_plot_area(theme)
    
    def create_title_area(self, theme):
        """创建标题区域"""
        title_frame = tk.Frame(self.main_frame, bg=theme['background'])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        # 主标题
        title_label = tk.Label(
            title_frame,
            text="📊 数学函数可视化工具",
            font=('', 20, 'bold'),
            fg=theme['primary'],
            bg=theme['background']
        )
        title_label.pack(anchor=tk.W)
        
        # 副标题
        subtitle_label = tk.Label(
            title_frame,
            text="现代化界面 • 多主题支持 • 实时绘制",
            font=('', 11),
            fg=theme['secondary'],
            bg=theme['background']
        )
        subtitle_label.pack(anchor=tk.W, pady=(5, 0))
        
        # 主题切换按钮
        theme_button = tk.Button(
            title_frame,
            text="🎨 切换主题",
            command=self.show_theme_selector,
            bg=theme['accent'],
            fg='white',
            font=('', 10, 'bold'),
            relief='flat',
            padx=15,
            pady=5,
            cursor='hand2'
        )
        theme_button.pack(side=tk.RIGHT)
    
    def create_control_area(self, theme):
        """创建控制区域"""
        # 控制面板卡片
        control_card = tk.Frame(
            self.main_frame,
            bg=theme['surface'],
            relief='flat',
            bd=1,
            highlightbackground=theme['border'],
            highlightthickness=1
        )
        control_card.pack(fill=tk.X, pady=(0, 15))
        
        # 卡片标题
        card_title = tk.Label(
            control_card,
            text="🎛️ 函数控制面板",
            font=('', 14, 'bold'),
            fg=theme['primary'],
            bg=theme['surface']
        )
        card_title.pack(anchor=tk.W, padx=20, pady=(15, 10))
        
        # 控制内容
        control_content = tk.Frame(control_card, bg=theme['surface'])
        control_content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        # 函数类型选择
        self.create_function_selector(control_content, theme)
        
        # 参数输入
        self.create_parameter_inputs(control_content, theme)
        
        # 操作按钮
        self.create_action_buttons(control_content, theme)
    
    def create_function_selector(self, parent, theme):
        """创建函数选择器"""
        func_frame = tk.Frame(parent, bg=theme['surface'])
        func_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            func_frame,
            text="选择函数类型:",
            font=('', 11, 'bold'),
            fg=theme['on_surface'],
            bg=theme['surface']
        ).pack(side=tk.LEFT)
        
        self.function_type = tk.StringVar(value="二次函数")
        function_menu = ttk.Combobox(
            func_frame,
            textvariable=self.function_type,
            values=["二次函数", "正弦函数", "余弦函数", "正切函数", "指数函数", "对数函数"],
            state="readonly",
            width=15,
            font=('', 10)
        )
        function_menu.pack(side=tk.LEFT, padx=(10, 0))
        function_menu.bind("<<ComboboxSelected>>", self.update_parameters)
    
    def create_parameter_inputs(self, parent, theme):
        """创建参数输入区域"""
        self.param_frame = tk.Frame(parent, bg=theme['surface'])
        self.param_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 初始化参数
        self.update_parameters()
    
    def update_parameters(self, event=None):
        """更新参数输入"""
        # 清除现有参数
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        
        theme = self.themes[self.current_theme]
        func_type = self.function_type.get()
        
        # 显示函数公式
        formula_label = tk.Label(
            self.param_frame,
            text=self.get_formula_text(func_type),
            font=('', 12, 'bold'),
            fg=theme['primary'],
            bg=theme['surface']
        )
        formula_label.pack(anchor=tk.W, pady=(0, 10))
        
        # 参数输入
        params_frame = tk.Frame(self.param_frame, bg=theme['surface'])
        params_frame.pack(fill=tk.X)
        
        # 创建参数输入框
        self.a = tk.DoubleVar(value=1.0)
        self.b = tk.DoubleVar(value=1.0 if func_type in ["正弦函数", "余弦函数", "指数函数", "对数函数"] else 0.0)
        self.c = tk.DoubleVar(value=0.0)
        
        for i, (param, var) in enumerate([("a", self.a), ("b", self.b), ("c", self.c)]):
            tk.Label(
                params_frame,
                text=f"{param}:",
                font=('', 10),
                fg=theme['on_surface'],
                bg=theme['surface']
            ).grid(row=0, column=i*2, padx=(0, 5), sticky=tk.W)
            
            entry = tk.Entry(
                params_frame,
                textvariable=var,
                width=8,
                font=('', 10),
                bg=theme['surface_variant'],
                fg=theme['on_surface'],
                relief='flat',
                bd=1
            )
            entry.grid(row=0, column=i*2+1, padx=(0, 15))
    
    def get_formula_text(self, func_type):
        """获取函数公式文本"""
        formulas = {
            "二次函数": "y = a·x² + b·x + c",
            "正弦函数": "y = a·sin(b·x + c)",
            "余弦函数": "y = a·cos(b·x + c)",
            "正切函数": "y = a·tan(b·x + c)",
            "指数函数": "y = a·e^(b·x) + c",
            "对数函数": "y = a·log(b·x + c)"
        }
        return formulas.get(func_type, "")
    
    def create_action_buttons(self, parent, theme):
        """创建操作按钮"""
        button_frame = tk.Frame(parent, bg=theme['surface'])
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        buttons = [
            ("📊 绘制函数", self.plot_function, theme['primary']),
            ("➕ 添加函数", self.add_function, theme['secondary']),
            ("🗑️ 清除图形", self.clear_plot, theme['danger']),
            ("💾 保存图像", self.save_plot, theme['success'])
        ]
        
        for text, command, color in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                bg=color,
                fg='white',
                font=('', 10, 'bold'),
                relief='flat',
                padx=15,
                pady=6,
                cursor='hand2'
            )
            btn.pack(side=tk.LEFT, padx=(0, 10))
            
            # 添加悬停效果
            self.add_hover_effect(btn, color)
    
    def add_hover_effect(self, button, original_color):
        """添加按钮悬停效果"""
        def on_enter(e):
            button.configure(bg=self.darken_color(original_color))
        
        def on_leave(e):
            button.configure(bg=original_color)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
    
    def darken_color(self, color):
        """使颜色变暗"""
        # 简单的颜色变暗算法
        if color.startswith('#'):
            color = color[1:]
        
        try:
            r = int(color[0:2], 16)
            g = int(color[2:4], 16)
            b = int(color[4:6], 16)
            
            r = max(0, r - 30)
            g = max(0, g - 30)
            b = max(0, b - 30)
            
            return f"#{r:02x}{g:02x}{b:02x}"
        except:
            return color
    
    def create_plot_area(self, theme):
        """创建绘图区域"""
        # 绘图卡片
        plot_card = tk.Frame(
            self.main_frame,
            bg=theme['surface'],
            relief='flat',
            bd=1,
            highlightbackground=theme['border'],
            highlightthickness=1
        )
        plot_card.pack(fill=tk.BOTH, expand=True)
        
        # 卡片标题
        plot_title = tk.Label(
            plot_card,
            text="📈 函数图形",
            font=('', 14, 'bold'),
            fg=theme['primary'],
            bg=theme['surface']
        )
        plot_title.pack(anchor=tk.W, padx=20, pady=(15, 10))
        
        # 绘图区域
        plot_frame = tk.Frame(plot_card, bg=theme['surface'])
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))
        
        # 创建绘图区域
        self.plot_area = PlotArea(plot_frame, self.font_manager)
    
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
    
    def show_theme_selector(self):
        """显示主题选择器"""
        # 简化的主题选择对话框
        dialog = tk.Toplevel(self.parent)
        dialog.title("选择主题")
        dialog.geometry("300x200")
        dialog.resizable(False, False)
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # 居中显示
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (150)
        y = (dialog.winfo_screenheight() // 2) - (100)
        dialog.geometry(f'300x200+{x}+{y}')
        
        theme = self.themes[self.current_theme]
        dialog.configure(bg=theme['background'])
        
        tk.Label(
            dialog,
            text="🎨 选择主题",
            font=('', 14, 'bold'),
            fg=theme['on_surface'],
            bg=theme['background']
        ).pack(pady=20)
        
        # 主题选项
        selected_theme = tk.StringVar(value=self.current_theme)
        
        for theme_id, theme_config in self.themes.items():
            tk.Radiobutton(
                dialog,
                text=theme_config['name'],
                variable=selected_theme,
                value=theme_id,
                font=('', 11),
                fg=theme['on_surface'],
                bg=theme['background'],
                selectcolor=theme['primary']
            ).pack(anchor=tk.W, padx=50, pady=2)
        
        # 应用按钮
        def apply_theme():
            self.current_theme = selected_theme.get()
            dialog.destroy()
            self.refresh_interface()
            messagebox.showinfo("主题应用", f"已应用 {self.themes[self.current_theme]['name']} 主题！")
        
        tk.Button(
            dialog,
            text="应用主题",
            command=apply_theme,
            bg=theme['primary'],
            fg='white',
            font=('', 10, 'bold'),
            relief='flat',
            padx=20,
            pady=5
        ).pack(pady=20)
    
    def refresh_interface(self):
        """刷新界面"""
        # 重新创建界面
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        self.create_beautiful_panel()


def main():
    """主函数"""
    print("🚀 启动美化版数学函数可视化工具...")
    
    try:
        # 创建主窗口
        root = tk.Tk()
        root.title("📊 数学函数可视化工具 - 美化版")
        root.geometry("1200x800")
        root.minsize(1000, 700)
        
        # 居中显示
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (600)
        y = (root.winfo_screenheight() // 2) - (400)
        root.geometry(f'1200x800+{x}+{y}')
        
        # 初始化核心组件
        font_manager = FontManager()
        math_calculator = MathFunctionCalculator()
        
        # 创建美化的控制面板
        app = BeautifulControlPanel(root, math_calculator, font_manager, None)
        
        # 设置默认函数并绘制
        app.plot_function()
        
        print("✅ 启动成功！")
        root.mainloop()
        
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        messagebox.showerror("启动错误", f"应用启动失败：\n{e}")


if __name__ == "__main__":
    main()
