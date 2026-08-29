---
name: prd-to-admin-spec
description: >-
  将后台管理系统 PRD、产品需求文档、API 文档、数据模型、数据库结构或已有后台说明转换为结构化、可追踪的 ADMIN_SPEC.md。用户要求“根据 PRD 设计后台”“分析 PRD 有哪些后台页面”“生成后台页面规格”“整理后台管理系统页面”“PRD 转后台 UI Spec”，或需要在 Figma / 前端实现之前提取后台模块、菜单、页面、表格、筛选、表单、详情、弹窗、操作、状态、权限和异常态时，应使用此 Skill，即使用户没有明确提到 ADMIN_SPEC.md。若任务只是创建或修改 Figma、编写 React/Vue 页面、定义视觉风格、生成 DESIGN.md、设计营销页面，或实现非后台管理产品，且不需要先产出后台页面规格，则不应使用此 Skill。
---

# PRD to Admin Specification

把产品需求证据转换为可供产品、设计、研发和测试共同使用的后台页面规格。最终交付物是 `ADMIN_SPEC.md`；不要把页面规格混同为视觉稿或实现方案。

## Scope

只完成：

```text
PRD / API / Data Model / Existing Admin Docs -> ADMIN_SPEC.md
```

不要在此 Skill 中：

- 创建或修改 Figma 文件
- 编写 React、Vue 或其他前端页面
- 定义字体、颜色、阴影等具体视觉风格
- 生成 `DESIGN.md`
- 将推测包装成已确认的业务规则
- 扩展 PRD 中不存在的大型业务能力

如果用户同时要求后续设计或实现，先把 `ADMIN_SPEC.md` 作为独立阶段完成；除非用户明确要求继续且当前任务具备相应能力，否则在该文件完成后停止。

## Workflow

### 1. Collect source evidence

先读取用户明确指定的文件或内容，再在用户指定的项目范围内查找与后台需求直接相关的材料：

- PRD、产品需求文档和验收标准
- API / OpenAPI 文档
- 数据模型、数据库 schema 和枚举定义
- 已有后台说明、菜单定义、权限说明和操作流程
- 当前 `ADMIN_SPEC.md`

如果存在 `ADMIN_SPEC.md`，先判断它与当前需求的关系：

- 当前结构正确且大部分内容仍有效：增量更新，保留已验证内容和稳定 Page ID。
- 与新证据局部冲突：按证据优先级修订冲突部分，并在 Traceability 或 Missing Requirements 中记录影响。
- 已明显过期、结构不可用或用户明确要求重建：重新生成，但保留仍可证实的事实。

不要无条件覆盖已有文件，也不要删除无法从新 PRD 反证的正确内容。

没有任何可定位的需求来源时，才请求用户提供文件或路径。PRD 只是局部不完整时不要停下，继续输出并标注不确定性。

### 2. Build a requirement ledger

在设计页面之前，先形成内部需求清单。为可识别的需求保留原始编号；没有编号时创建稳定的本地编号，例如 `REQ-001`。每条需求归入一种证据级别：

- `Confirmed Requirement`：来源明确表达的业务、数据、角色或流程要求。
- `Derived Requirement`：为让已确认流程在后台可操作而必需的 UI 或状态处理，可从证据直接推导。
- `Assumption`：不会改变核心业务规则、可逆的后台默认设计。
- `Missing Requirement`：缺失答案会改变权限、状态流转、资金/风控结果、数据语义或不可逆操作。

不要把 API 字段存在等同于页面必须展示，也不要把数据库可写等同于操作有权限。记录来源文件、章节或接口名，以便最终追踪。

### 3. Model the admin information architecture

从需求中识别并归并：

1. **Domain / Module**：例如用户、订单、商户、产品、财务、风控、系统配置。
2. **Entity**：例如 User、Order、Merchant、Transaction、Product。
3. **Operation**：List、Detail、Create、Edit、Delete、Search、Filter、Export、Approve、Reject、Enable、Disable、Freeze、Unfreeze、Retry、View Logs 等。
4. **Page**：List、Detail、Create、Edit、Settings、Dashboard、Log 等页面类型。
5. **Navigation**：菜单层级、入口、面包屑、页面跳转、返回行为和跨模块关系。

