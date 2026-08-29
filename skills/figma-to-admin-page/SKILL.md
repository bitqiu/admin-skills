---
name: figma-to-admin-page
description: >-
  根据指定 Figma frame/node 在现有 React、Vue 或其他后台 Web 项目中实现生产级页面。结合 DESIGN.md、ADMIN_SPEC.md 和已有组件；不用于单独提取设计系统、修改 Figma 或生成孤立 HTML demo。
---

# Figma to Admin Page

把已有 Figma 后台页面落入当前前端项目，产出符合项目架构、可维护、可扩展并具备合理交互与状态的真实页面。Figma 不是待描摹的截图；先理解设计结构和工程结构，再选择正确的 Web 布局与现有组件实现。

需要能够读取目标前端项目。读取 Figma 时使用当前环境提供的 Figma MCP 或 Figma Skills，并遵守其既有工作流。

## Scope

完成以下转换：

```text
Figma target frame
+ DESIGN.md
+ Existing Codebase
+ ADMIN_SPEC.md (if present)
-> Production-ready Admin Page
```

本 Skill 负责页面实现、必要的路由接入、局部数据适配、交互状态和验证。它不负责：

- 从 Figma 单独提取或创建设计系统
- 在 Figma 中重新设计、补画或改造页面
- 脱离当前项目创建孤立 HTML Demo
- 在没有证据时虚构真实 API、权限规则或业务状态流
- 为一个局部页面无必要地重构整个应用或引入新的 UI 框架

用户同时要求提取设计系统时，先使用对应的 Figma-to-design-system / DESIGN.md Skill 完成该阶段，再使用本 Skill 实现页面。环境提供 Figma MCP 或 Figma Skills 时，先完整读取并遵循对应 Skill；不要在本 Skill 中自行发明底层 Figma 调用流程。

## Source priority

遇到冲突时按以下优先级处理：

1. 用户当前明确要求
2. Figma target frame
3. `DESIGN.md`
4. `ADMIN_SPEC.md`
5. Existing Components
6. Existing Project Conventions

每种来源承担不同职责：

- Figma target frame 是当前页面结构和视觉的真源。
- `DESIGN.md` 是跨页面 token、组件视觉和设计规则的真源。
- `ADMIN_SPEC.md` 是字段含义、业务交互、权限和状态流的真源。
- Existing Codebase 是依赖、组件 API、路由、数据访问和工程组织的真源。

不要用低优先级来源覆盖高优先级的明确证据。若冲突会影响业务正确性、权限、安全或不可逆操作，先说明冲突并请求用户确认；可逆的实现细节可按优先级合理决策。

## Workflow

### 1. Resolve the exact target

确认需要实现的 Figma file、page、frame 或 node，以及目标代码库、路由和页面范围。若用户给出多个 node，只读取与当前页面及其必要组件直接相关的内容。

检查项目根目录及就近的 agent instructions。查找并阅读当前任务相关的：

- `DESIGN.md`
- `ADMIN_SPEC.md`
- Figma 资源或导出 asset 说明
- 页面验收标准、API 文档或类型定义

没有 `DESIGN.md` 或 `ADMIN_SPEC.md` 时继续工作，不要为缺失的可选文件阻塞。只在缺少的信息会实质改变目标页面、业务规则或写入位置时提问。

### 2. Understand the existing project before coding

在创建文件前先建立项目地图。至少检查适用的目录和文件：

- `package.json` 及 lockfile，确认框架、版本、脚本和已有依赖
- `src` 或等价源码根目录
- `components` / shared UI
- `layouts`
- router / route definitions
- `pages` / `views`
- global styles、CSS modules、Tailwind 配置或 CSS-in-JS 方案
- theme、tokens 和 `DESIGN.md`
- hooks / composables
- API client、query/mutation 和错误处理约定
- state management
- permissions / auth guards
- tests、Storybook 或 preview 约定

主动寻找一个或多个相似页面，重点学习其 route、目录、命名、查询参数、表格、表单、hooks、请求状态、权限和测试方式。新页面应像项目原本的一部分，而不是外接样例。

