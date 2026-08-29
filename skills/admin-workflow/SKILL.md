---
name: admin-workflow
description: >-
  编排后台管理系统从 PRD 到 Figma、前端实现和验收的工作流。适用于跨阶段交付、变更同步或询问下一步；检测现有产物并选择最短有效路径，不代替各阶段专用 Skill。
---

# Admin Workflow Orchestrator

协调后台管理系统的需求、设计、实现与验收阶段。先识别用户真正要到达的终点，再根据现有产物构建最短可行执行路径。阶段产物已经稳定且仍适用时复用它，不为展示流程完整性而重复生成。

## Role boundary

此 Skill 只负责：

- Routing：选择需要使用的后台工作流 Skill
- Sequencing：确定依赖顺序和停止点
- State Detection：识别已有产物、目标对象和项目实现状态
- Artifact Dependency：判断上游变化是否影响下游
- Scope Control：阻止无关阶段和重复工作
- Traceability：汇报每个执行阶段的输入、输出与跳过原因

不要亲自：

- 重新分析完整 PRD 并撰写 `ADMIN_SPEC.md`
- 分析完整 Figma 并提取设计系统
- 在 Figma 中创建或修改完整设计
- 编写大量页面或组件代码
- 代替专用 Skill 完成 UI 评审
- 把下游 Skill 的详细 instructions 复制进当前上下文或输出

可以进行轻量、只读的项目检查，以决定路由和验证阶段交付物。需要实际产出时，调用对应 Skill，让它拥有该阶段的具体判断和编辑权。

## Workflow capabilities

使用以下 Skill 作为阶段执行器：

| Skill | Owns | Typical output |
|---|---|---|
| `prd-to-admin-spec` | 从产品证据整理后台信息架构与交互规格 | `ADMIN_SPEC.md` |
| `prd-to-admin-design` | 根据后台规格创建或更新后台 Figma 设计 | Figma page / frame |
| `figma-to-design-md` | 从可识别的 Figma 设计提取跨页面设计系统 | `DESIGN.md` |
| `figma-to-admin-page` | 在现有前端项目中实现指定 Figma 后台页面 | Frontend code |
| `admin-ui-review` | 对实现结果做设计与交互一致性评审 | Review findings / fixes, as requested |

先从当前可用 Skills 清单或安装位置确认执行器是否可用。目录存在但 `SKILL.md` 仍是占位稿、缺少有效 instructions 或无法读取时，视为不可用。只有被当前路径选中的执行器不可用时才阻塞；可选阶段不可用时跳过并说明原因。

## Artifact ownership

在冲突和变更判断中保持以下边界：

```text
PRD.md          = Product Source of Truth
ADMIN_SPEC.md   = Admin Information Architecture / Interaction Source of Truth
DESIGN.md       = Design System Source of Truth
Figma           = Page Visual Source of Truth
Code            = Engineering Implementation
```

用户当前的明确要求高于这些默认边界。不要让一个产物替另一个产物决定其不拥有的事实：例如，不从 Figma 猜测关键业务规则，也不让 `ADMIN_SPEC.md` 覆盖目标 Figma 的页面视觉细节。

## Orchestration workflow

### 1. Determine the requested outcome

先把请求归为一个明确停止点：

- 规格整理
- Figma 页面设计
- 设计系统提取
- 页面实现
- UI 评审
- 全流程交付
- 变更影响判断或下游同步

按用户动词和明确交付物判断终点。用户只要求一个阶段时，在该阶段完成后停止。若请求只是“给出计划”“判断下一步”或“检查是否需要同步”，只输出路由或影响判断，不调用执行器。

如果“做后台”“处理一下这个设计”等表述无法可靠确定终点，先利用已给文件、Figma 链接和项目状态缩小含义；只有不同解释会导致明显不同产物时才询问用户。

### 2. Inspect current state

在调用任何执行器之前，检查与目标直接相关的范围：

- 可定位的 PRD、需求文本、API 或数据模型是否存在
- `ADMIN_SPEC.md` 是否存在、内容是否有效、是否覆盖当前需求
- `DESIGN.md` 是否存在、是否属于当前产品、是否覆盖目标页面所用系统
- Figma 文件、page、frame 或 node 是否可识别且与任务对应
- 目标前端项目、路由、页面或相似实现是否存在
- 五个工作流执行器中，当前路径所需的 Skill 是否可用
- 工作树中是否有相关未提交修改，避免覆盖用户正在进行的工作

不要只用文件名或修改时间判断状态。结合文档中的来源、版本、traceability、目标 page/frame/node、路由和实现引用，把每项标记为：

- `Missing`：不存在
- `Usable`：存在且与当前目标一致
- `Affected`：存在，但确认受到上游变化影响
- `Ambiguous`：存在，但无法确认是否对应当前目标

只检查足以决定路径的内容，不在路由阶段重做下游 Skill 的深度分析。

### 3. Build the shortest valid route

使用以下默认路由，再根据状态删除不需要的阶段。

| Requested outcome | Route |
|---|---|
| 从 PRD 整理后台页面或规格 | `prd-to-admin-spec` |
| 根据 PRD 创建后台 Figma，规格缺失或受影响 | `prd-to-admin-spec` -> `prd-to-admin-design` |
| 根据 PRD 创建后台 Figma，规格可用 | `prd-to-admin-design` |
| 从 Figma 生成 `DESIGN.md` | `figma-to-design-md` |
| 根据 Figma 实现页面，`DESIGN.md` 可用 | `figma-to-admin-page` |
| 根据 Figma 实现页面，设计系统缺失且用户要求长期一致性 | `figma-to-design-md` -> `figma-to-admin-page` |
| 根据 Figma 实现一次性或临时页面 | `figma-to-admin-page`；不要强制生成完整 `DESIGN.md` |
| 仅评审已有后台实现 | `admin-ui-review` |

