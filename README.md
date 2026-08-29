# Admin UI Skills

一套用于 **后台管理系统 AI 设计与开发** 的 Codex Skills。

目标是让 Codex 能够基于 PRD、Figma 和现有代码，完成从需求分析、后台页面设计、设计规范提取、前端实现到最终 Review 的完整工作流。

---

# 1. 目标

这套 Skills 主要解决以下问题：

* 读取 PRD，自动拆解后台模块和页面
* 将 PRD 转换为结构化 `ADMIN_SPEC.md`
* 根据已有 Figma 提取项目设计规范并生成 `DESIGN.md`
* 根据 PRD / ADMIN_SPEC / DESIGN.md 创建后台 Figma 设计稿
* 根据 Figma 实现 React / Vue 后台页面
* Review PRD、设计稿、Design System 和代码之间的一致性
* 通过统一 Workflow 自动判断当前应该执行哪个 Skill

最终形成完整链路：

```text
PRD
 ↓
ADMIN_SPEC.md
 ↓
DESIGN.md
 ↓
Figma
 ↓
Frontend Code
 ↓
Review
```

---

# 2. 核心设计原则

整个工作流遵循一个原则：

> 不让 AI 每次从头重新理解产品、设计和代码。

不同 Artifact 分别承担不同职责。

```text
PRD.md
= 产品需求真源

ADMIN_SPEC.md
= 后台页面与交互真源

DESIGN.md
= Design System 真源

Figma
= 页面视觉真源

Code
= 最终实现
```

这样可以避免随着开发推进出现：

* 页面结构越来越不一致
* 同一个功能有时使用 Drawer，有时使用 Modal
* 表格字段遗漏
* 筛选条件遗漏
* Design Token 被不断 hardcode
* Figma 与代码越来越偏
* Codex 每次重新创造组件
* 不同页面使用不同设计语言

---

# 3. Skills

当前包含 6 个核心 Skill。

```text
.agents/
└── skills/
    ├── admin-workflow/
    │   └── SKILL.md
    │
    ├── prd-to-admin-spec/
    │   └── SKILL.md
    │
    ├── prd-to-admin-design/
    │   └── SKILL.md
    │
    ├── figma-to-design-md/
    │   └── SKILL.md
    │
    ├── figma-to-admin-page/
    │   └── SKILL.md
    │
    └── admin-ui-review/
        └── SKILL.md
```

---

# 4. Skill 职责

## 4.1 admin-workflow

工作流编排 Skill。

负责判断当前任务应该使用哪个 Skill，以及执行顺序。

它不直接承担大量设计或开发工作。

典型任务：

```text
读取 PRD，把用户管理模块设计并开发出来。
```

可能自动拆解为：

```text
prd-to-admin-spec
        ↓
prd-to-admin-design
        ↓
figma-to-admin-page
        ↓
admin-ui-review
```

核心职责：

* Workflow Routing
* Artifact Detection
* Dependency Analysis
* Execution Sequencing
* Scope Control

---

## 4.2 prd-to-admin-spec

负责：

```text
PRD
 ↓
ADMIN_SPEC.md
```

将产品语言转换成后台 UI 可以直接消费的页面规格。

主要分析：

* 后台模块
* 菜单
* 页面
* Route
* Page Type
* Filters
* Search
* Table Columns
* Row Actions
* Bulk Actions
* Detail Sections
* Dialog
* Drawer
* Form
* Tabs
* Permissions
* Status
* Loading
* Empty
* Error
* Page Relationship

这个 Skill 不负责：

* Figma 设计
* Design System
* React / Vue 开发

---

## 4.3 prd-to-admin-design

负责：

```text
ADMIN_SPEC.md
+
DESIGN.md
+
Existing Figma
 ↓
Figma Admin UI
```

这是后台 UI/UX Designer Skill。

主要负责：

* 根据页面规格创建后台页面
* 使用已有 Design System
* 复用已有 Figma Components
* 保持不同模块之间的一致性
* 设计 Table、Filter、Form、Detail、Dialog、Drawer
* 处理后台常见操作状态

其中：

```text
ADMIN_SPEC.md
决定设计什么

DESIGN.md
决定怎么设计

Figma
决定现有设计系统具体如何表达
```