不要看到 Figma 后立即创建大量文件。先确定最小合理改动面，以及哪些模块确实需要新增或调整。

### 3. Read Figma as structured design

使用环境已有 Figma 读取工作流获取设计上下文。优先读取 node 的结构化信息和组件关系；截图用于整体视觉核对，不替代设计上下文。

理解并记录：

- Auto Layout、方向、gap、padding 和对齐
- Parent / Child 层级
- Component Instance、Variants 和复用关系
- Constraints、固定/自适应尺寸和滚动区域
- Text Styles、Variables、颜色和效果
- 页面宽度、内容区域、栅格、密度与留白
- 图标、图片、品牌图形和其他 asset
- 设计中表达的交互状态或替代视图

把这些关系翻译为语义化 HTML 和正常 Web layout。不要把 frame 坐标逐项翻译为 CSS 坐标。

### 4. Discover reusable components

创建组件前，主动搜索现有实现、导出名、用法和相似页面。至少覆盖：

- Button
- Input
- Select
- Search / SearchInput
- Table / DataTable
- Form
- Modal / Dialog
- Drawer
- Tabs
- Pagination
- Badge / Tag
- Dropdown / Menu
- PageHeader
- Breadcrumb
- Card
- Empty
- Loading / Skeleton
- Error / Result

同时搜索项目中语义相同但名称不同的组件。阅读组件 API、variants、tokens 和实际调用，不能仅凭文件名判断能否复用。

已有组件能够承担相同职责时优先复用。几像素差异通常应通过现有 props、variant、size、className 插槽或 token 调整解决，而不是复制一套组件。只有在以下情况下新增组件：

- 现有组件的职责或交互模型明显不同
- 强行扩展会破坏多个既有消费者
- 当前页面存在可识别且值得复用的新领域组件

不要为了单页抽象只使用一次、没有降低复杂度的包装层。

### 5. Build an internal component map

写主要页面代码前，在内部建立并核对映射：

```text
Figma Layer -> Existing Component / Extended Variant / New Component
```

例如：

```text
PageHeader       -> PageHeader
Filters/Search   -> SearchInput
Filters/Status   -> Select
UserTable        -> DataTable
Status           -> StatusBadge
Actions          -> DropdownMenu
```

这张表不要求展示给用户，但必须用于决定复用边界、必要 props、数据流和文件改动。映射不清楚时继续阅读现有组件与相似页面，不要直接开始堆 JSX 或 template。

### 6. Plan the smallest native implementation

确定：

- 页面文件和 route 接入点
- 复用、扩展和新增的组件
- 数据来源与类型
- URL query、local state、server state 的职责
- 搜索、筛选、分页、tabs 和弹层行为
- loading、empty、error、disabled 和权限状态
- 需要使用或导出的 asset
- 适合当前风险的测试与视觉验证方式

沿用项目技术栈。React 项目遵循现有 hooks、query、form 和 component patterns；Vue 项目遵循现有 Composition API / Options API、composables、store 和 component patterns。不要仅因个人偏好迁移框架写法。

### 7. Implement layout and styling

用浏览器布局表达 Figma 的结构关系：

- 优先 `flex`、`grid`、`gap`、padding、margin、width、min/max constraints
- 使用项目已有 breakpoint 和桌面横向滚动策略
- 为 toolbar、filters、table、pagination 等固定格式区域设置稳定约束，避免内容或状态变化导致跳动
- 后台页面以桌面工作流为主，但常见桌面宽度变化不能导致重叠、截断或结构破坏
- table 等复杂结构可按项目惯例横向滚动；不要擅自重构为移动卡片 UI

避免大量 absolute positioning、固定坐标、translate 微调和散落的 magic numbers。只有 overlay、badge、decorative layer 或本身需要覆盖的元素才使用 absolute。

若 `DESIGN.md`、theme 或项目已定义 token，使用 CSS variables、theme tokens、Tailwind theme、design-system variables 或 component variants。不要在多个位置重复 hardcode 已存在的颜色、尺寸、圆角或阴影。

### 8. Implement behavior and data honestly

