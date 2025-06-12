# -*- coding: utf-8 -*-
"""
主题选择器组件
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from .theme_manager import theme_manager
from .modern_widgets import ModernButton
from config.settings import THEMES


class ThemeSelector:
    """主题选择器窗口"""
    
    def __init__(self, parent, callback: Callable):
        """
        初始化主题选择器
        
        Args:
            parent: 父窗口
            callback: 主题更改后的回调函数
        """
        self.parent = parent
        self.callback = callback
        self.current_theme = theme_manager.current_theme
        
        # 创建主题选择窗口
        self.create_theme_window()
    
    def create_theme_window(self):
        """创建主题选择窗口"""
        # 创建窗口
        self.theme_window = tk.Toplevel(self.parent)
        self.theme_window.title("🎨 主题设置")
        self.theme_window.geometry("600x500")
        self.theme_window.resizable(False, False)
        
        # 设置窗口为模态窗口
        self.theme_window.transient(self.parent)
        self.theme_window.grab_set()
        
        # 居中显示
        self._center_window()
        
        # 获取当前主题颜色
        colors = theme_manager.get_theme_colors()
        self.theme_window.configure(bg=colors['background'])
        
        # 创建界面内容
        self.create_header()
        self.create_theme_preview_area()
        self.create_theme_list()
        self.create_button_area()
    
    def _center_window(self):
        """居中显示窗口"""
        self.theme_window.update_idletasks()
        width = 600
        height = 500
        x = (self.theme_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.theme_window.winfo_screenheight() // 2) - (height // 2)
        self.theme_window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_header(self):
        """创建标题区域"""
        colors = theme_manager.get_theme_colors()
        
        header_frame = tk.Frame(self.theme_window, bg=colors['background'])
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        # 主标题
        title_label = tk.Label(
            header_frame,
            text="🎨 选择界面主题",
            font=('', 18, 'bold'),
            fg=colors['on_surface'],
            bg=colors['background']
        )
        title_label.pack(anchor=tk.W)
        
        # 副标题
        subtitle_label = tk.Label(
            header_frame,
            text="选择您喜欢的界面主题，让数学可视化更加美观",
            font=('', 11),
            fg=colors['secondary'],
            bg=colors['background']
        )
        subtitle_label.pack(anchor=tk.W, pady=(5, 0))
    
    def create_theme_preview_area(self):
        """创建主题预览区域"""
        colors = theme_manager.get_theme_colors()
        
        preview_frame = tk.Frame(self.theme_window, bg=colors['background'])
        preview_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # 预览标题
        preview_label = tk.Label(
            preview_frame,
            text="🔍 主题预览",
            font=('', 14, 'bold'),
            fg=colors['on_surface'],
            bg=colors['background']
        )
        preview_label.pack(anchor=tk.W, pady=(0, 10))
        
        # 预览卡片
        self.preview_card = tk.Frame(
            preview_frame,
            bg=colors['surface'],
            relief='flat',
            bd=1,
            highlightbackground=colors['border'],
            highlightthickness=1
        )
        self.preview_card.pack(fill=tk.X, pady=5)
        
        # 预览内容
        self.create_preview_content()
    
    def create_preview_content(self):
        """创建预览内容"""
        colors = theme_manager.get_theme_colors()
        
        # 清除现有内容
        for widget in self.preview_card.winfo_children():
            widget.destroy()
        
        # 预览标题
        preview_title = tk.Label(
            self.preview_card,
            text="📊 函数控制面板",
            font=('', 12, 'bold'),
            fg=colors['primary'],
            bg=colors['surface']
        )
        preview_title.pack(anchor=tk.W, padx=15, pady=(15, 5))
        
        # 预览按钮区域
        button_preview_frame = tk.Frame(self.preview_card, bg=colors['surface'])
        button_preview_frame.pack(fill=tk.X, padx=15, pady=(5, 15))
        
        # 示例按钮
        sample_buttons = [
            ("绘制函数", "primary"),
            ("添加函数", "secondary"),
            ("保存图像", "success")
        ]
        
        for text, style in sample_buttons:
            btn = tk.Button(
                button_preview_frame,
                text=text,
                font=('', 9),
                relief='flat',
                borderwidth=0,
                cursor='hand2',
                padx=12,
                pady=4
            )
            
            if style == "primary":
                btn.configure(bg=colors['primary'], fg=colors['on_primary'])
            elif style == "secondary":
                btn.configure(bg=colors['surface_variant'], fg=colors['on_surface'])
            elif style == "success":
                btn.configure(bg=colors['success'], fg='white')
            
            btn.pack(side=tk.LEFT, padx=(0, 8))
    
    def create_theme_list(self):
        """创建主题列表"""
        colors = theme_manager.get_theme_colors()
        
        list_frame = tk.Frame(self.theme_window, bg=colors['background'])
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # 列表标题
        list_label = tk.Label(
            list_frame,
            text="🌈 可用主题",
            font=('', 14, 'bold'),
            fg=colors['on_surface'],
            bg=colors['background']
        )
        list_label.pack(anchor=tk.W, pady=(0, 10))
        
        # 主题选项
        self.selected_theme = tk.StringVar(value=self.current_theme)
        
        for theme_id, theme_config in THEMES.items():
            theme_frame = tk.Frame(
                list_frame,
                bg=colors['surface'],
                relief='flat',
                bd=1,
                highlightbackground=colors['border'],
                highlightthickness=1
            )
            theme_frame.pack(fill=tk.X, pady=3)
            
            # 主题选择按钮
            theme_radio = tk.Radiobutton(
                theme_frame,
                text=f"{theme_config['name']}",
                variable=self.selected_theme,
                value=theme_id,
                font=('', 11),
                fg=colors['on_surface'],
                bg=colors['surface'],
                selectcolor=colors['primary'],
                activebackground=colors['surface_variant'],
                command=lambda t=theme_id: self.preview_theme(t)
            )
            theme_radio.pack(side=tk.LEFT, padx=15, pady=10)
            
            # 主题描述
            description = self.get_theme_description(theme_id)
            desc_label = tk.Label(
                theme_frame,
                text=description,
                font=('', 9),
                fg=colors['secondary'],
                bg=colors['surface']
            )
            desc_label.pack(side=tk.LEFT, padx=(10, 15))
            
            # 主题颜色预览
            color_frame = tk.Frame(theme_frame, bg=colors['surface'])
            color_frame.pack(side=tk.RIGHT, padx=15)
            
            theme_colors = THEMES[theme_id]
            preview_colors = [
                theme_colors['primary'],
                theme_colors['secondary'],
                theme_colors['accent']
            ]
            
            for color in preview_colors:
                color_box = tk.Frame(
                    color_frame,
                    bg=color,
                    width=20,
                    height=20,
                    relief='flat'
                )
                color_box.pack(side=tk.LEFT, padx=2)
    
    def get_theme_description(self, theme_id: str) -> str:
        """获取主题描述"""
        descriptions = {
            'modern_blue': '现代蓝色主题，清新专业',
            'elegant_dark': '优雅暗色主题，护眼舒适',
            'nature_green': '自然绿色主题，清新自然'
        }
        return descriptions.get(theme_id, '经典主题')
    
    def create_button_area(self):
        """创建按钮区域"""
        colors = theme_manager.get_theme_colors()
        
        button_frame = tk.Frame(self.theme_window, bg=colors['background'])
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # 应用按钮
        ModernButton(
            button_frame,
            text="应用主题",
            command=self.apply_theme,
            style="primary",
            icon="✨"
        ).pack(side=tk.RIGHT, padx=(10, 0))
        
        # 取消按钮
        ModernButton(
            button_frame,
            text="取消",
            command=self.theme_window.destroy,
            style="secondary"
        ).pack(side=tk.RIGHT)
        
        # 重置按钮
        ModernButton(
            button_frame,
            text="重置默认",
            command=self.reset_theme,
            style="secondary"
        ).pack(side=tk.LEFT)
    
    def preview_theme(self, theme_id: str):
        """预览主题"""
        theme_manager.apply_theme(theme_id)
        self.create_preview_content()
    
    def apply_theme(self):
        """应用选中的主题"""
        selected = self.selected_theme.get()
        theme_manager.apply_theme(selected)
        
        # 调用回调函数
        self.callback()
        
        # 显示成功消息
        theme_name = THEMES[selected]['name']
        messagebox.showinfo(
            "主题应用成功",
            f"已成功应用 {theme_name} 主题！"
        )
        
        self.theme_window.destroy()
    
    def reset_theme(self):
        """重置为默认主题"""
        from config.settings import DEFAULT_THEME
        self.selected_theme.set(DEFAULT_THEME)
        self.preview_theme(DEFAULT_THEME)
