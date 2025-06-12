# -*- coding: utf-8 -*-
"""
数学函数可视化工具 - 主程序入口
"""

import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from gui.main_window import MathVisualizerApp
except ImportError as e:
    print(f"导入模块失败: {e}")
    sys.exit(1)



def main():
    """主函数"""
<<<<<<< HEAD
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
=======
    try:
        app = MathVisualizerApp()
        app.run()
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        import traceback
        traceback.print_exc()
>>>>>>> b8fa0e1d66aa93543928312044add878d77cfd6c


if __name__ == "__main__":
    main()