---

## 4.4 figma-to-design-md

负责：

```text
Figma
 ↓
DESIGN.md
```

将 Figma 中的设计语言转换成 Codex 和开发者可以直接使用的 Design System 文档。

不仅仅提取：

* Color
* Font
* Radius

还会分析：

* Layout
* Spacing
* Component
* Table Pattern
* Form Pattern
* Detail Pattern
* List Pattern
* Dashboard Pattern
* Interaction
* State
* Do / Don't

最终目标：

即使 Codex 不重新读取完整 Figma，也可以通过 `DESIGN.md` 创建风格一致的新页面。

---

## 4.5 figma-to-admin-page

负责：

```text
Figma
+
DESIGN.md
+
ADMIN_SPEC.md
+
Existing Codebase
 ↓
Frontend Page
```

这是前端实现 Skill。

主要负责：

* 理解 Figma 页面结构
* 分析现有代码
* 搜索已有 Components
* 建立 Figma → Code Component Mapping
* 复用已有 Design System
* 实现 React / Vue 页面
* 保证合理的页面结构
* 保证 Figma Fidelity
* 保证工程一致性

优先使用：

```text
flex
grid
gap
padding
Design Tokens
Existing Components
```

避免：

```text
大量 absolute
大量 magic number
重复组件
重复颜色
重复 spacing
截图式页面实现
```

---

## 4.6 admin-ui-review

负责整个链路的质量检查。

```text
PRD
 ↓
ADMIN_SPEC
 ↓
DESIGN
 ↓
Figma
 ↓
Code
```

检查四个主要维度：

### Requirement Fidelity

需求有没有遗漏。

### Design Fidelity

代码是否符合 Figma。

### Design System Consistency

是否符合 `DESIGN.md`。

### Implementation Quality

代码是否符合项目已有工程规范。

问题分级：

```text
Critical
Major
Minor
Suggestion
```

如果任务要求：

```text
检查并修复
```

则按照：

```text
Critical
 ↓
Major
 ↓
Minor
```

进行修复。

---

# 5. Artifact 关系

推荐后台项目中保留以下文件：

```text
project/
├── AGENTS.md
├── PRD.md
├── ADMIN_SPEC.md
├── DESIGN.md
├── src/
└── ...
```

## PRD.md

产品需求。

主要描述：

* 业务目标
* 用户需求
* 功能
* 规则
* 状态
* 权限
* 操作

不要在 PRD 中维护大量视觉规范。

---

## ADMIN_SPEC.md

后台产品结构。

例如：

```text
用户管理

├── 用户列表
│   ├── Search
│   ├── Filters
│   ├── Table
│   └── Actions
│
└── 用户详情
    ├── 基本信息
    ├── 账户信息
    ├── 财务信息
    └── 操作日志
```

这是设计师和前端之间的重要中间层。

---

## DESIGN.md

项目唯一 Design System 文档。

包括：

```text
Design Principles

Foundations
├── Color
├── Typography
├── Spacing
├── Radius
├── Border
└── Shadow

Layout

Components

Page Patterns

Interaction

States

Do / Don't
```

---

# 6. 推荐工作流

## 场景一：只有 PRD

用户：

```text
读取 PRD.md，整理后台页面。
```

执行：

```text
prd-to-admin-spec
```

结果：

```text
ADMIN_SPEC.md
```

---

## 场景二：已有后台参考 Figma

先执行：

```text
figma-to-design-md
```

得到：

```text
DESIGN.md
```

之后：

```text
prd-to-admin-design
```

生成新的后台设计稿。

---

## 场景三：根据 Figma 开发页面

输入：

```text
Figma
DESIGN.md
ADMIN_SPEC.md
Existing Code
```

执行：

```text
figma-to-admin-page
```

输出真实项目页面。

---

## 场景四：完整后台开发

可以直接要求：

```text
读取 PRD，根据当前 Figma 设计系统完成用户管理模块的设计和前端实现。
```

推荐执行：

```text
prd-to-admin-spec
        ↓
figma-to-design-md
        ↓
prd-to-admin-design
        ↓
figma-to-admin-page
        ↓
admin-ui-review
```

---

# 7. 第一次使用

