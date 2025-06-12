# -*- coding: utf-8 -*-
"""
数学函数计算核心模块
"""

import numpy as np
from typing import Tuple, List, Dict, Any


class MathFunctionCalculator:
    """数学函数计算器类"""
    
    def __init__(self):
        """初始化计算器"""
        self.functions = []  # 存储所有已添加的函数信息
    
    def get_function_values(self, x: np.ndarray, func_type: str, a: float, b: float, c: float) -> np.ndarray:
        """
        根据函数类型和参数计算y值
        
        Args:
            x: x坐标数组
            func_type: 函数类型
            a, b, c: 函数参数
            
        Returns:
            y坐标数组
        """
        if func_type == "二次函数":
            return a * x**2 + b * x + c
        elif func_type == "正弦函数":
            return a * np.sin(b * x + c)
        elif func_type == "余弦函数":
            return a * np.cos(b * x + c)
        elif func_type == "正切函数":
            y = a * np.tan(b * x + c)
            y[np.abs(y) > 50] = np.nan  # 限制极值
            return y
        elif func_type == "指数函数":
            return a * np.exp(b * x) + c
        elif func_type == "对数函数":
            arg = b * x + c
            arg[arg <= 0] = np.nan  # 处理定义域
            return a * np.log(arg)
        return np.zeros_like(x)
    
    def get_function_expression(self, func_type: str, a: float, b: float, c: float) -> str:
        """
        生成函数表达式字符串
        
        Args:
            func_type: 函数类型
            a, b, c: 函数参数
            
        Returns:
            函数表达式字符串
        """
        if func_type == "二次函数":
            return f"$y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}$"
        elif func_type == "正弦函数":
            return f"y = {a:.2f}·sin({b:.2f}x + {c:.2f})"
        elif func_type == "余弦函数":
            return f"y = {a:.2f}·cos({b:.2f}x + {c:.2f})"
        elif func_type == "正切函数":
            return f"y = {a:.2f}·tan({b:.2f}x + {c:.2f})"
        elif func_type == "指数函数":
            return f"y = {a:.2f}·e^({b:.2f}x) + {c:.2f}"
        elif func_type == "对数函数":
            return f"y = {a:.2f}·log({b:.2f}x + {c:.2f})"
        return ""
    
    def add_function(self, func_type: str, params: Tuple[float, float, float], color: str) -> None:
        """
        添加函数到列表
        
        Args:
            func_type: 函数类型
            params: 函数参数 (a, b, c)
            color: 函数颜色
        """
        self.functions.append({
            'type': func_type,
            'params': params,
            'color': color
        })
    
    def clear_functions(self) -> None:
        """清除所有函数"""
        self.functions = []
    
    def get_function_count(self) -> int:
        """获取函数数量"""
        return len(self.functions)
    
    def calculate_quadratic_features(self, a: float, b: float, c: float) -> Dict[str, Any]:
        """
        计算二次函数的特征点
        
        Args:
            a, b, c: 二次函数参数
            
        Returns:
            包含特征点信息的字典
        """
        features = {}
        
        # 顶点
        vertex_x = -b / (2 * a)
        vertex_y = a * vertex_x**2 + b * vertex_x + c
        features['vertex'] = (vertex_x, vertex_y)
        
        # 判别式和零点
        discriminant = b**2 - 4 * a * c
        if discriminant > 0:
            root1 = (-b + np.sqrt(discriminant)) / (2 * a)
            root2 = (-b - np.sqrt(discriminant)) / (2 * a)
            features['roots'] = [root1, root2]
        elif discriminant == 0:
            root = -b / (2 * a)
            features['roots'] = [root]
        else:
            features['roots'] = []
        
        # y轴交点
        features['y_intercept'] = c
        
        return features
    
    def calculate_trig_features(self, a: float, b: float, c: float) -> Dict[str, Any]:
        """
        计算三角函数的特征
        
        Args:
            a, b, c: 三角函数参数
            
        Returns:
            包含特征信息的字典
        """
        features = {}
        features['amplitude'] = abs(a)
        features['period'] = 2 * np.pi / abs(b) if b != 0 else float('inf')
        features['phase'] = c
        
        return features
    
    def find_roots(self, x: np.ndarray, y: np.ndarray, tolerance: float = 0.1) -> List[float]:
        """
        寻找函数的零点
        
        Args:
            x: x坐标数组
            y: y坐标数组
            tolerance: 容差
            
        Returns:
            零点列表
        """
        roots = []
        
        for i in range(1, len(y)):
            if not (np.isnan(y[i]) or np.isnan(y[i-1])):
                if y[i-1] * y[i] <= 0 and abs(y[i]) < tolerance:
                    if abs(y[i] - y[i-1]) > 1e-10:
                        root_x = x[i-1] - y[i-1] * (x[i] - x[i-1]) / (y[i] - y[i-1])
                        roots.append(root_x)
        
        # 去重并排序
        roots = list(set([round(r, 2) for r in roots]))
        roots.sort()
        
        return roots[:5]  # 最多返回5个零点
    
    def find_extrema(self, x: np.ndarray, y: np.ndarray) -> List[Tuple[float, float, str]]:
        """
        寻找函数的极值点
        
        Args:
            x: x坐标数组
            y: y坐标数组
            
        Returns:
            极值点列表，每个元素为 (x, y, type)
        """
        extrema = []
        dy = np.diff(y)
        
        for i in range(1, len(dy)):
            if dy[i-1] * dy[i] < 0:
                x_ext = x[i]
                y_ext = y[i]
                ext_type = "最大值" if dy[i-1] > 0 else "最小值"
                extrema.append((x_ext, y_ext, ext_type))
        
        return extrema[:5]  # 最多返回5个极值点
    
    def find_intersections(self, x: np.ndarray, func1: Dict, func2: Dict) -> List[Tuple[float, float]]:
        """
        寻找两个函数的交点
        
        Args:
            x: x坐标数组
            func1: 第一个函数信息
            func2: 第二个函数信息
            
        Returns:
            交点列表
        """
        y1 = self.get_function_values(x, func1['type'], *func1['params'])
        y2 = self.get_function_values(x, func2['type'], *func2['params'])
        
        diff = y1 - y2
        intersections = []
        
        for i in range(1, len(diff)):
            if not (np.isnan(diff[i]) or np.isnan(diff[i-1])):
                if diff[i-1] * diff[i] <= 0:
                    if abs(diff[i] - diff[i-1]) > 1e-10:
                        int_x = x[i-1] - diff[i-1] * (x[i] - x[i-1]) / (diff[i] - diff[i-1])
                        int_y = self.get_function_values(np.array([int_x]), func1['type'], *func1['params'])[0]
                        intersections.append((int_x, int_y))
        
        return intersections[:3]  # 最多返回3个交点
