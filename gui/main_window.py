# -*- coding: utf-8 -*-
"""
主窗口模块
"""

import tkinter as tk
from tkinter import ttk, messagebox
from config.settings import APP_TITLE, APP_GEOMETRY, APP_BACKGROUND, TTK_THEME, ACCENT_BUTTON_STYLE
from core.font_manager import FontManager
from core.math_functions import MathFunctionCalculator
from .control_panel import ControlPanel
from .plot_area import PlotArea
from .font_settings import FontSettingsWindow


class MathVisualizerApp:
    """数学函数可视化工具主应用程序类"""
    
    def __init__(self, root):
        """
        初始化主应用程序
        
        Args:
            root: tkinter根窗口
        """
        self.root = root
        self.setup_window()
        
        # 初始化核心组件
        self.font_manager = FontManager()
        self.math_calculator = MathFunctionCalculator()
        
        # 设置ttk主题样式
        self.setup_styles()
        
        # 创建主界面框架
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 创建界面组件
        self.create_components()
        
        # 设置默认函数并绘制
        self.control_panel.set_default_function()
    
    def setup_window(self):
        """设置主窗口属性"""
        self.root.title(APP_TITLE)
        self.root.geometry(APP_GEOMETRY)
        self.root.configure(bg=APP_BACKGROUND)
    
    def setup_styles(self):
        """设置ttk主题样式"""
        self.style = ttk.Style()
        self.style.theme_use(TTK_THEME)
        
        # 配置强调按钮样式
        self.style.configure("Accent.TButton", **ACCENT_BUTTON_STYLE)
        self.style.map("Accent.TButton", background=[("active", "#3a70b0")])
    
    def create_components(self):
        """创建界面组件"""
        # 创建控制面板
        self.control_panel = ControlPanel(
            self.main_frame, 
            self.math_calculator, 
            self.font_manager,
            self.on_plot_function,
            self.on_add_function,
            self.on_clear_plot,
            self.on_save_plot,
            self.on_show_font_settings
        )
        
        # 创建绘图区域
        self.plot_area = PlotArea(self.main_frame, self.font_manager)
        
        # 连接控制面板和绘图区域
        self.control_panel.set_plot_area(self.plot_area)
    
    def on_plot_function(self):
        """绘制当前函数（清除之前的函数）"""
        try:
            # 获取函数参数
            func_type, params = self.control_panel.get_current_function()
            ranges = self.control_panel.get_plot_ranges()
            options = self.control_panel.get_display_options()
            
            # 清除之前的函数
            self.math_calculator.clear_functions()
            
            # 添加当前函数
            color = 'b'  # 默认颜色
            self.math_calculator.add_function(func_type, params, color)
            
            # 绘制函数
            self.plot_area.plot_functions(
                self.math_calculator.functions, 
                ranges, 
                options
            )
            
            # 更新函数信息显示
            expression = self.math_calculator.get_function_expression(func_type, *params)
            self.control_panel.update_function_info(expression, func_type, params)
            
        except Exception as e:
            messagebox.showerror("错误", f"绘制函数时发生错误: {str(e)}")
    
    def on_add_function(self):
        """添加函数到列表"""
        try:
            # 获取函数参数
            func_type, params = self.control_panel.get_current_function()
            ranges = self.control_panel.get_plot_ranges()
            options = self.control_panel.get_display_options()
            
            # 选择颜色
            from config.settings import FUNCTION_COLORS
            color = FUNCTION_COLORS[self.math_calculator.get_function_count() % len(FUNCTION_COLORS)]
            
            # 添加函数
            self.math_calculator.add_function(func_type, params, color)
            
            # 重新绘制所有函数
            self.plot_area.plot_functions(
                self.math_calculator.functions, 
                ranges, 
                options
            )
            
            # 更新函数信息显示
            expression = self.math_calculator.get_function_expression(func_type, *params)
            self.control_panel.update_function_info(expression, func_type, params)
            
        except Exception as e:
            messagebox.showerror("错误", f"添加函数时发生错误: {str(e)}")
    
    def on_clear_plot(self):
        """清除所有图形和数据"""
        self.math_calculator.clear_functions()
        self.plot_area.clear_plot()
        self.control_panel.clear_function_info()
    
    def on_save_plot(self):
        """保存当前图形"""
        success, message = self.plot_area.save_plot()
        if success:
            messagebox.showinfo("保存成功", message)
        else:
            messagebox.showerror("保存错误", message)
    
    def on_show_font_settings(self):
        """显示字体设置窗口"""
        font_window = FontSettingsWindow(
            self.root, 
            self.font_manager,
            self.on_font_changed
        )
    
    def on_font_changed(self):
        """字体更改后的回调"""
        # 重新绘制图形以应用新字体
        if self.math_calculator.functions:
            ranges = self.control_panel.get_plot_ranges()
            options = self.control_panel.get_display_options()
            self.plot_area.plot_functions(
                self.math_calculator.functions, 
                ranges, 
                options
            )


def main():
    """主函数"""
    root = tk.Tk()
    app = MathVisualizerApp(root)
    
    # 设置应用程序样式
    root.tk_setPalette(
        background='#f0f0f0', 
        foreground='#333333', 
        activeBackground='#4a90d9', 
        activeForeground='white'
    )
    
    root.mainloop()


if __name__ == "__main__":
    main()