建议不要一开始就让 Codex 做整个后台。

先建立三个基础 Artifact。

## Step 1

准备：

```text
PRD.md
```

然后执行：

```text
使用 prd-to-admin-spec。

读取 PRD.md，生成 ADMIN_SPEC.md。

当前阶段不要设计 Figma，也不要编写代码。
```

---

## Step 2

如果已有参考 Figma：

```text
使用 figma-to-design-md。

分析当前后台 Figma 的 Design System。

生成项目根目录 DESIGN.md。
```

---

## Step 3

开始设计某个模块：

```text
读取：

ADMIN_SPEC.md
DESIGN.md

根据用户管理模块规格创建对应 Figma 后台设计稿。

保持现有 Design System。
```

---

## Step 4

开始开发：

```text
实现 Figma 中的用户管理模块。

读取：

DESIGN.md
ADMIN_SPEC.md

优先复用项目已有 Components。

不要创建重复 Design System。
```

---

## Step 5

Review：

```text
使用 admin-ui-review。

检查：

PRD
ADMIN_SPEC
DESIGN.md
Figma
当前代码

修复 Critical 和 Major 问题。
```

---

# 8. 推荐日常使用方式

项目初始化完成后，通常不需要手动指定每一个 Skill。

可以直接使用：

```text
admin-workflow
```

例如：

```text
根据 PRD 开始设计订单管理模块。
```

Workflow 应自动判断：

```text
ADMIN_SPEC 是否存在？

DESIGN.md 是否存在？

对应 Figma 页面是否存在？

当前是设计任务还是开发任务？
```

然后选择最短正确路径。

---

# 9. 不要重复生成稳定 Artifact

一个非常重要的规则：

> 已经稳定的 Artifact 不应该每次重新生成。

例如 `DESIGN.md` 已经存在：

不要每开发一个页面都重新分析整个 Figma。

正确方式：

```text
读取 DESIGN.md
+
读取目标 Figma Frame
```

只有当：

* Figma Design System 改变
* 新增大量 Components
* Layout 发生变化
* 用户明确要求更新设计规范

才重新执行：

```text
figma-to-design-md
```

---

# 10. Source of Truth

如果不同来源发生冲突，需要明确优先级。

## 产品需求

```text
用户当前明确指令
        ↓
PRD
        ↓
ADMIN_SPEC
```

## 页面设计

```text
用户当前明确指令
        ↓
ADMIN_SPEC
        ↓
DESIGN.md
        ↓
Existing Figma
```

## 页面实现

```text
用户当前明确指令
        ↓
Target Figma
        ↓
DESIGN.md
        ↓
ADMIN_SPEC
        ↓
Existing Codebase
```

注意：

不同 Artifact 管理不同领域。

不能简单理解成一个全局优先级。

---

# 11. 为什么不做一个万能 Skill

不推荐：

```text
admin-builder
```

一个 Skill 同时负责：

```text
PRD
Figma
Design System
Frontend
Review
```

因为这样很容易导致职责混乱。

例如模型可能在开发阶段重新解释 PRD，然后修改已有页面结构。

或者在设计阶段自行修改业务规则。

拆分后：

```text
prd-to-admin-spec
= What

prd-to-admin-design
= Design

figma-to-design-md
= Design Language

figma-to-admin-page
= Implementation

admin-ui-review
= Quality

admin-workflow
= Routing
```

每一个 Skill 都只解决一个明确问题。

---

# 12. 为什么需要 ADMIN_SPEC.md

直接使用：

```text
PRD → Figma
```

存在很大不确定性。

例如一个：

```text
查看用户详情
```

不同 AI 执行可能分别设计成：

```text
Dialog
Drawer
Detail Page
```

建立 `ADMIN_SPEC.md` 后：

```text
User Detail
page_type: detail-page
route: /users/:id
```

后续设计和开发就不会重复猜测。

---

# 13. 为什么需要 DESIGN.md

Figma 是人类很容易理解的视觉信息。

但对于 AI 来说，每次重新读取整个 Figma：

* 上下文成本高
* 分析速度慢
* 容易遗漏
* 每次理解可能略有差异

因此：

```text
Figma
 ↓
DESIGN.md
```

