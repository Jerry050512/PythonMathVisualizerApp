# -*- coding: utf-8 -*-
"""
主题管理器模块 - 现代化界面主题
"""

import tkinter as tk
from tkinter import ttk
from typing import Dict, Any, Optional
from config.settings import THEMES, DEFAULT_THEME, BUTTON_STYLES, CARD_STYLE


class ThemeManager:
    """主题管理器类 - 管理应用程序的视觉主题"""
    
    def __init__(self):
        """初始化主题管理器"""
        self.current_theme = DEFAULT_THEME
        self.themes = THEMES
        self.style = None
        self._animation_jobs = {}
        
    def initialize_style(self, root: tk.Tk) -> None:
        """
        初始化TTK样式
        
        Args:
            root: 根窗口
        """
        self.style = ttk.Style(root)
        self.style.theme_use('clam')
        self.apply_theme(self.current_theme)
    
    def apply_theme(self, theme_name: str) -> None:
        """
        应用指定主题
        
        Args:
            theme_name: 主题名称
        """
        if theme_name not in self.themes:
            theme_name = DEFAULT_THEME
            
        self.current_theme = theme_name
        theme = self.themes[theme_name]
        
        # 配置TTK样式
        self._configure_ttk_styles(theme)
        
    def _configure_ttk_styles(self, theme: Dict[str, str]) -> None:
        """
        配置TTK组件样式
        
        Args:
            theme: 主题配置字典
        """
        if not self.style:
            return
            
        # === 基础样式配置 ===
        
        # Frame样式
        self.style.configure('Card.TFrame',
            background=theme['surface'],
            relief='flat',
            borderwidth=1,
            lightcolor=theme['border'],
            darkcolor=theme['border']
        )
        
        # LabelFrame样式
        self.style.configure('Modern.TLabelframe',
            background=theme['surface'],
            foreground=theme['on_surface'],
            relief='flat',
            borderwidth=1,
            lightcolor=theme['border'],
            darkcolor=theme['border']
        )
        
        self.style.configure('Modern.TLabelframe.Label',
            background=theme['surface'],
            foreground=theme['primary'],
            font=('', 11, 'bold')
        )
        
        # === 按钮样式 ===
        
        # 主要按钮
        self.style.configure('Primary.TButton',
            background=theme['primary'],
            foreground=theme['on_primary'],
            borderwidth=0,
            focuscolor='none',
            font=('', 10, 'bold'),
            padding=(20, 8)
        )
        
        self.style.map('Primary.TButton',
            background=[
                ('active', theme['primary_dark']),
                ('pressed', theme['primary_dark'])
            ],
            relief=[('pressed', 'flat'), ('!pressed', 'flat')]
        )
        
        # 次要按钮
        self.style.configure('Secondary.TButton',
            background=theme['surface'],
            foreground=theme['on_surface'],
            borderwidth=1,
            focuscolor='none',
            font=('', 10),
            padding=(16, 6)
        )
        
        self.style.map('Secondary.TButton',
            background=[
                ('active', theme['surface_variant']),
                ('pressed', theme['surface_variant'])
            ],
            bordercolor=[
                ('active', theme['primary']),
                ('!active', theme['border'])
            ]
        )
        
        # 成功按钮
        self.style.configure('Success.TButton',
            background=theme['success'],
            foreground='white',
            borderwidth=0,
            focuscolor='none',
            font=('', 10, 'bold'),
            padding=(16, 6)
        )
        
        # 危险按钮
        self.style.configure('Danger.TButton',
            background=theme['danger'],
            foreground='white',
            borderwidth=0,
            focuscolor='none',
            font=('', 10, 'bold'),
            padding=(16, 6)
        )
        
        # === 输入组件样式 ===
        
        # Entry样式
        self.style.configure('Modern.TEntry',
            fieldbackground=theme['surface'],
            foreground=theme['on_surface'],
            borderwidth=1,
            insertcolor=theme['primary'],
            selectbackground=theme['primary_light'],
            selectforeground=theme['on_primary']
        )
        
        self.style.map('Modern.TEntry',
            bordercolor=[
                ('focus', theme['primary']),
                ('!focus', theme['border'])
            ]
        )
        
        # Combobox样式
        self.style.configure('Modern.TCombobox',
            fieldbackground=theme['surface'],
            foreground=theme['on_surface'],
            borderwidth=1,
            selectbackground=theme['primary_light'],
            selectforeground=theme['on_primary']
        )
        
        # === 其他组件样式 ===
        
        # Label样式
        self.style.configure('Title.TLabel',
            background=theme['background'],
            foreground=theme['on_surface'],
            font=('', 14, 'bold')
        )
        
        self.style.configure('Subtitle.TLabel',
            background=theme['background'],
            foreground=theme['secondary'],
            font=('', 11)
        )
        
        self.style.configure('Caption.TLabel',
            background=theme['background'],
            foreground=theme['secondary'],
            font=('', 9)
        )
        
        # Checkbutton样式
        self.style.configure('Modern.TCheckbutton',
            background=theme['surface'],
            foreground=theme['on_surface'],
            focuscolor='none'
        )
        
        # Separator样式
        self.style.configure('Modern.TSeparator',
            background=theme['border']
        )
        
        # Notebook样式
        self.style.configure('Modern.TNotebook',
            background=theme['background'],
            borderwidth=0
        )
        
        self.style.configure('Modern.TNotebook.Tab',
            background=theme['surface_variant'],
            foreground=theme['on_surface'],
            padding=(20, 10),
            borderwidth=0
        )
        
        self.style.map('Modern.TNotebook.Tab',
            background=[
                ('selected', theme['surface']),
                ('active', theme['surface'])
            ],
            foreground=[
                ('selected', theme['primary']),
                ('active', theme['primary'])
            ]
        )
    
    def get_theme_colors(self, theme_name: Optional[str] = None) -> Dict[str, str]:
        """
        获取主题颜色配置
        
        Args:
            theme_name: 主题名称，默认为当前主题
            
        Returns:
            主题颜色字典
        """
        if theme_name is None:
            theme_name = self.current_theme
        return self.themes.get(theme_name, self.themes[DEFAULT_THEME])
    
    def get_available_themes(self) -> Dict[str, str]:
        """
        获取可用主题列表
        
        Returns:
            主题名称和显示名称的字典
        """
        return {name: config['name'] for name, config in self.themes.items()}
    
    def create_card_frame(self, parent: tk.Widget, theme_name: Optional[str] = None) -> ttk.Frame:
        """
        创建卡片样式的Frame
        
        Args:
            parent: 父组件
            theme_name: 主题名称
            
        Returns:
            配置好的Frame组件
        """
        frame = ttk.Frame(parent, style='Card.TFrame')
        return frame
    
    def create_modern_labelframe(self, parent: tk.Widget, text: str) -> ttk.LabelFrame:
        """
        创建现代化的LabelFrame
        
        Args:
            parent: 父组件
            text: 标签文本
            
        Returns:
            配置好的LabelFrame组件
        """
        return ttk.LabelFrame(parent, text=text, style='Modern.TLabelframe')
    
    def animate_color_transition(self, widget: tk.Widget, 
                                from_color: str, to_color: str, 
                                duration: int = 200) -> None:
        """
        颜色过渡动画
        
        Args:
            widget: 目标组件
            from_color: 起始颜色
            to_color: 结束颜色
            duration: 动画时长（毫秒）
        """
        # 简化版本，实际实现可以更复杂
        widget.configure(bg=to_color)


# 全局主题管理器实例
theme_manager = ThemeManager()
