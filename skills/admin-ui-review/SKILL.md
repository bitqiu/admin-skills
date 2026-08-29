---
name: admin-ui-review
description: >-
  审查后台管理系统从 PRD、ADMIN_SPEC、DESIGN.md、Figma 到前端代码的需求追踪、设计还原和实现质量。适用于 UI review、一致性核对及明确要求的 review-and-fix；仅审查时不得修改产物。
---

# Admin UI Review

以证据为基础审查后台管理系统的需求、设计和实现链路。目标是找出会影响交付的具体偏差，而不是重新定义产品、泛谈设计理论，或为了追求像素级一致而重写稳定页面。

## Scope

审查链路：

```text
PRD Requirement
  -> ADMIN_SPEC Page / Interaction
  -> DESIGN.md Rule
  -> Figma Page / Component
  -> Frontend Route / Component / Behavior
```

覆盖四个维度：

1. Requirement Fidelity
2. Design Fidelity
3. Design System Consistency
4. Implementation Quality

本 Skill 是 Reviewer：

- 默认只读取、运行和验证，不修改 PRD、`ADMIN_SPEC`、`DESIGN.md`、Figma 或前端代码。
- 只有用户明确要求“检查并修复”“review and fix”或同等含义时才进入修复模式。
- 不重新定义产品需求，不擅自改变 Design System，不为没有证据的偏好制造问题。
- 没有发现问题时直接说明，不为填满报告而提出无意义改写。

## Review modes

开始时根据用户原话确定模式：

- **Review only**：检查、对比、核对、review。只输出报告；允许执行只读检查、构建、测试、截图和浏览器验证。
- **Review and fix**：检查并修复、review and fix。先形成问题清单，再按 `Critical -> Major -> Minor` 修复并验证。

`Suggestion` 默认不实施，除非用户明确要求或它是完成已请求修复所必需的小范围调整。

## Evidence discipline

### Collect sources

先读取用户明确提供的材料，再在用户指定的仓库或目录内查找：

- PRD、验收标准、业务规则、当前用户补充说明
- `ADMIN_SPEC.md` 或同类后台页面规格
- `DESIGN.md`、设计 token、主题配置、共享样式
- Figma 文件、页面、Frame、组件、变量及原型交互
- 前端路由、页面、组件、样式、测试和运行中的界面

记录每类材料的实际路径、URL、Figma node 或代码位置。不要只根据文件名推断内容。

如果材料缺失：

- 继续审查仍可验证的链路，不把整个任务阻塞。
- 将缺失来源写为 `Not provided` 或 `Not accessible`，对应结论写为 `Unverified`。
- 不把“无法验证”写成“符合要求”，也不把推测写成发现。
- 只有缺失材料导致用户的核心问题完全无法回答时，才请求补充材料。

### Resolve authority and conflicts

不同材料承担不同职责，不应简单互相覆盖：

- 当前用户的明确说明与已批准变更决定本次审查范围和最新业务意图。
- PRD 与验收标准定义产品需求。
- `ADMIN_SPEC` 将需求落实为后台页面、字段、状态、操作和权限。
- `DESIGN.md` 定义视觉与组件规则。
- Figma 定义当前已批准页面设计与交互表达。
- Code 定义实际交付行为。

发现材料冲突时报告冲突两端，不擅自选择一个版本修正。若仓库有明确的文档版本、批准状态或更新时间，可据此判断，并在证据中说明。

## Workflow

### 1. Establish review scope

确定：

- 要审查的模块、页面、路由和视口
- 是否覆盖交互状态、权限和响应式布局
- 当前是 Review only 还是 Review and fix
- 可用与缺失的证据来源

不要把用户指定的单页审查扩展成无边界的全仓库审计。共享组件或 token 可能影响目标页面时，可以追踪到其定义处。

### 2. Build the traceability matrix

在详细视觉审查前，先建立内部追踪表：

