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
    try:
        app = MathVisualizerApp()
        app.run()
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