模块边界应反映用户任务与权限边界，而不是简单按 API 文件或数据库表拆分。相同实体的列表、详情和维护流程通常归入同一模块；共享配置或审计能力可以独立成模块，但必须有需求依据。

先画出导航结构，再逐页展开。只有具有独立导航目的、URL、权限边界或复杂工作流的界面才作为 Page；普通 Dialog 和 Drawer 作为所属页面的子交互记录。

### 4. Translate operations into admin UI

根据任务复杂度、信息量、风险和使用频率选择交互，不机械套模板：

- 查询条件通常映射为 Filter；高频关键字查询映射为 Search。
- 数据集合通常映射为 Table，并明确分页、排序和默认顺序。
- 简单且上下文明确的编辑可用 Dialog；字段多、分步或需要离开上下文校验时使用独立 Page。
- 辅助信息可用 Drawer；完整业务记录、跨区块信息或可深链内容使用 Detail Page。
- 危险或不可逆操作使用 Confirm Dialog，并说明影响、对象和确认文案要求。
- 状态分类只有在类别稳定且有高频切换价值时使用 Tabs / Segmented Control。
- 多个低频行操作可收纳在 Dropdown；高频主操作保持直接可见。
- 批量处理使用 Table Selection + Bulk Actions，并明确选择范围、资格限制和部分失败处理。

主动补全后台操作闭环所需的派生规格，例如查询、时间范围、状态筛选、分页、排序、批量操作、导出、操作日志、确认、权限和异常态。只有在业务有依据或是完成既有流程所必需时才补全；不要因此新增独立业务模块。

### 5. Specify every page completely

为每个页面分配稳定、唯一的 Page ID，例如 `USR-LIST-01`。Route 优先沿用已有路由约定；没有证据时给出一致的建议值并标注 `Assumption`。

每个 Page 必须逐项包含以下字段。若某项不适用，写 `None` 并简述原因，不要省略字段：

- **Page ID**
- **Page Name**
- **Module**
- **Purpose**
- **Route**
- **Page Type**
- **Requirement Level**：涉及的 Confirmed / Derived / Assumption 标记
- **Breadcrumb**
- **Primary Action**
- **Secondary Actions**
- **Filters**：字段、控件、数据源、默认值、联动、重置行为
- **Search**：搜索范围、匹配方式、触发方式
- **Metrics / Summary**：指标定义、时间口径、刷新方式
- **Tabs**：分类依据、数量、默认项和 URL / filter 同步方式
- **Table Columns**：字段、展示格式、可排序性、固定列、脱敏和缺省值
- **Pagination / Sorting**：分页模式、默认页大小、可选页大小、默认排序和可排序字段
- **Row Actions**：可见条件、权限、前置状态和结果
- **Bulk Actions**：选择范围、资格、确认、执行反馈和部分失败处理
- **Detail Sections**：区块、字段、来源、敏感数据处理
- **Forms**：字段、类型、必填、默认值、校验、依赖、提交结果
- **Dialogs**：触发、内容、操作、关闭规则和结果反馈
- **Drawers**：触发、内容、宽度需求、可深链性和关闭规则
- **Status**：状态值、语义、显示位置和允许操作
- **Permissions**：页面、字段和操作级权限；未知权限不可自行命名为既定角色
- **Data Dependencies**：API、数据实体、枚举、计算值、刷新和缓存要求
- **Navigation Relationship**：入口、出口、详情/编辑跳转、返回时状态保留
- **Loading State**
- **Empty State**：首次空数据和筛选无结果应按需要区分
- **Error State**：接口失败、部分失败、重试和错误反馈
- **Unauthorized State**：无页面权限、无字段权限和无操作权限的呈现与去向
- **Disabled State**：禁用条件及原因提示
- **Destructive Action Confirmation**：对象、影响、二次确认和成功/失败反馈

表格列和表单字段应使用结构化表格描述；不要只罗列字段名。操作需说明可见性、可用性和状态前置条件。详情页需按用户判断顺序组织区块，而不是照抄数据库字段顺序。