```text
Requirement ID / statement
-> ADMIN_SPEC module + Page ID + field/operation/state
-> Figma page + frame/component
-> Code route + component/test
-> Coverage status
```

Coverage status 使用：

- `Covered`
- `Partial`
- `Missing`
- `Conflicting`
- `Unverified`
- `Not applicable`

优先保留已有 Requirement ID 和 Page ID。没有编号时使用简短、稳定的本地编号，但不要回写源文档。

检查断链：

- PRD 需求没有进入 `ADMIN_SPEC`
- `ADMIN_SPEC` 页面或字段没有进入 Figma
- Figma 页面、组件或交互没有对应代码路由
- 代码实现没有可追溯的规格或设计依据
- Route 存在但菜单、权限或导航无法到达

断链本身的严重级别取决于业务影响；不要把所有断链机械地标为同一级别。

### 3. Review requirement fidelity

逐条比较 PRD、`ADMIN_SPEC`、Figma 和 Code，重点检查：

- 页面、入口、菜单和路由
- 表格列、筛选、搜索、排序、分页和导出
- 表单字段、默认值、必填、校验和提交反馈
- 详情区块、状态、枚举、格式化与敏感信息处理
- 行操作、批量操作、操作前置条件与结果反馈
- 权限、禁用、只读和不可见条件
- Loading、Empty、Error、Disabled 等状态
- 确认弹窗、危险操作、失败恢复和审计信息
- 响应式或指定视口要求

示例：PRD 要求 `Phone / Status / Balance / Register Time`，而 Figma 或 Code 缺少 `Register Time`，报告为 `Missing Requirement`，并指出缺失发生在哪一段链路。

不要因为 API 或数据模型存在某个字段，就断言 PRD 要求在页面展示它。

### 4. Review design fidelity

比较 Figma 与运行中的 Code，而不只比较源码字面值。覆盖：

- Layout 与信息层级
- Spacing 与密度
- Typography
- Color
- Border 与 Radius
- Component size
- Table、Form、Dialog、Drawer
- Icon、图标语义与尺寸
- Alignment
- Hover、Focus、Selected、Disabled、Loading、Empty、Error 等状态
- 点击、输入、展开、分页、切换和确认等交互
- 目标桌面宽度及需求中明确要求的响应式视口

优先使用可重复的运行和截图证据。Figma 和页面截图必须使用相同或可比的视口与状态；视口、内容或数据不同造成的偏差不要伪装成精确比较。

像素差异只有在明显影响层级、布局、可用性或 Design System 时才提升为问题。孤立的轻微抗锯齿、字体渲染或亚像素差异通常不报告。

### 5. Review design system consistency

将 `DESIGN.md`、token 和现有共享组件与 Figma、Code 对照，检查：

- 页面 padding、栅格、间距和密度
- 颜色 token、语义色和重复硬编码颜色
- 字体族、字号、字重、行高和文本层级
- Border、Radius、Shadow
- Button 层级、尺寸、状态和危险操作样式
- Table、Form、Dialog、Drawer 等共享模式
- Icon library 与图标风格
- 已有组件与重复组件
- 亮色、暗色或主题行为（仅在项目要求时）

例如 `DESIGN.md` 规定 page padding 为 `24px`，目标代码使用 `16px` 且没有局部例外依据，应报告为 `Design System Violation`。

先确认硬编码值是否是已批准的局部例外或底层 token 实现。不要只凭出现数字就判定为 magic number 或违规。

### 6. Review implementation quality

在目标页面及其直接依赖范围内检查：

- 是否复用已有组件、hook、token 和工具函数
- 是否创建功能或视觉重复的组件
- 是否过度使用 absolute positioning
- 是否存在缺少语义或说明的 magic number
- 是否破坏 responsive layout、滚动、溢出或文本适配
- 是否混用 icon library 或重复打包图标
- 是否无必要新增 dependency
- 是否符合项目目录、命名和状态管理规范
- 是否存在明显难以维护的条件分支、复制粘贴或样式耦合
- 交互是否具备键盘、focus、label 等项目所需的基本可访问性
- 列表 key、异步状态、表单提交和危险操作是否存在明显行为风险

