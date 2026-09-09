# Foreign Legal PPT Skill

面向涉外法务和跨境业务团队的 Codex Skill。它把境外法律检索、来源追溯、管理层表达、个人视觉偏好和 PPT 交付检查放进同一套工作流程。

## 适用场景

- 境外投资审查、制裁、出口管制、数据合规及跨境交易指南；
- 面向中国管理层的境外法规、案例和执法趋势汇报；
- 需要核验现行法、保留来源台账并控制页面质量的专业演示；
- 希望沉淀个人 PPT 风格和质量标准的用户。

## 主要特点

- 检索前建立议题地图，减少只覆盖容易搜索内容造成的片面性；
- 优先核验官方一手法源，记录法律状态、日期、定位和适用限制；
- 区分法律规则、事实、分析、风险判断和建议；
- 将研究结论翻译为管理层关心的适用性、商业影响和下一步动作；
- 支持通过参考 PPT 和样张建立个人 `ppt-profile.md`；
- 要求渲染后逐页检查内容、引用、术语和视觉问题；
- 根据当前 Agent 的检索、文件、视觉和渲染能力调整流程。

## 安装

把仓库地址交给支持 Skills 的 Agent：

> 请安装这个 Skill，并运行“设置我的 PPT 标准”。未经我同意，不要上传我的模板、客户资料或内部文件。

也可以将本仓库复制到个人 Skills 目录。不同产品的目录和安装方式可能不同，应以当前产品的官方说明为准。

详细说明见 [INSTALL.md](INSTALL.md)。

## 第一次配置

> 使用 `$foreign-legal-ppt` 设置我的 PPT 标准。请一次只问少量问题，并通过参考 PPT 或样张帮助我选择。

个人配置应保存在用户自己的工作目录，不应写回公共 Skill 仓库。

## 日常使用

> 使用 `$foreign-legal-ppt`，按照我的 PPT 标准制作一份面向中国管理层的 CFIUS 交易指南。检索并核验截至今天的官方法源；先形成议题地图和来源台账，存在重大范围问题时再问我。

## 能力与责任边界

本 Skill 定义研究、表达和质检标准，不自带法律数据库、网页检索、PPT 生成或渲染能力。实际结果取决于当前 Agent、模型、工具权限、用户材料和专业复核。

它不构成法律意见，也不能替代负责律师对法源、事实、分析和披露方式的最终判断。请勿向未经授权的服务上传客户秘密、个人信息、特权材料或其他受限数据。

## Repository layout

```text
foreign-legal-ppt-skill/
├── SKILL.md
├── INSTALL.md
├── agents/openai.yaml
├── assets/profile-template.md
└── references/
    ├── legal-research.md
    ├── management-deck.md
    ├── profile-setup.md
    ├── quality-gates.md
    └── runtime-adaptation.md
```

## Contributing

欢迎用公开、虚构或彻底脱敏的案例提交问题和改进。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

[MIT](LICENSE)

