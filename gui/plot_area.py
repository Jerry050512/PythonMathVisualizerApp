# -*- coding: utf-8 -*-
"""
绘图区域模块
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from typing import List, Dict, Tuple, Any
from config.settings import FIGURE_SIZE, FIGURE_DPI, FIGURE_FACECOLOR, AXES_FACECOLOR, PLOT_POINTS
from utils.plot_utils import PlotUtils
from core.math_functions import MathFunctionCalculator


class PlotArea:
    """绘图区域类"""
    
    def __init__(self, parent, font_manager):
        """
        初始化绘图区域
        
        Args:
            parent: 父容器
            font_manager: 字体管理器实例
        """
        self.parent = parent
        self.font_manager = font_manager
        
        # 创建绘图区域
        self.create_plot_area()
    
    def create_plot_area(self):
        """创建绘图区域"""
        self.plot_frame = ttk.Frame(self.parent)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建matplotlib图形对象
        self.fig = Figure(figsize=FIGURE_SIZE, dpi=FIGURE_DPI, facecolor=FIGURE_FACECOLOR)
        self.ax = self.fig.add_subplot(111)
        
        # 设置图形样式
        self.setup_axes_style()
        
        # 创建tkinter画布并嵌入matplotlib图形
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 创建状态栏
        self.status_bar = ttk.Label(
            self.plot_frame, 
            text="就绪", 
            relief=tk.SUNKEN, 
            anchor=tk.W, 
            font=('', 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_axes_style(self):
        """设置坐标轴样式"""
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_facecolor(AXES_FACECOLOR)
        self.ax.axhline(0, color='black', linewidth=0.8)
        self.ax.axvline(0, color='black', linewidth=0.8)
    
    def plot_functions(self, functions: List[Dict], ranges: Dict[str, Tuple[float, float]], 
                      options: Dict[str, bool]):
        """
        绘制所有函数
        
        Args:
            functions: 函数列表
            ranges: 绘图范围
            options: 显示选项
        """
        try:
            # 获取范围
            x_range = ranges['x_range']
            y_range = ranges['y_range']
            
            # 设置坐标轴
            PlotUtils.setup_axes(
                self.ax, 
                x_range[0], x_range[1], 
                y_range[0], y_range[1],
                chinese_font=self.font_manager.get_current_font()
            )
            
            # 生成x坐标数组
            x = np.linspace(x_range[0], x_range[1], PLOT_POINTS)
            
            # 创建数学计算器实例
            calculator = MathFunctionCalculator()
            
            # 绘制所有函数
            for i, func in enumerate(functions):
                func_type = func['type']
                a, b, c = func['params']
                color = func['color']
                
                # 计算y值
                y = calculator.get_function_values(x, func_type, a, b, c)
                
                # 生成函数表达式
                expression = calculator.get_function_expression(func_type, a, b, c)
                
                # 绘制函数曲线
                self.ax.plot(x, y, color + '-', linewidth=2, label=expression)
                
                # 如果是最后一个函数，保存其信息用于显示特征点
                if i == len(functions) - 1:
                    self.current_x = x
                    self.current_y = y
                    self.current_func_type = func_type
                    self.current_params = (a, b, c)
            
            # 根据选项显示特征点
            if options.get('show_extrema', False) and functions:
                self.plot_extrema(x_range)
            
            if options.get('show_roots', False) and functions:
                self.plot_roots(x_range)
            
            if options.get('show_intersection', False) and len(functions) >= 2:
                PlotUtils.plot_intersections(
                    self.ax, functions, x_range, y_range,
                    self.font_manager.get_current_font()
                )
            
            if options.get('show_grid_points', False):
                PlotUtils.plot_grid_points(self.ax, x_range, y_range)
            
            # 添加图例
            self.ax.legend(loc='best', prop={
                'family': self.font_manager.get_current_font(), 
                'size': 9
            })
            
            # 更新画布显示
            self.canvas.draw()
            self.status_bar.config(text=f"已绘制 {len(functions)} 个函数")
        
        except Exception as e:
            self.status_bar.config(text=f"错误: {str(e)}")
            raise e
    
    def plot_extrema(self, x_range: Tuple[float, float]):
        """绘制极值点"""
        if hasattr(self, 'current_func_type'):
            PlotUtils.plot_extrema_points(
                self.ax, 
                self.current_x, 
                self.current_y, 
                self.current_func_type,
                self.current_params,
                x_range,
                self.font_manager.get_current_font()
            )
    
    def plot_roots(self, x_range: Tuple[float, float]):
        """绘制零点"""
        if hasattr(self, 'current_y'):
            PlotUtils.plot_roots(
                self.ax, 
                self.current_x, 
                self.current_y, 
                x_range,
                self.font_manager.get_current_font()
            )
    
    def clear_plot(self):
        """清除所有图形和数据"""
        self.ax.clear()
        self.setup_axes_style()
        self.canvas.draw()
        self.status_bar.config(text="图形已清除")
        
        # 清除当前函数信息
        if hasattr(self, 'current_x'):
            delattr(self, 'current_x')
        if hasattr(self, 'current_y'):
            delattr(self, 'current_y')
        if hasattr(self, 'current_func_type'):
            delattr(self, 'current_func_type')
        if hasattr(self, 'current_params'):
            delattr(self, 'current_params')
    
    def save_plot(self, filename: str = None) -> Tuple[bool, str]:
        """
        保存当前图形
        
        Args:
            filename: 文件名（可选）
            
        Returns:
            (成功标志, 消息)
        """
        success, message = PlotUtils.save_plot(self.fig, filename)
        if success:
            self.status_bar.config(text=message)
        else:
            self.status_bar.config(text=f"保存错误: {message}")
        
        return success, message