若 Figma 或 `ADMIN_SPEC.md` 包含以下能力，按项目惯例实现完整而合理的交互：

- Search
- Filters and reset
- Pagination
- Tabs
- Dialog / Modal
- Drawer
- Dropdown and row actions
- Form validation and submission states
- Selection and bulk actions
- Sorting or URL state

接入已有 API 时沿用项目的 client、types、query keys、缓存、错误提示和权限约定。没有 API 且用户只要求 UI demo 时，使用清晰、有限的 mock data 与 local state；不要伪造网络请求或声称已连接真实后端。

不要把大量业务 mock data 混在页面 JSX 或 Vue template 中。按项目惯例放入 local mocks、fixtures 或 page constants，但简单页面不要因此过度分层。

至少考虑 loading、empty 和 error。若项目已有统一组件，必须复用；若页面包含危险、不可逆或有权限约束的操作，严格按 `ADMIN_SPEC.md` 或现有业务模式处理，不能从视觉稿猜测业务规则。

### 9. Preserve icon and asset consistency

使用项目已有 icon library 和封装。项目使用 Lucide、Ant Design Icons、Material Icons 或其他图标库时，保持同一套体系，不要为一个 Figma 图标引入新库。

品牌图形、特殊插画、产品截图或无法由现有图标表达的 asset，优先复用项目已有资源或从 Figma 获取的有效 asset。保持合理格式、清晰度、命名和导入方式。

除非现有依赖明显无法满足必要能力，否则不要新增 dependency。新增依赖前检查 bundle、license、维护状态以及项目是否已有等价方案。

### 10. Verify in three passes

实现后运行适合项目的 format、lint、typecheck、unit/widget tests 和 build。修复由本次改动引入的问题；对无关的既有失败明确区分，不要修改无关代码来掩盖它们。

启动或复用本地开发环境，打开真实 route 做视觉验证。在环境允许时使用浏览器截图或前端测试工具检查至少一个项目主要桌面 viewport，并补充一个较窄的常见桌面 viewport。验证 console error、关键交互、滚动和文本容纳。

执行三轮对照：

#### Figma vs Implementation

检查：

- 页面结构、内容宽度和 page padding
- 文案、表格列、筛选项和按钮
- icon 与 asset
- alignment、spacing 和 visual grouping
- typography、font weight 和 line height
- input/button/table row height 与内部 padding
- color hierarchy、border、radius 和 elevation

Pixel accurate 指视觉关系与细节可信，不代表用绝对定位硬画截图。发现 critical 或明显差异时直接修复并再次检查。

#### DESIGN.md vs Implementation

检查 token、组件 variant、字体、颜色、间距、圆角、状态和响应式规则。若 Figma 页面特例与跨页面系统规则冲突，保留 Figma 的当前页面意图，同时以最小、可解释的方式实现，避免污染全局 token。

#### ADMIN_SPEC.md vs Implementation

检查字段、业务文案、搜索范围、筛选语义、分页、tabs、row actions、弹层、校验、权限和 loading/empty/error 状态。视觉稿缺少但规格明确要求的业务状态仍需实现，并保持设计系统一致。

## Completion criteria

只有满足以下条件才算完成：

- 页面已接入目标项目与正确 route，而非独立 demo
- 最大化复用了现有组件、tokens、icons 和工程模式
- Figma layer 到代码组件的职责映射清晰
- 页面主要视觉、内容与交互和目标 frame 一致
- `DESIGN.md` 与 `ADMIN_SPEC.md` 的适用要求已落实
- loading、empty、error 以及适用的 disabled/permission 状态已处理
- 常见桌面宽度下布局稳定，复杂表格按项目策略滚动
- 相关校验通过，或已清楚说明无法运行的检查与原因
- 没有新增无必要依赖、虚构 API 或扩大任务范围

## Completion response

简洁报告：

- 实现的页面与 route
- 主要复用或扩展的现有组件
- 实现的关键交互和状态
- 执行的验证及结果
- 仍需用户或后端确认的真实缺口

不要把内部 component mapping 全表或大段实现过程粘贴给用户；只保留有助于验收和后续维护的信息。
