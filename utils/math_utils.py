# -*- coding: utf-8 -*-
"""
数学计算工具函数模块
"""

import numpy as np
from typing import List, Dict, Any, Tuple


class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def calculate_function_features(func_type: str, a: float, b: float, c: float) -> List[str]:
        """
        计算函数的特征信息
        
        Args:
            func_type: 函数类型
            a, b, c: 函数参数
            
        Returns:
            特征信息列表
        """
        key_points = []
        
        if func_type == "二次函数":
            # 顶点
            vertex_x = -b / (2 * a)
            vertex_y = a * vertex_x**2 + b * vertex_x + c
            key_points.append(f"顶点: ({vertex_x:.2f}, {vertex_y:.2f})")
            
            # 判别式和零点
            discriminant = b**2 - 4 * a * c
            if discriminant > 0:
                root1 = (-b + np.sqrt(discriminant)) / (2 * a)
                root2 = (-b - np.sqrt(discriminant)) / (2 * a)
                key_points.append(f"零点: x₁={root1:.2f}, x₂={root2:.2f}")
            elif discriminant == 0:
                root = -b / (2 * a)
                key_points.append(f"零点: x={root:.2f} (二重根)")
            else:
                key_points.append("无实数零点")
            
            # y轴交点
            key_points.append(f"y轴交点: (0, {c:.2f})")
            
        elif func_type in ["正弦函数", "余弦函数"]:
            key_points.append(f"振幅: {abs(a):.2f}")
            key_points.append(f"周期: {2*np.pi/abs(b):.2f}")
            key_points.append(f"相位: {c:.2f}")
            
        elif func_type == "指数函数":
            if b < 0:
                key_points.append(f"水平渐近线: y={c:.2f}")
            y_intercept = a * np.exp(0) + c
            key_points.append(f"y轴交点: (0, {y_intercept:.2f})")
            
        elif func_type == "对数函数":
            try:
                root = (1 - c) / b
                key_points.append(f"零点: ({root:.2f}, 0)")
            except:
                key_points.append("无零点")
            
            vertical_asymptote = -c / b
            key_points.append(f"垂直渐近线: x={vertical_asymptote:.2f}")
        
        return key_points
    
    @staticmethod
    def validate_function_parameters(func_type: str, a: float, b: float, c: float) -> Tuple[bool, str]:
        """
        验证函数参数的有效性
        
        Args:
            func_type: 函数类型
            a, b, c: 函数参数
            
        Returns:
            (是否有效, 错误消息)
        """
        if func_type == "二次函数":
            if a == 0:
                return False, "二次函数的参数a不能为0"
        
        elif func_type in ["正弦函数", "余弦函数", "正切函数"]:
            if b == 0:
                return False, f"{func_type}的参数b不能为0"
        
        elif func_type == "指数函数":
            if a == 0:
                return False, "指数函数的参数a不能为0"
        
        elif func_type == "对数函数":
            if a == 0:
                return False, "对数函数的参数a不能为0"
            if b == 0:
                return False, "对数函数的参数b不能为0"
        
        return True, ""
    
    @staticmethod
    def get_optimal_range(func_type: str, a: float, b: float, c: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        根据函数类型获取最优的显示范围
        
        Args:
            func_type: 函数类型
            a, b, c: 函数参数
            
        Returns:
            ((x_min, x_max), (y_min, y_max))
        """
        if func_type == "二次函数":
            vertex_x = -b / (2 * a)
            x_range = (vertex_x - 5, vertex_x + 5)
            vertex_y = a * vertex_x**2 + b * vertex_x + c
            y_range = (vertex_y - 10, vertex_y + 10)
            
        elif func_type in ["正弦函数", "余弦函数"]:
            period = 2 * np.pi / abs(b) if b != 0 else 2 * np.pi
            x_range = (-2 * period, 2 * period)
            amplitude = abs(a)
            y_range = (-amplitude * 1.5, amplitude * 1.5)
            
        elif func_type == "正切函数":
            period = np.pi / abs(b) if b != 0 else np.pi
            x_range = (-2 * period, 2 * period)
            y_range = (-10, 10)
            
        elif func_type == "指数函数":
            x_range = (-5, 5)
            if b > 0:
                y_range = (c - 2, c + 20)
            else:
                y_range = (c - 20, c + 2)
                
        elif func_type == "对数函数":
            x_range = (0.1, 10)
            y_range = (-5, 5)
            
        else:
            x_range = (-5, 5)
            y_range = (-5, 5)
        
        return x_range, y_range
    
    @staticmethod
    def format_number(value: float, precision: int = 2) -> str:
        """
        格式化数字显示
        
        Args:
            value: 数值
            precision: 精度
            
        Returns:
            格式化后的字符串
        """
        if abs(value) < 1e-10:
            return "0"
        elif abs(value) > 1e6 or abs(value) < 1e-3:
            return f"{value:.{precision}e}"
        else:
            return f"{value:.{precision}f}"
    
    @staticmethod
    def is_valid_range(x_min: float, x_max: float, y_min: float, y_max: float) -> Tuple[bool, str]:
        """
        验证坐标范围的有效性
        
        Args:
            x_min, x_max: x轴范围
            y_min, y_max: y轴范围
            
        Returns:
            (是否有效, 错误消息)
        """
        if x_min >= x_max:
            return False, "x轴最小值必须小于最大值"
        if y_min >= y_max:
            return False, "y轴最小值必须小于最大值"
        if abs(x_max - x_min) < 1e-10:
            return False, "x轴范围过小"
        if abs(y_max - y_min) < 1e-10:
            return False, "y轴范围过小"
        
        return True, ""
