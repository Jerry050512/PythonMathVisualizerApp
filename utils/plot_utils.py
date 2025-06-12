# -*- coding: utf-8 -*-
"""
绘图工具函数模块
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Any
from config.settings import DEFAULT_SAVE_FILENAME, SAVE_DPI


class PlotUtils:
    """绘图工具类"""
    
    @staticmethod
    def setup_axes(ax, x_min: float, x_max: float, y_min: float, y_max: float, 
                   title: str = "数学函数可视化", chinese_font: str = "DejaVu Sans") -> None:
        """
        设置坐标轴属性
        
        Args:
            ax: matplotlib轴对象
            x_min, x_max: x轴范围
            y_min, y_max: y轴范围
            title: 图形标题
            chinese_font: 中文字体
        """
        ax.clear()
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.axhline(0, color='black', linewidth=0.8)
        ax.axvline(0, color='black', linewidth=0.8)
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.set_title(title, fontsize=14, fontfamily=chinese_font)
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
    
    @staticmethod
    def plot_extrema_points(ax, x: np.ndarray, y: np.ndarray, func_type: str, 
                           params: Tuple[float, float, float], x_range: Tuple[float, float],
                           chinese_font: str = "DejaVu Sans") -> None:
        """
        绘制函数的极值点
        
        Args:
            ax: matplotlib轴对象
            x: x坐标数组
            y: y坐标数组
            func_type: 函数类型
            params: 函数参数
            x_range: x轴范围
            chinese_font: 中文字体
        """
        if func_type == "二次函数":
            a, b, c = params
            vertex_x = -b / (2 * a)
            vertex_y = a * vertex_x**2 + b * vertex_x + c
            
            if x_range[0] <= vertex_x <= x_range[1]:
                ax.plot(vertex_x, vertex_y, 'ro', markersize=8)
                ax.annotate(f'顶点\n({vertex_x:.2f}, {vertex_y:.2f})', 
                           xy=(vertex_x, vertex_y), xytext=(10, 10),
                           textcoords='offset points', fontsize=9,
                           bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                           fontfamily=chinese_font)
        
        elif func_type in ["正弦函数", "余弦函数"]:
            dy = np.diff(y)
            extrema_indices = []
            
            for i in range(1, len(dy)):
                if dy[i-1] * dy[i] < 0:
                    extrema_indices.append(i)
            
            for idx in extrema_indices[:5]:
                x_ext = x[idx]
                y_ext = y[idx]
                ext_type = "最大值" if dy[idx-1] > 0 else "最小值"
                ax.plot(x_ext, y_ext, 'ro', markersize=6)
                ax.annotate(f'{ext_type}\n({x_ext:.2f}, {y_ext:.2f})', 
                           xy=(x_ext, y_ext), xytext=(10, 10),
                           textcoords='offset points', fontsize=8,
                           bbox=dict(boxstyle='round,pad=0.3', facecolor='orange', alpha=0.7),
                           fontfamily=chinese_font)
    
    @staticmethod
    def plot_roots(ax, x: np.ndarray, y: np.ndarray, x_range: Tuple[float, float],
                   chinese_font: str = "DejaVu Sans") -> None:
        """
        绘制函数的零点
        
        Args:
            ax: matplotlib轴对象
            x: x坐标数组
            y: y坐标数组
            x_range: x轴范围
            chinese_font: 中文字体
        """
        roots = []
        tolerance = 0.1
        
        for i in range(1, len(y)):
            if not (np.isnan(y[i]) or np.isnan(y[i-1])):
                if y[i-1] * y[i] <= 0 and abs(y[i]) < tolerance:
                    if abs(y[i] - y[i-1]) > 1e-10:
                        root_x = x[i-1] - y[i-1] * (x[i] - x[i-1]) / (y[i] - y[i-1])
                        roots.append(root_x)
        
        roots = list(set([round(r, 2) for r in roots]))
        roots.sort()
        
        for root in roots[:5]:
            if x_range[0] <= root <= x_range[1]:
                ax.plot(root, 0, 'go', markersize=8)
                ax.annotate(f'零点\n({root:.2f}, 0)', 
                           xy=(root, 0), xytext=(10, -20),
                           textcoords='offset points', fontsize=9,
                           bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7),
                           fontfamily=chinese_font)
    
    @staticmethod
    def plot_intersections(ax, functions: List[Dict], x_range: Tuple[float, float], 
                          y_range: Tuple[float, float], chinese_font: str = "DejaVu Sans") -> None:
        """
        绘制多个函数之间的交点
        
        Args:
            ax: matplotlib轴对象
            functions: 函数列表
            x_range: x轴范围
            y_range: y轴范围
            chinese_font: 中文字体
        """
        if len(functions) < 2:
            return
        
        from core.math_functions import MathFunctionCalculator
        calculator = MathFunctionCalculator()
        
        x = np.linspace(x_range[0], x_range[1], 1000)
        
        for i in range(len(functions)):
            for j in range(i + 1, len(functions)):
                intersections = calculator.find_intersections(x, functions[i], functions[j])
                
                for int_x, int_y in intersections:
                    if (x_range[0] <= int_x <= x_range[1] and 
                        y_range[0] <= int_y <= y_range[1]):
                        ax.plot(int_x, int_y, 'mo', markersize=10)
                        ax.annotate(f'交点\n({int_x:.2f}, {int_y:.2f})', 
                                   xy=(int_x, int_y), xytext=(15, 15),
                                   textcoords='offset points', fontsize=9,
                                   bbox=dict(boxstyle='round,pad=0.3', facecolor='magenta', alpha=0.7),
                                   fontfamily=chinese_font)
    
    @staticmethod
    def plot_grid_points(ax, x_range: Tuple[float, float], y_range: Tuple[float, float]) -> None:
        """
        绘制坐标网格点
        
        Args:
            ax: matplotlib轴对象
            x_range: x轴范围
            y_range: y轴范围
        """
        x_grid = np.arange(int(x_range[0]), int(x_range[1]) + 1, 1)
        y_grid = np.arange(int(y_range[0]), int(y_range[1]) + 1, 1)
        
        for x_val in x_grid:
            for y_val in y_grid:
                ax.plot(x_val, y_val, 'k.', markersize=2, alpha=0.3)
    
    @staticmethod
    def save_plot(fig, filename: str = None) -> Tuple[bool, str]:
        """
        保存图形为PNG文件
        
        Args:
            fig: matplotlib图形对象
            filename: 文件名（可选）
            
        Returns:
            (成功标志, 消息)
        """
        try:
            if filename is None:
                filename = DEFAULT_SAVE_FILENAME
            
            fig.savefig(filename, dpi=SAVE_DPI, bbox_inches='tight')
            return True, f"图像已保存为 {filename}"
        except Exception as e:
            return False, f"保存图像时出错: {str(e)}"