复用不是绝对目标：现有组件无法满足语义、行为或可访问性要求时，局部新组件可以合理。报告问题时说明为什么当前选择造成实际风险。

### 7. Consolidate and classify findings

将相同根因造成的多处现象合并为一个 finding，并列出受影响位置。每个 finding 使用稳定 ID：`CRIT-01`、`MAJOR-01`、`MINOR-01`、`SUG-01`。

严重级别：

- **Critical**：功能错误、核心需求缺失、权限或数据暴露、金额/状态错误、危险操作缺少必要保护，或会导致用户执行错误操作的偏差。
- **Major**：明显页面结构缺失、关键操作或状态不完整、主要 Figma 布局偏差、Design System 核心规则被破坏、响应式主流程不可用。
- **Minor**：局部视觉、间距、对齐、状态细节或可维护性问题，不阻断主要任务。
- **Suggestion**：可选优化，不影响当前验收和交付。

严重级别由影响决定，而不是由差异数量决定。证据不足的判断放到 `Remaining`，不要虚增为问题。

### 8. Fix only when requested

在 Review and fix 模式中：

1. 先确认问题和根因。
2. 按 `Critical -> Major -> Minor` 顺序修复。
3. 优先复用现有 token、组件和目录模式。
4. 为每个修复执行与风险相称的构建、测试和界面验证。
5. 重新检查受影响链路，避免修复一个页面时破坏共享组件消费者。

不要因为细小视觉差异大规模重构稳定页面。不要修改 PRD、`ADMIN_SPEC`、`DESIGN.md` 或 Figma 来掩盖代码偏差，除非用户明确要求修改对应来源且证据表明来源本身有误。

若某项修复需要产品决策、设计批准、不可用的 Figma 权限或缺失接口，将它保留在 `Remaining`，说明阻塞原因和所需决定。

## Review output

保持报告简洁，按以下结构输出。没有对应项时写 `None`。Review only 模式下 `Fixed` 必须写 `None (review only)`。

```markdown
## Summary

- Scope: [pages/routes/viewports]
- Mode: [Review only | Review and fix]
- Evidence: [available sources and unavailable sources]
- Traceability: [covered / partial / missing / unverified counts]
- Findings: [Critical n, Major n, Minor n, Suggestion n]

## Critical

### CRIT-01 [Short title]
- Expected: [requirement, Figma target, or Design System rule]
- Actual: [observed behavior or implementation]
- Location: [source section/node and code path:line/route]
- Action: [specific correction]
- Evidence: [how the difference was verified]

## Major

[Same finding format]

## Minor

[Same finding format; put optional suggestions here with SUG IDs]

## Fixed

- [Finding ID]: [change and verification]

## Remaining

- [Finding ID or Unverified item]: [reason, impact, and required decision/input]
```

在 `Location` 中尽量同时给出需求/设计位置和代码位置。能够定位时使用文件与行号、route、Figma page/frame/node；不要只写“表格组件”这类模糊位置。

报告只列可执行、证据充分的问题。不要粘贴大篇设计理论，也不要复述所有符合项；符合项用 Summary 中的覆盖统计概括即可。

## Completion checks

结束前确认：

- 审查范围和证据来源已说明。
- PRD Requirement 到 Code Route 的每一段可用链路都已检查。
- 四个 Review Dimensions 均已覆盖，或明确标为 Unverified / Not applicable。
- 每个 finding 都包含 Expected、Actual、Location 和 Action。
- 严重级别反映业务和交付影响。
- Review only 没有产生文件修改。
- Review and fix 已记录 Fixed、验证结果和 Remaining。
- 没有为了凑问题而建议重写稳定页面或改变 Design System。
