# -*- coding: utf-8 -*-
"""
现代化组件库 - 美观的自定义组件
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Any, Dict
from .theme_manager import theme_manager


class ModernButton(tk.Button):
    """现代化按钮组件"""
    
    def __init__(self, parent, text: str = "", command: Optional[Callable] = None,
                 style: str = "primary", icon: str = "", **kwargs):
        """
        初始化现代化按钮
        
        Args:
            parent: 父组件
            text: 按钮文本
            command: 点击回调
            style: 按钮样式 (primary, secondary, success, danger)
            icon: 图标文本（emoji）
            **kwargs: 其他参数
        """
        self.style_type = style
        self.icon = icon
        self.original_text = text
        
        # 获取主题颜色
        colors = theme_manager.get_theme_colors()
        
        # 根据样式设置颜色
        style_config = self._get_style_config(colors, style)

        # 组合图标和文本
        display_text = f"{icon} {text}" if icon else text

        # 提取tkinter Button支持的参数
        button_config = {
            'bg': style_config['bg'],
            'fg': style_config['fg'],
            'padx': style_config['padx'],
            'pady': style_config['pady']
        }

        super().__init__(
            parent,
            text=display_text,
            command=command,
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            font=('', 10, 'bold' if style == 'primary' else 'normal'),
            **button_config,
            **kwargs
        )

        # 绑定悬停效果
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        self.bind('<Button-1>', self._on_click)
        self.bind('<ButtonRelease-1>', self._on_release)

        # 保存原始颜色
        self.original_bg = style_config['bg']
        self.hover_bg = style_config.get('hover_bg', self.original_bg)
        self.active_bg = style_config.get('active_bg', self.original_bg)
    
    def _get_style_config(self, colors: Dict[str, str], style: str) -> Dict[str, Any]:
        """获取样式配置"""
        configs = {
            'primary': {
                'bg': colors['primary'],
                'fg': colors['on_primary'],
                'hover_bg': colors['primary_dark'],
                'active_bg': colors['primary_dark'],
                'padx': 20,
                'pady': 8
            },
            'secondary': {
                'bg': colors['surface'],
                'fg': colors['on_surface'],
                'hover_bg': colors['surface_variant'],
                'active_bg': colors['surface_variant'],
                'padx': 16,
                'pady': 6
            },
            'success': {
                'bg': colors['success'],
                'fg': 'white',
                'hover_bg': '#059669',
                'active_bg': '#047857',
                'padx': 16,
                'pady': 6
            },
            'danger': {
                'bg': colors['danger'],
                'fg': 'white',
                'hover_bg': '#dc2626',
                'active_bg': '#b91c1c',
                'padx': 16,
                'pady': 6
            }
        }
        return configs.get(style, configs['primary'])
    
    def _on_enter(self, event):
        """鼠标进入事件"""
        self.configure(bg=self.hover_bg)
    
    def _on_leave(self, event):
        """鼠标离开事件"""
        self.configure(bg=self.original_bg)
    
    def _on_click(self, event):
        """鼠标按下事件"""
        self.configure(bg=self.active_bg)
    
    def _on_release(self, event):
        """鼠标释放事件"""
        self.configure(bg=self.hover_bg)


class ModernCard(tk.Frame):
    """现代化卡片组件"""
    
    def __init__(self, parent, title: str = "", **kwargs):
        """
        初始化现代化卡片
        
        Args:
            parent: 父组件
            title: 卡片标题
            **kwargs: 其他参数
        """
        colors = theme_manager.get_theme_colors()
        
        super().__init__(
            parent,
            bg=colors['surface'],
            relief='flat',
            bd=1,
            highlightbackground=colors['border'],
            highlightthickness=1,
            **kwargs
        )
        
        # 创建标题
        if title:
            self.title_label = tk.Label(
                self,
                text=title,
                bg=colors['surface'],
                fg=colors['primary'],
                font=('', 12, 'bold'),
                anchor='w'
            )
            self.title_label.pack(fill=tk.X, padx=15, pady=(15, 5))
        
        # 创建内容区域
        self.content_frame = tk.Frame(
            self,
            bg=colors['surface']
        )
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
    
    def add_content(self, widget):
        """添加内容到卡片"""
        widget.pack(in_=self.content_frame, fill=tk.X, pady=2)


class ModernEntry(tk.Frame):
    """现代化输入框组件"""
    
    def __init__(self, parent, label: str = "", placeholder: str = "", **kwargs):
        """
        初始化现代化输入框
        
        Args:
            parent: 父组件
            label: 标签文本
            placeholder: 占位符文本
            **kwargs: 其他参数
        """
        colors = theme_manager.get_theme_colors()
        
        super().__init__(parent, bg=colors['background'])
        
        # 创建标签
        if label:
            self.label = tk.Label(
                self,
                text=label,
                bg=colors['background'],
                fg=colors['on_surface'],
                font=('', 10),
                anchor='w'
            )
            self.label.pack(fill=tk.X, pady=(0, 5))
        
        # 创建输入框容器
        self.entry_frame = tk.Frame(
            self,
            bg=colors['surface'],
            relief='flat',
            bd=1,
            highlightbackground=colors['border'],
            highlightthickness=1
        )
        self.entry_frame.pack(fill=tk.X)
        
        # 创建输入框
        self.entry = tk.Entry(
            self.entry_frame,
            bg=colors['surface'],
            fg=colors['on_surface'],
            relief='flat',
            bd=0,
            font=('', 10),
            insertbackground=colors['primary'],
            selectbackground=colors['primary_light'],
            selectforeground=colors['on_primary'],
            **kwargs
        )
        self.entry.pack(fill=tk.X, padx=10, pady=8)
        
        # 占位符功能
        self.placeholder = placeholder
        self.placeholder_active = False
        if placeholder:
            self._show_placeholder()
        
        # 绑定焦点事件
        self.entry.bind('<FocusIn>', self._on_focus_in)
        self.entry.bind('<FocusOut>', self._on_focus_out)
        self.entry_frame.bind('<Button-1>', lambda e: self.entry.focus())
    
    def _show_placeholder(self):
        """显示占位符"""
        if not self.entry.get():
            self.placeholder_active = True
            colors = theme_manager.get_theme_colors()
            self.entry.configure(fg=colors['secondary'])
            self.entry.insert(0, self.placeholder)
    
    def _hide_placeholder(self):
        """隐藏占位符"""
        if self.placeholder_active:
            self.placeholder_active = False
            colors = theme_manager.get_theme_colors()
            self.entry.configure(fg=colors['on_surface'])
            self.entry.delete(0, tk.END)
    
    def _on_focus_in(self, event):
        """获得焦点"""
        colors = theme_manager.get_theme_colors()
        self.entry_frame.configure(highlightbackground=colors['primary'])
        self._hide_placeholder()
    
    def _on_focus_out(self, event):
        """失去焦点"""
        colors = theme_manager.get_theme_colors()
        self.entry_frame.configure(highlightbackground=colors['border'])
        if not self.entry.get():
            self._show_placeholder()
    
    def get(self):
        """获取输入值"""
        if self.placeholder_active:
            return ""
        return self.entry.get()
    
    def set(self, value):
        """设置输入值"""
        self._hide_placeholder()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)


class ModernProgressBar(tk.Frame):
    """现代化进度条组件"""
    
    def __init__(self, parent, width: int = 200, height: int = 6, **kwargs):
        """
        初始化现代化进度条
        
        Args:
            parent: 父组件
            width: 宽度
            height: 高度
            **kwargs: 其他参数
        """
        colors = theme_manager.get_theme_colors()
        
        super().__init__(parent, bg=colors['background'], **kwargs)
        
        self.width = width
        self.height = height
        self.progress = 0.0
        
        # 创建画布
        self.canvas = tk.Canvas(
            self,
            width=width,
            height=height,
            bg=colors['surface_variant'],
            highlightthickness=0,
            relief='flat'
        )
        self.canvas.pack()
        
        # 创建进度条背景
        self.bg_rect = self.canvas.create_rectangle(
            0, 0, width, height,
            fill=colors['surface_variant'],
            outline=""
        )
        
        # 创建进度条
        self.progress_rect = self.canvas.create_rectangle(
            0, 0, 0, height,
            fill=colors['primary'],
            outline=""
        )
    
    def set_progress(self, value: float):
        """
        设置进度值
        
        Args:
            value: 进度值 (0.0 - 1.0)
        """
        self.progress = max(0.0, min(1.0, value))
        progress_width = self.width * self.progress
        
        self.canvas.coords(
            self.progress_rect,
            0, 0, progress_width, self.height
        )


class ModernTooltip:
    """现代化工具提示"""
    
    def __init__(self, widget, text: str):
        """
        初始化工具提示
        
        Args:
            widget: 目标组件
            text: 提示文本
        """
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        
        # 绑定事件
        self.widget.bind('<Enter>', self._on_enter)
        self.widget.bind('<Leave>', self._on_leave)
        self.widget.bind('<Motion>', self._on_motion)
    
    def _on_enter(self, event):
        """鼠标进入"""
        self._show_tooltip(event)
    
    def _on_leave(self, event):
        """鼠标离开"""
        self._hide_tooltip()
    
    def _on_motion(self, event):
        """鼠标移动"""
        if self.tooltip_window:
            self._update_position(event)
    
    def _show_tooltip(self, event):
        """显示工具提示"""
        if self.tooltip_window:
            return
        
        colors = theme_manager.get_theme_colors()
        
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.configure(bg=colors['surface'])
        
        label = tk.Label(
            self.tooltip_window,
            text=self.text,
            bg=colors['surface'],
            fg=colors['on_surface'],
            font=('', 9),
            relief='flat',
            bd=1,
            highlightbackground=colors['border'],
            highlightthickness=1,
            padx=8,
            pady=4
        )
        label.pack()
        
        self._update_position(event)
    
    def _hide_tooltip(self):
        """隐藏工具提示"""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None
    
    def _update_position(self, event):
        """更新位置"""
        if self.tooltip_window:
            x = event.x_root + 10
            y = event.y_root + 10
            self.tooltip_window.geometry(f"+{x}+{y}")
