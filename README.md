# OK Duet Night Abyss - 优化版本

基于 [BnanZ0/ok-duet-night-abyss](https://github.com/BnanZ0/ok-duet-night-abyss) 的优化修改版本，专注于自动化游戏操作和效率提升。

## 🚀 新增功能

### 多次技能释放
- **增强的技能系统**：新增多次技能释放功能，提升战斗效率
- **智能连招**：支持自定义技能连招组合，一键释放
- **技能循环**：可配置自动技能循环，最大化输出伤害
- **战斗策略**：更灵活的战斗AI，支持不同场景的技能释放策略

## 📋 原有功能

- **自动化探索**：自动探索地图，收集资源
- **战斗辅助**：智能战斗检测和自动操作
- **任务管理**：自动完成日常任务和委托
- **装备管理**：自动装备强化和遗器管理
- **钓鱼系统**：自动化钓鱼功能
- **移动控制**：智能路径规划和移动

## 🛠️ 安装使用

### 环境要求
- Python 3.8+
- Windows系统

### 安装步骤
1. 克隆仓库
```bash
git clone https://github.com/GemVent/ok-duet-night-abyss.git
cd ok-duet-night-abyss
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行程序
```bash
python main.py
```

## ⚙️ 配置说明

所有配置文件位于 `configs/` 目录下：
- `AutoSkill.json` - 技能释放配置
- `AutoCombatTask.json` - 战斗任务配置
- `Basic Options.json` - 基础选项配置
- 其他特定功能配置文件

### 新增技能配置
在 `configs/AutoSkill.json` 中可以配置：
- 技能释放顺序
- 技能间隔时间
- 连招组合
- 条件触发设置

## 📁 项目结构

```
ok-duet-night-abyss/
├── main.py              # 主程序入口
├── main_debug.py        # 调试模式入口
├── requirements.txt     # 依赖包列表
├── assets/              # 资源文件
├── configs/             # 配置文件
├── icons/               # 图标文件
├── src/                 # 源代码目录
│   ├── char/           # 角色相关
│   ├── combat/         # 战斗系统
│   ├── tasks/          # 任务模块
│   └── ...             # 其他模块
└── README.md           # 项目说明文档
```

## 🔧 主要优化

### 技能系统优化
- 多次技能释放机制
- 智能技能冷却管理
- 动态技能优先级调整
- 战斗状态感知技能释放

### 性能优化
- 内存使用优化
- 响应速度提升
- 稳定性增强
- 错误处理改进

### 用户体验
- 更直观的配置界面
- 详细的日志输出
- 更好的错误提示
- 操作反馈优化

## 🎮 使用说明

1. **启动程序**：运行 `main.py` 启动主程序
2. **配置设置**：根据需要修改 `configs/` 目录下的配置文件
3. **开始使用**：在界面中选择需要的功能并开始

### 注意事项
- 首次使用前请仔细阅读配置说明
- 建议在测试环境中验证配置
- 使用过程中请注意游戏安全

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 📄 许可证

本项目基于原项目的许可证，请参考相关许可证条款。

## 🙏 致谢

感谢 [BnanZ0/ok-duet-night-abyss](https://github.com/BnanZ0/ok-duet-night-abyss) 项目提供的优秀基础。

---

⚠️ **免责声明**：本工具仅供学习和研究使用，请遵守相关游戏的使用条款和规定。