完整后台交付默认按以下依赖推进：

```text
prd-to-admin-spec
-> figma-to-design-md       # 仅当已有可复用的参考 Figma 且 DESIGN.md 缺失/受影响
-> prd-to-admin-design
-> figma-to-design-md       # 新 Figma 成为长期设计基准且此前仍没有可用 DESIGN.md 时
-> figma-to-admin-page
-> admin-ui-review
```

同一路径中两个 `figma-to-design-md` 位置是条件分支，不是重复执行：有既有参考设计时在 Figma 设计前提取；没有参考设计但新 Figma 将成为长期基准时，在其确认后、编码前提取。已有可用 `DESIGN.md` 时两个位置都跳过。

不要仅因完整流程图中存在某阶段就调用它。每一步都必须服务于当前终点或下一个必要依赖。

### 4. Validate dependencies and critical targets

调用阶段执行器前确认其最小关键输入：

- `prd-to-admin-spec`：至少有可定位的需求证据；PRD 局部缺失通常不是阻塞，可由该 Skill 标注缺口。
- `prd-to-admin-design`：需要可用的 `ADMIN_SPEC.md`，以及可访问的目标 Figma 上下文或创建目标。
- `figma-to-design-md`：需要可识别、可访问的 Figma 文件或页面范围。
- `figma-to-admin-page`：需要可识别的 Figma target frame/node 和目标前端项目；`DESIGN.md`、`ADMIN_SPEC.md` 可按路径作为补充输入。
- `admin-ui-review`：需要可运行或可检查的页面实现，并需要足以比较的 Figma、规格或明确验收标准。

非关键输入缺失时，把已有材料传给阶段执行器并继续，让拥有该阶段的 Skill 管理局部不确定性。关键对象缺失会让结果指向错误页面或错误项目时，明确指出缺少的对象并停止该分支。例如，用户要求“按这个 Figma 实现”但没有任何可识别的文件、URL、page、frame 或 node 时，不得凭空创造设计。

### 5. Execute one stage at a time

对选中的执行器按顺序执行：

1. 读取该 Skill 的 `SKILL.md`，让它接管当前阶段。
2. 只传递该阶段需要的目标、已有产物、用户约束和已知缺口。
3. 等待阶段完成，不并行运行存在产物依赖的阶段。
4. 检查预期产物是否实际创建或更新，并确认仍对应当前目标。
5. 重新计算剩余路径；阶段结果可能消除后续步骤，也可能暴露真正的阻塞。

如果用户明确要求并行处理多个互不依赖的页面或评审目标，可以并行；不要并行执行 `ADMIN_SPEC.md -> Figma -> Code` 这类有直接依赖的阶段。

执行器失败后，不要假设其产物已经完成并继续下游。先检查是否存在可复用的有效产物；没有则报告失败阶段、已完成阶段和恢复入口。

## Change propagation

上游变化只在语义影响到下游时传播。先识别变化，再检查 traceability 和实际引用：

| Changed source | Propagate when | Possible next stage |
|---|---|---|
| `PRD.md` | 模块、页面、字段、状态、权限、操作或验收规则发生变化 | `prd-to-admin-spec` |
| `ADMIN_SPEC.md` | 页面结构、交互、状态、权限或内容需求影响视觉方案 | `prd-to-admin-design` |
| `DESIGN.md` | 被现有页面使用的 token、组件、布局或状态规范变化 | `figma-to-admin-page` and/or `admin-ui-review` |
| Figma | 目标 frame 的视觉、结构、内容或交互发生变化 | `figma-to-admin-page` |
| Code | 实现需要与 Figma、规格或设计系统重新核对 | `admin-ui-review` |

以下情况通常不应触发全链重跑：拼写修正、注释和元数据变化、未被后台引用的 PRD 段落、未被目标页面使用的 token、无关 Figma frame、无关代码模块。

用户只要求影响分析时，报告受影响的直接下游和证据，不执行更新。用户要求“同步到最新”时，只调用确实受影响的阶段，并在每阶段后重新判断传播是否还需要继续。

## Scope and stop rules

- 以用户请求的最终交付物为停止点，不擅自扩展到后续阶段。
- 已有产物 `Usable` 时跳过生成，并把它作为输入传给下一阶段。
- `Ambiguous` 不能自动当作 `Usable`；先用轻量检查消除歧义，关键歧义仍存在时询问用户。
- 不因为缺少可选产物而阻塞，例如临时页面可以没有完整 `DESIGN.md`。
- 不为证明工作完整而创建额外规划文件、重复预览或副本。
- 不修改 `PRD.md`，除非用户明确要求修改产品源文档且存在拥有该工作的合适能力。

## Completion report

完成后简要报告：

- 用户目标与实际停止点
- 检测到的关键状态
- 实际执行的 Skill 顺序
- 创建、更新、复用或跳过的产物及原因
- 未解决的阻塞、影响范围或下一可执行阶段

保持阶段可追踪，但不要粘贴下游 Skill 的完整产物或 instructions。
