# -*- coding: utf-8 -*-
"""
数学函数可视化工具 - 主程序入口
"""

import tkinter as tk
from gui.main_window import MathVisualizerApp


def main():
    """主函数"""
    # 创建根窗口
    root = tk.Tk()
    
    # 创建应用程序实例
    app = MathVisualizerApp(root)
    
    # 设置应用程序样式
    root.tk_setPalette(
        background='#f0f0f0', 
        foreground='#333333', 
        activeBackground='#4a90d9', 
        activeForeground='white'
    )
    
    # 启动主循环
    root.mainloop()


if __name__ == "__main__":
    main()
