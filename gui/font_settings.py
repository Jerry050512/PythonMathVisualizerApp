# -*- coding: utf-8 -*-
"""
字体设置窗口模块
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable


class FontSettingsWindow:
    """字体设置窗口类"""
    
    def __init__(self, parent, font_manager, callback: Callable):
        """
        初始化字体设置窗口
        
        Args:
            parent: 父窗口
            font_manager: 字体管理器实例
            callback: 字体更改后的回调函数
        """
        self.parent = parent
        self.font_manager = font_manager
        self.callback = callback
        
        # 创建字体设置窗口
        self.create_font_window()
    
    def create_font_window(self):
        """创建字体设置窗口"""
        # 创建字体设置窗口
        self.font_window = tk.Toplevel(self.parent)
        self.font_window.title("字体设置")
        self.font_window.geometry("500x400")
        self.font_window.resizable(False, False)
        
        # 设置窗口为模态窗口
        self.font_window.transient(self.parent)
        self.font_window.grab_set()
        
        # 创建各个区域
        self.create_current_font_area()
        self.create_preview_area()
        self.create_font_list_area()
        self.create_button_area()
        self.create_info_area()
    
    def create_current_font_area(self):
        """创建当前字体信息显示区域"""
        current_frame = ttk.LabelFrame(self.font_window, text="当前字体", padding=10)
        current_frame.pack(fill=tk.X, padx=10, pady=5)
        
        current_font = self.font_manager.get_current_font()
        ttk.Label(
            current_frame, 
            text=f"当前使用字体: {current_font}", 
            font=('', 10)
        ).pack(anchor=tk.W)
    
    def create_preview_area(self):
        """创建字体预览区域"""
        preview_frame = ttk.LabelFrame(self.font_window, text="字体预览", padding=10)
        preview_frame.pack(fill=tk.X, padx=10, pady=5)
        
        current_font = self.font_manager.get_current_font()
        self.preview_label = ttk.Label(
            preview_frame, 
            text="中文测试: 数学函数可视化工具\nEnglish Test: Mathematical Functions", 
            font=(current_font, 12), 
            justify=tk.CENTER
        )
        self.preview_label.pack(expand=True)
    
    def create_font_list_area(self):
        """创建可用字体列表区域"""
        fonts_frame = ttk.LabelFrame(self.font_window, text="可用中文字体", padding=10)
        fonts_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 创建字体列表框和滚动条
        list_frame = ttk.Frame(fonts_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.font_listbox = tk.Listbox(list_frame, height=8, font=('', 9))
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.font_listbox.yview)
        self.font_listbox.configure(yscrollcommand=scrollbar.set)
        
        # 添加经过验证的中文字体到列表
        available_fonts = self.font_manager.get_available_fonts()
        for font in available_fonts:
            self.font_listbox.insert(tk.END, font)
        
        # 选中当前字体
        current_font = self.font_manager.get_current_font()
        try:
            current_index = available_fonts.index(current_font)
            self.font_listbox.selection_set(current_index)
            self.font_listbox.see(current_index)
        except ValueError:
            pass
        
        # 绑定选择事件进行实时预览
        self.font_listbox.bind('<<ListboxSelect>>', self.on_font_select)
        
        # 布局字体列表框和滚动条
        self.font_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_button_area(self):
        """创建按钮区域"""
        button_frame = ttk.Frame(self.font_window)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # 创建操作按钮
        ttk.Button(
            button_frame, 
            text="应用字体", 
            command=self.apply_font, 
            style="Accent.TButton"
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="重置默认", 
            command=self.reset_font
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame, 
            text="取消", 
            command=self.font_window.destroy
        ).pack(side=tk.RIGHT, padx=5)
    
    def create_info_area(self):
        """创建使用说明区域"""
        info_frame = ttk.Frame(self.font_window)
        info_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        info_text = "提示: 选择字体后可在上方预览效果，确认无误后点击'应用字体'"
        ttk.Label(
            info_frame, 
            text=info_text, 
            font=('', 8), 
            foreground="gray"
        ).pack(anchor=tk.W)
    
    def on_font_select(self, event):
        """字体选择事件处理"""
        selection = self.font_listbox.curselection()
        if selection:
            selected_font = self.font_listbox.get(selection[0])
            try:
                self.preview_label.config(font=(selected_font, 12))
            except:
                self.preview_label.config(font=('TkDefaultFont', 12))
    
    def apply_font(self):
        """应用选中的字体"""
        selection = self.font_listbox.curselection()
        if selection:
            selected_font = self.font_listbox.get(selection[0])
            
            # 更新字体设置
            success = self.font_manager.set_font(selected_font)
            
            if success:
                # 调用回调函数重新绘制图形
                self.callback()
                
                messagebox.showinfo("字体设置", f"已应用字体: {selected_font}")
                self.font_window.destroy()
            else:
                messagebox.showerror("字体设置", f"应用字体失败: {selected_font}")
        else:
            messagebox.showwarning("字体设置", "请先选择一个字体")
    
    def reset_font(self):
        """重置为默认字体"""
        self.font_manager.reset_to_default()
        
        # 调用回调函数重新绘制图形
        self.callback()
        
        default_font = self.font_manager.get_current_font()
        messagebox.showinfo("字体设置", f"已重置为默认字体: {default_font}")
        self.font_window.destroy()
