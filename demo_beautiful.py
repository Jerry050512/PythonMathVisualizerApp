#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学函数可视化工具 - 美化版演示
展示现代化界面设计和主题系统
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MathVisualizerApp
from gui.theme_manager import theme_manager
from config.settings import THEMES


class BeautifulMathVisualizer:
    """美化版数学函数可视化工具"""
    
    def __init__(self):
        """初始化美化版应用"""
        self.root = tk.Tk()
        self.setup_splash_screen()
        
    def setup_splash_screen(self):
        """设置启动画面"""
        # 隐藏主窗口
        self.root.withdraw()
        
        # 创建启动画面
        splash = tk.Toplevel()
        splash.title("数学函数可视化工具")
        splash.geometry("500x350")
        splash.resizable(False, False)
        splash.configure(bg='#2563eb')
        
        # 居中显示
        splash.update_idletasks()
        x = (splash.winfo_screenwidth() // 2) - (500 // 2)
        y = (splash.winfo_screenheight() // 2) - (350 // 2)
        splash.geometry(f'500x350+{x}+{y}')
        
        # 移除窗口装饰
        splash.overrideredirect(True)
        
        # 创建启动画面内容
        self.create_splash_content(splash)
        
        # 3秒后关闭启动画面并显示主窗口
        splash.after(3000, lambda: self.show_main_window(splash))
        
    def create_splash_content(self, splash):
        """创建启动画面内容"""
        # 主容器
        main_frame = tk.Frame(splash, bg='#2563eb')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # 标题
        title_label = tk.Label(
            main_frame,
            text="📊 数学函数可视化工具",
            font=('', 24, 'bold'),
            fg='white',
            bg='#2563eb'
        )
        title_label.pack(pady=(40, 20))
        
        # 副标题
        subtitle_label = tk.Label(
            main_frame,
            text="Modern & Beautiful Interface",
            font=('', 14),
            fg='#93c5fd',
            bg='#2563eb'
        )
        subtitle_label.pack(pady=(0, 30))
        
        # 功能特性
        features = [
            "🎨 现代化界面设计",
            "🌈 多主题支持",
            "📈 实时函数绘制",
            "🔧 智能参数调节",
            "💾 图像保存功能"
        ]
        
        for feature in features:
            feature_label = tk.Label(
                main_frame,
                text=feature,
                font=('', 12),
                fg='white',
                bg='#2563eb',
                anchor='w'
            )
            feature_label.pack(pady=3, fill=tk.X)
        
        # 加载进度
        progress_frame = tk.Frame(main_frame, bg='#2563eb')
        progress_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(30, 0))
        
        tk.Label(
            progress_frame,
            text="正在加载...",
            font=('', 10),
            fg='#93c5fd',
            bg='#2563eb'
        ).pack()
        
        # 简单的进度条
        progress_bg = tk.Frame(progress_frame, bg='#1d4ed8', height=4)
        progress_bg.pack(fill=tk.X, pady=(10, 0))
        
        progress_bar = tk.Frame(progress_bg, bg='#60a5fa', height=4)
        progress_bar.pack(side=tk.LEFT, fill=tk.Y)
        
        # 动画进度条
        self.animate_progress(progress_bar, 0)
        
    def animate_progress(self, progress_bar, width):
        """动画进度条"""
        if width <= 440:
            progress_bar.configure(width=width)
            progress_bar.after(20, lambda: self.animate_progress(progress_bar, width + 8))
    
    def show_main_window(self, splash):
        """显示主窗口"""
        splash.destroy()
        self.root.deiconify()
        
        # 创建主应用
        self.app = MathVisualizerApp(self.root)
        
        # 显示主题选择对话框
        self.show_theme_selector()
        
    def show_theme_selector(self):
        """显示主题选择对话框"""
        dialog = tk.Toplevel(self.root)
        dialog.title("选择界面主题")
        dialog.geometry("400x300")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 居中显示
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (300 // 2)
        dialog.geometry(f'400x300+{x}+{y}')
        
        colors = theme_manager.get_theme_colors()
        dialog.configure(bg=colors['background'])
        
        # 标题
        title_label = tk.Label(
            dialog,
            text="🎨 选择您喜欢的主题",
            font=('', 16, 'bold'),
            fg=colors['on_surface'],
            bg=colors['background']
        )
        title_label.pack(pady=20)
        
        # 主题选项
        theme_frame = tk.Frame(dialog, bg=colors['background'])
        theme_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        self.selected_theme = tk.StringVar(value=theme_manager.current_theme)
        
        for theme_id, theme_config in THEMES.items():
            theme_button = tk.Radiobutton(
                theme_frame,
                text=f"{theme_config['name']} - {theme_id}",
                variable=self.selected_theme,
                value=theme_id,
                font=('', 12),
                fg=colors['on_surface'],
                bg=colors['background'],
                selectcolor=colors['primary'],
                activebackground=colors['surface_variant'],
                command=lambda t=theme_id: self.preview_theme(t)
            )
            theme_button.pack(anchor=tk.W, pady=5)
        
        # 按钮区域
        button_frame = tk.Frame(dialog, bg=colors['background'])
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=30, pady=20)
        
        tk.Button(
            button_frame,
            text="应用主题",
            command=lambda: self.apply_theme_and_close(dialog),
            bg=colors['primary'],
            fg=colors['on_primary'],
            font=('', 11, 'bold'),
            relief='flat',
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(side=tk.RIGHT, padx=(10, 0))
        
        tk.Button(
            button_frame,
            text="使用默认",
            command=dialog.destroy,
            bg=colors['surface'],
            fg=colors['on_surface'],
            font=('', 11),
            relief='flat',
            padx=20,
            pady=8,
            cursor='hand2'
        ).pack(side=tk.RIGHT)
    
    def preview_theme(self, theme_id):
        """预览主题"""
        theme_manager.apply_theme(theme_id)
        
    def apply_theme_and_close(self, dialog):
        """应用主题并关闭对话框"""
        selected = self.selected_theme.get()
        theme_manager.apply_theme(selected)
        dialog.destroy()
        
        # 显示成功消息
        messagebox.showinfo(
            "主题应用成功", 
            f"已应用 {THEMES[selected]['name']} 主题！\n\n享受您的数学函数可视化之旅！"
        )
    
    def run(self):
        """运行应用"""
        self.root.mainloop()


def main():
    """主函数"""
    print("🚀 启动美化版数学函数可视化工具...")
    print("✨ 现代化界面设计")
    print("🎨 多主题支持")
    print("📊 实时函数绘制")
    print("-" * 50)
    
    try:
        app = BeautifulMathVisualizer()
        app.run()
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        messagebox.showerror("启动错误", f"应用启动失败：\n{e}")


if __name__ == "__main__":
    main()
