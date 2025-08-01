# 异步类脑工具链 易思 (ANP-Flow)

## 项目简介

易思(ANP-Flow)是一个基于Web的异步类脑芯片设计工具链，提供从设计空间探索到系统级仿真的完整解决方案。该工具链集成了强化学习、Akka Actor并发框架、Chisel硬件描述语言和LLVM编译优化技术，为异步类脑芯片的设计和验证提供全面的支持。



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

## 使用方法

### 1. 设计空间探索
1. 点击"设计空间探索"卡片
2. 选择相关参数（param1, param2, param3）
3. 点击"开始"按钮
4. 等待强化学习算法完成优化
5. 查看最优设计方案

### 2. 系统级建模仿真
1. 点击"系统级建模仿真"卡片
2. 选择模型级别和调试级别
3. 选择云模型路径
4. 设置保存路径
5. 启动仿真并实时监控输出

### 3. 异步电路设计
1. 点击"异步电路设计"卡片
2. 跳转到GitHub仓库获取设计库
3. 使用Chisel框架进行开发
4. 下载相关设计模板

### 4. 异步类脑编译器
1. 点击"异步类脑编译器"卡片
2. 上传或选择目标文件
3. 配置编译参数
4. 执行编译优化
5. 获取资源配置方案

## 故障排除

### 常见问题

1. **端口占用**
```bash
# 检查端口占用
lsof -i :8020
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
