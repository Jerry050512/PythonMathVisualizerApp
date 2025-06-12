# -*- coding: utf-8 -*-
"""
数学函数可视化工具 - 主程序入口
"""

import sys
import os
import ctypes # Added
import platform # Added

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from gui.main_window import MathVisualizerApp
except ImportError as e:
    print(f"导入模块失败: {e}")
    sys.exit(1)

def set_dpi_awareness():
    if platform.system() == "Windows":
        try:
            # Try Per Monitor V2 (Windows 10 Creators Update+)
            ctypes.windll.shcore.SetProcessDpiAwarenessContext(-4)
            print("ℹ️ DPI Awareness set to Per Monitor V2.")
            return
        except (AttributeError, OSError):
            pass # Fall through to next try
        try:
            # Try Per Monitor (Windows 8.1+)
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
            print("ℹ️ DPI Awareness set to Per Monitor (via shcore).")
            return
        except (AttributeError, OSError):
            pass # Fall through to next try
        try:
            # Try System DPI Aware (Windows Vista+)
            ctypes.windll.user32.SetProcessDPIAware()
            print("ℹ️ DPI Awareness set to System Aware (via user32).")
        except (AttributeError, OSError):
            print("⚠️ Could not set DPI awareness.")


def main():
    """主函数"""
    set_dpi_awareness() # Added call
    try:
        app = MathVisualizerApp()
        app.run()
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