### 6. Resolve ambiguity without blocking

对可逆、不会改变核心业务流程的问题采用合理默认值并标注 `Assumption`，例如：

- 列表使用服务端分页
- 筛选条件可重置
- 页面跳转返回后保留列表查询状态
- 提交期间按钮禁用以避免重复请求
- 无数据、加载失败和无权限使用不同状态

不要擅自决定以下类型的关键规则，将其记录在 `Missing Requirements`：

- 审批人和审批层级
- 状态能否回退或跨级流转
- 金额、额度、手续费、退款或结算规则
- 删除是否可恢复以及数据保留策略
- 角色的实际授权范围和敏感字段可见性
- 批量操作的业务资格、上限和原子性
- 导出范围、字段脱敏和审计要求
- 失败后的业务补偿、重试幂等和人工介入规则

每个 Missing Requirement 都写明受影响的 Module / Page、为什么重要、需要谁确认，以及在确认前可采用的 UI 占位方式。不要只列问题。

### 7. Validate coverage and consistency

写文件前执行一次完整性检查：

- 每条 Confirmed Requirement 至少映射到一个 Module、Page 或明确的非 UI 说明。
- 每个菜单项都有对应 Page，每个 Page 都能从某个入口到达。
- 列表到详情、创建、编辑、日志等关系闭合，返回行为明确。
- 状态名称、枚举和值在页面之间一致。
- 操作的前置状态、权限、确认和结果反馈完整。
- 页面引用的数据能够在 API / 模型中找到，或已标记缺口。
- 没有把推测写成 Confirmed Requirement。
- 没有引入 PRD 无关的大型业务能力。
- 现有 `ADMIN_SPEC.md` 的有效内容没有被无意丢失。

发现冲突时，按以下优先级处理，并记录重要取舍：

1. 用户当前明确说明
2. 当前 PRD、验收标准和业务流程
3. API、数据模型、数据库枚举所证明的数据能力
4. 当前 `ADMIN_SPEC.md`
5. 其他已有后台说明
6. 可逆的后台默认推导

## Output contract

默认在用户指定位置创建或更新 `ADMIN_SPEC.md`；未指定时写入当前任务对应的项目根目录。沿用用户和源文档的主要语言。不要创建 `DESIGN.md` 或设计预览。

使用以下结构；没有内容的章节仍保留，并写明 `None` 或原因：

```markdown
# Admin Specification

## Document Control
## Product Overview
## Requirement Classification
## Navigation Architecture
## Modules

### Module: [Module Name]
#### Module Scope
#### Entities and Operations

#### Page: [Page Name]
##### Page Definition
##### Actions and Navigation
##### Filters and Search
##### Metrics / Summary and Tabs
##### Table, Pagination and Sorting
##### Details
##### Forms
##### Dialogs and Drawers
##### Status and Permissions
##### Data Dependencies
##### UI States and Unauthorized Access

## Shared Interaction Patterns
## Permissions
## Page Relationships
## Status Definitions
## Missing Requirements
## Assumptions
## Traceability
```

`Document Control` 至少记录源文档、生成/更新时间和更新模式（Created / Incremental Update / Rebuilt）。

`Navigation Architecture` 使用树状结构或表格给出菜单层级、Page ID、Route 和权限备注。

`Page Relationships` 记录 `From Page -> Trigger -> To Page / Overlay -> Return Behavior`，避免页面成为孤岛。

`Status Definitions` 统一记录实体、状态、含义、来源、允许操作和可达后续状态；没有证据的流转标为 Missing Requirement。

`Traceability` 最后提供以下映射，确保每个页面和关键交互都能回到需求来源：

```text
PRD Requirement -> Module -> Page -> Component / Interaction
```

推荐字段：Requirement ID、Requirement Summary、Source、Classification、Module、Page ID、Component / Interaction、Coverage Notes。

## Completion response

完成后只简要报告：

- `ADMIN_SPEC.md` 的路径
- 是新建、增量更新还是重建
- 识别出的模块数和页面数
- Missing Requirements 和 Assumptions 的数量
- 使用的需求来源与完成的校验

不要在对话中粘贴完整规格文档。