实际上是把视觉设计转换成 AI 更稳定的设计语言。

以后：

```text
DESIGN.md
+
Target Figma Frame
```

就足够支持大部分页面开发。

---

# 14. Figma 原则

设计和开发过程中应优先理解：

```text
Variables
Components
Variants
Auto Layout
Constraints
Styles
Instances
```

不要把 Figma 当截图。

同样也不要通过大量：

```text
position: absolute
left: xxx
top: xxx
```

来模拟设计稿。

后台页面应该使用真实 Web Layout。

---

# 15. Component First

无论设计还是开发，都应该遵循：

```text
Search Existing
      ↓
Can Reuse?
 ┌────┴────┐
Yes        No
 ↓          ↓
Reuse    Determine
          ↓
      Shared Component?
        ┌────┴────┐
       Yes        No
        ↓          ↓
      Create    Local UI
```

不要遇到一个新页面就创建：

```text
UserButton
OrderButton
MerchantButton
FinanceButton
```

如果本质都是 Button，应继续使用统一 Button Component。

---

# 16. 后台 UI 原则

整个 Skill 集合主要服务于：

```text
B2B
Admin
SaaS
Operations
Management Console
```

后台设计优先：

```text
Efficiency
Clarity
Consistency
Density
Scannability
Predictability
```

而不是：

```text
Decoration
Huge Typography
Marketing Visual
Excessive Animation
Oversized Cards
```

---

# 17. Table First

后台系统中 Table 通常是最重要的信息载体之一。

需要特别关注：

```text
Column Priority
Column Width
Alignment
Search
Filter
Sort
Pagination
Selection
Bulk Actions
Row Actions
Status
Long Text
Money
Date Time
ID
```

操作数量较多时优先：

```text
Primary Action
+
More Dropdown
```

而不是每行排列大量按钮。

---

# 18. 安全操作

以下操作需要特别处理：

```text
Delete
Ban
Freeze
Reject
Reset
Clear
Force Stop
Balance Adjustment
Permission Change
```

一般需要：

```text
Danger Style
+
Confirmation
+
Impact Description
+
Reason
```

重大操作可考虑二次确认。

---

# 19. 版本控制建议

推荐将以下内容提交 Git：

```text
.agents/skills/
AGENTS.md
ADMIN_SPEC.md
DESIGN.md
```

这样：

```text
PRD Change
Design Change
Skill Change
Implementation Change
```

都能够通过 Git 进行追踪。

---

# 20. 推荐开发节奏

不推荐一次：

```text
把整个后台全部做完
```

推荐按照模块推进：

```text
用户管理
 ↓
Review

订单管理
 ↓
Review

财务管理
 ↓
Review

系统管理
 ↓
Review
```

每完成一个模块就运行：

```text
admin-ui-review
```

比最后统一检查整个项目更稳定。

---

# 21. 项目最终形态

推荐最终项目结构：

```text
project/
│
├── .agents/
│   └── skills/
│       ├── admin-workflow/
│       ├── prd-to-admin-spec/
│       ├── prd-to-admin-design/
│       ├── figma-to-design-md/
│       ├── figma-to-admin-page/
│       └── admin-ui-review/
│
├── AGENTS.md
│
├── PRD.md
├── ADMIN_SPEC.md
├── DESIGN.md
│
├── src/
│
└── package.json
```

最终形成：

```text
                 PRD.md
                    │
                    ▼
             ADMIN_SPEC.md
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
      DESIGN.md             Figma
          │                   │
          └─────────┬─────────┘
                    ▼
              Frontend Code
                    │
                    ▼
              admin-ui-review
```

---

# 22. 核心原则总结

整套系统只需要记住几个原则：

```text
PRD 决定业务

ADMIN_SPEC 决定页面结构

DESIGN.md 决定设计语言

Figma 决定具体视觉

Existing Code 决定工程实现方式

Review 保证整个链路没有偏离
```

Skill 不应该互相抢职责。

不要让 Designer 修改产品逻辑。

不要让 Frontend Skill 重新设计页面。

不要让 Design System Skill 重新定义业务。

不要让 Workflow 自己完成所有具体工作。

保持职责边界，才能让整个后台系统随着页面数量增加仍然保持稳定和一致。
