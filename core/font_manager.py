# -*- coding: utf-8 -*-
"""
字体管理模块
"""

import platform
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from typing import List
from config.settings import (
    WINDOWS_CHINESE_FONTS, MACOS_CHINESE_FONTS, LINUX_CHINESE_FONTS,
    CHINESE_FONT_KEYWORDS, FALLBACK_FONTS, MATPLOTLIB_CONFIG
)


class FontManager:
    """字体管理器类"""
    
    def __init__(self):
        """初始化字体管理器"""
        self.chinese_font = None
        self.available_chinese_fonts = []
        self.setup_chinese_font()
    
    def test_font_chinese_support(self, font_name: str) -> bool:
        """
        测试字体是否支持中文显示
        
        Args:
            font_name: 字体名称
            
        Returns:
            是否支持中文
        """
        try:
            # 创建一个小的测试图形
            test_fig = plt.figure(figsize=(1, 1))
            test_ax = test_fig.add_subplot(111)
            
            # 临时设置字体
            original_font = plt.rcParams['font.sans-serif'][0] if plt.rcParams['font.sans-serif'] else 'DejaVu Sans'
            plt.rcParams['font.sans-serif'] = [font_name]
            
            # 尝试渲染中文文本
            test_text = test_ax.text(0.5, 0.5, "中文测试", fontsize=12)
            
            # 获取渲染后的字体信息
            actual_font = test_text.get_fontname()
            
            # 恢复原字体设置
            plt.rcParams['font.sans-serif'] = [original_font]
            plt.close(test_fig)
            
            # 如果实际使用的字体与设置的字体相同或相近，则认为支持中文
            return font_name.lower() in actual_font.lower() or actual_font.lower() in font_name.lower()
            
        except Exception as e:
            print(f"测试字体 {font_name} 时出错: {e}")
            return False
    
    def get_verified_chinese_fonts(self) -> List[str]:
        """
        获取经过验证的中文字体列表
        
        Returns:
            支持中文的字体列表
        """
        # 获取系统类型
        system = platform.system()
        
        # 根据系统定义已知的中文字体
        if system == "Windows":
            known_chinese_fonts = WINDOWS_CHINESE_FONTS
        elif system == "Darwin":  # macOS
            known_chinese_fonts = MACOS_CHINESE_FONTS
        else:  # Linux
            known_chinese_fonts = LINUX_CHINESE_FONTS
        
        # 获取系统中所有可用字体
        available_fonts = set([f.name for f in fm.fontManager.ttflist])
        
        # 筛选出系统中存在的已知中文字体
        verified_fonts = []
        for font in known_chinese_fonts:
            if font in available_fonts:
                verified_fonts.append(font)
        
        # 如果没有找到已知的中文字体，尝试通过关键词筛选
        if not verified_fonts:
            for font in available_fonts:
                if any(keyword in font for keyword in CHINESE_FONT_KEYWORDS):
                    verified_fonts.append(font)
        
        # 添加一些通用的Unicode字体作为备用
        for font in FALLBACK_FONTS:
            if font in available_fonts and font not in verified_fonts:
                verified_fonts.append(font)
        
        return verified_fonts[:20]  # 限制返回数量
    
    def setup_chinese_font(self) -> None:
        """设置中文字体"""
        try:
            # 配置matplotlib设置
            for key, value in MATPLOTLIB_CONFIG.items():
                plt.rcParams[key] = value
            
            # 获取经过验证的中文字体
            chinese_fonts = self.get_verified_chinese_fonts()
            
            # 选择第一个可用的字体
            if chinese_fonts:
                selected_font = chinese_fonts[0]
            else:
                print("警告: 未找到合适的中文字体")
                selected_font = 'DejaVu Sans'  # 备用字体
            
            # 配置matplotlib的中文字体
            plt.rcParams['font.sans-serif'] = [selected_font]
            
            # 保存字体信息和字体列表
            self.chinese_font = selected_font
            self.available_chinese_fonts = chinese_fonts
            print(f"已设置中文字体: {selected_font}")
            
        except Exception as e:
            print(f"设置中文字体时出错: {e}")
            # 使用默认设置作为备用方案
            plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
            for key, value in MATPLOTLIB_CONFIG.items():
                plt.rcParams[key] = value
            self.chinese_font = 'DejaVu Sans'
            self.available_chinese_fonts = ['DejaVu Sans']
    
    def set_font(self, font_name: str) -> bool:
        """
        设置指定的字体
        
        Args:
            font_name: 字体名称
            
        Returns:
            设置是否成功
        """
        try:
            if font_name in self.available_chinese_fonts:
                plt.rcParams['font.sans-serif'] = [font_name]
                self.chinese_font = font_name
                print(f"字体已更改为: {font_name}")
                return True
            else:
                print(f"字体 {font_name} 不在可用列表中")
                return False
        except Exception as e:
            print(f"设置字体时出错: {e}")
            return False
    
    def get_current_font(self) -> str:
        """获取当前字体"""
        return self.chinese_font
    
    def get_available_fonts(self) -> List[str]:
        """获取可用字体列表"""
        return self.available_chinese_fonts.copy()
    
    def reset_to_default(self) -> None:
        """重置为默认字体"""
        if self.available_chinese_fonts:
            default_font = self.available_chinese_fonts[0]
            self.set_font(default_font)
