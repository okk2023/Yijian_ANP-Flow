# 异步类脑工具链:易思 (ANP-Flow)

## 项目简介

易思(ANP-Flow)是清华大学集成电路学院异步电路课题组自主研发的一个基于Web的异步类脑芯片设计工具链，提供从设计空间探索到系统级仿真的完整解决方案。该工具链集成了强化学习、Akka Actor并发框架、Chisel硬件描述语言和LLVM编译优化技术，为异步类脑芯片的设计和验证提供全面的支持。



## 功能特性

### 🧠 设计空间探索
- 基于强化学习的设计空间探索框架
- 自动获得给定条件下的最优算法-硬件设计方案
- 支持多参数优化和约束条件设置

### 🔬 系统级建模仿真
- 基于Akka Actor并发框架的系统级仿真器
- 异步类脑芯片预期延时性能分析
- 功耗和面积评估
- 实时仿真输出监控

### ⚡ 异步电路设计
- 基于Chisel框架的异步电路设计
- 快速原型开发和验证
- 开源设计库支持
- 与GitHub集成

## 安装说明

### 环境要求
- Python 3.7+
- Flask 2.0+
- 支持WebGL的现代浏览器

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd anchain
```

2. **安装依赖**
```bash
pip install flask
pip install subprocess32  # 如果需要
```

3. **配置环境**
```bash
# 确保scripts目录有执行权限
chmod +x processes/*.sh
```

4. **启动应用**
```bash
python app.py
```

5. **访问应用**
打开浏览器访问 `http://localhost:5000`

## 故障排除

### 常见问题

1. **端口占用**
```bash
# 检查端口占用
lsof -i :5000
# 杀死占用进程
kill -9 <PID>
```

2. **权限问题**
```bash
# 确保脚本有执行权限
chmod +x processes/*.sh
```

3. **依赖缺失**
```bash
# 安装缺失的Python包
pip install -r requirements.txt
```

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 更新日志

### v1.0.0 (2024-01-XX)
- 初始版本发布
- 实现四大核心功能模块
- 集成Web界面
- 支持实时仿真监控

---

**注意**: 本项目仍在积极开发中，功能可能会有所变化。如有问题或建议，请提交Issue。
