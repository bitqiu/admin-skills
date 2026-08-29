# 使用说明

本仓库提供 6 个可组合的 Agent Skills，用于后台管理系统从 PRD、页面规格、Figma、前端实现到验收的完整交付过程。它们不绑定单一厂商，可安装到 `npx skills` 支持的多种 AI 工具。

仓库中的 `skills/` 是源码分发目录，不会因为克隆仓库就自动作用于其他项目。请使用 [`skills`](https://www.npmjs.com/package/skills) CLI 安装到用户环境或目标业务项目。

## 1. 选择安装范围

| 范围 | CLI 参数 | 适用场景 |
|---|---|---|
| 项目级 | 默认 | 将 Skills 固定到当前业务项目并与团队共享 |
| 用户级 | `--global` / `-g` | 在多个后台项目中使用同一套 Skills |

推荐安装全部 6 个 Skills。`admin-workflow` 是编排器，需要另外 5 个 Skill 执行具体阶段；如果只安装单个 Skill，应直接调用该 Skill，而不是依赖完整工作流。

## 2. 安装

需要本机已安装 Node.js，并且可以使用 `npx`。

### 查看仓库中的 Skills

```bash
npx skills add bitqiu/admin-skills --list
```

该命令只列出可安装项，不执行安装。仓库应返回 6 个 Skills。

### 项目级安装

在目标业务项目根目录安装全部 Skills，并选择要使用的 AI 工具：

```bash
npx skills add bitqiu/admin-skills
```

项目级是默认范围，适合将 Skills 与当前项目绑定。命令会交互式选择 Skills、AI 工具和安装方式。

如果要将全部 Skills 安装到当前项目中所有受支持的 AI 工具：

```bash
npx skills add bitqiu/admin-skills --all
```

### 用户级安装

安装全部 Skills，并使其在所有项目中可用：

```bash
npx skills add bitqiu/admin-skills --all --global
```

### 安装单个 Skill

例如只安装 `prd-to-admin-spec`：

```bash
npx skills add bitqiu/admin-skills --skill prd-to-admin-spec
```

安装多个指定 Skills 时，重复使用 `--skill`：

```bash
npx skills add bitqiu/admin-skills \
  --skill prd-to-admin-spec \
  --skill prd-to-admin-design
```

命令会让用户选择目标 AI 工具。追加 `--global` 可改为用户级安装；使用 `--agent <agent-name>` 可指定 `npx skills` 支持的某个工具。

使用 `--all` 时会安装全部 Skills，并面向所有检测到的受支持 AI 工具跳过交互选择。

## 3. 确认安装

先通过 CLI 检查安装结果：

```bash
# 项目级与用户级
npx skills list

# 只查看用户级
npx skills list --global
```

然后在目标 AI 工具的 Skill 列表、命令面板或上下文中确认这些 Skills 可用。不同工具的选择和调用方式可能不同，请使用对应工具提供的 Skill 入口。

应能看到：

```text
admin-workflow
prd-to-admin-spec
figma-to-design-md
prd-to-admin-design
figma-to-admin-page
admin-ui-review
```

如果没有出现：

1. 运行 `npx skills add bitqiu/admin-skills --list`，确认仓库可访问且能发现 6 个 Skills。
2. 运行 `npx skills list`，确认目标 Skill 已安装到预期 AI 工具。
3. 项目级安装时，确认安装命令是在目标业务项目根目录执行。
4. 用户级安装时，确认命令包含 `--global`。
5. 重启目标 AI 工具。

## 4. 调用方式

### 显式调用

在目标 AI 工具中选择 Skill，或在请求中明确写出 Skill 名称，适合需要严格控制阶段和停止点的任务：

```text
使用 prd-to-admin-spec Skill，读取 PRD.md，生成 ADMIN_SPEC.md。
这个阶段不要创建 Figma，也不要修改前端代码。
```

### 自动触发

如果目标 AI 工具支持根据 description 自动选择 Skill，也可以直接描述任务：

```text
根据 PRD 整理订单管理后台需要的菜单、页面、筛选条件、表格字段和操作权限。
```

当多个阶段需要串联时，建议显式指定 `admin-workflow`，并说明最终交付物：

```text
使用 admin-workflow Skill，读取 PRD 和现有 Figma，完成用户管理模块的页面规格、Figma 设计、前端实现和最终检查。
```

## 5. 各 Skill 用法

### admin-workflow

用于跨阶段任务、变更同步，或判断下一步应该使用哪个 Skill。

建议提供：

- 最终目标，例如“只要规格”“完成 Figma”“实现页面”“检查并修复”
- PRD、Figma 和前端项目的实际位置
- 已存在的 `ADMIN_SPEC.md`、`DESIGN.md` 和页面实现状态
- 明确的模块、页面或 route 范围

示例：

```text
使用 admin-workflow Skill。
项目已有 PRD.md 和 React 后台，也有一套可访问的参考 Figma，但没有 ADMIN_SPEC.md 和 DESIGN.md。
请完成订单管理模块的规格、Figma 设计和前端实现，最后做一致性检查。
```

编排器会检测已有产物并选择最短有效路径，不会为了展示完整流程而重复生成稳定文件。

### prd-to-admin-spec

用于将 PRD、API、数据模型或现有后台说明转换为 `ADMIN_SPEC.md`。

示例：

```text
使用 prd-to-admin-spec Skill。
读取 docs/merchant-prd.md 和 docs/merchant-api.md，生成项目根目录 ADMIN_SPEC.md。
覆盖菜单、route、筛选、表格、详情、审核操作、权限、状态和异常态。
无法从材料确认的业务规则放入 Missing Requirements，不要自行决定。
```

该 Skill 不创建 Figma、`DESIGN.md` 或前端代码。

### figma-to-design-md

用于从已有 Figma 后台产品提取设计系统，并创建：

```text
DESIGN.md
preview.html
preview-dark.html
```

示例：

```text
使用 figma-to-design-md Skill。
分析这个 Figma 后台文件及 User List、Order Detail 和 Settings frames：<Figma URL>
在项目根目录创建或增量更新 DESIGN.md、preview.html 和 preview-dark.html。
Figma 没有定义的 dark mode 必须标记为 Proposed Dark Mapping。
```

应提供可访问的 Figma 文件或页面范围。只有截图时也可以执行，但估算值不能标记为 verified token。

### prd-to-admin-design

用于根据 `ADMIN_SPEC.md` 或 PRD，在已有 Figma 文件中创建或扩展后台页面。

示例：

```text
使用 prd-to-admin-design Skill。
读取 ADMIN_SPEC.md 和 DESIGN.md，在这个 Figma 文件中新增订单列表、订单详情和退款拒绝弹窗：<Figma URL>
复用现有侧边栏、Filter、Table、Badge、Drawer 和 Modal，不要创建平行组件系统。
```

建议同时提供目标 Figma 文件、要创建的 page/frame、现有设计系统位置，以及明确的模块范围。

### figma-to-admin-page

用于将指定 Figma frame/node 实现到现有 React、Vue 或其他后台 Web 项目中。

示例：

```text
使用 figma-to-admin-page Skill。
把这个 Figma frame 实现到当前 React 后台：<包含 node-id 的 Figma URL>
目标 route 是 /settings/users。
读取 DESIGN.md 和 ADMIN_SPEC.md，优先复用 DataTable、SearchInput、StatusBadge 和权限组件。
实现搜索、角色筛选、分页、批量禁用、编辑弹窗以及 loading、empty、error 状态。
```

必须提供可识别的 Figma frame/node 和目标前端项目。没有真实 API 时，应明确是交互 demo 还是等待后端接入。

### admin-ui-review

用于核对 PRD、`ADMIN_SPEC.md`、`DESIGN.md`、Figma 和代码之间的一致性。

只检查、不修改：

```text
使用 admin-ui-review Skill，只检查不要修改。
审查 /admin/orders/:id，对照 PRD.md、ADMIN_SPEC.md、DESIGN.md 和指定 Figma frame。
重点检查退款权限、金额格式、危险操作确认、表格密度和响应式布局。
```

检查并修复：

```text
使用 admin-ui-review Skill，检查并修复用户列表页。
先列出 Critical、Major 和 Minor 问题，再按严重程度修复并运行相关测试。
不要为无影响的 1px 差异重构整个页面。
```

仅说“检查”时默认是 review-only，不会修改代码或设计稿。

## 6. 推荐工作流

### 只有 PRD，只需要页面规格

```text
prd-to-admin-spec
```

停止点：`ADMIN_SPEC.md`。

### 已有 Figma，需要实现一个页面

```text
figma-to-admin-page
```

如果这套 Figma 还要作为后续多个页面的长期设计基准，可先执行：

```text
figma-to-design-md
-> figma-to-admin-page
```

### 从 PRD 完成完整模块

```text
admin-workflow

PRD
-> ADMIN_SPEC.md
-> DESIGN.md（已有参考 Figma 且需要长期复用时）
-> Figma pages
-> Frontend code
-> Review
```

### 上游需求发生变化

```text
使用 admin-workflow Skill，同步最新 PRD 中的退款状态和审批权限变更。
只更新实际受影响的 ADMIN_SPEC、Figma 页面、前端实现和 review 结果。
```

工作流会先判断影响范围，不会默认重跑整条链路。

## 7. 输入材料建议

材料越具体，执行越稳定：

| 材料 | 建议内容 |
|---|---|
| PRD | 业务目标、角色、流程、状态、权限、验收标准 |
| API / 数据模型 | 字段、枚举、分页、错误结构和权限能力 |
| ADMIN_SPEC.md | 稳定 Page ID、route、字段、操作、状态和追踪关系 |
| DESIGN.md | token、组件、布局、页面模式和代码映射 |
| Figma | 文件 URL、page、frame/node、组件库和目标视口 |
| 前端项目 | route、相似页面、共享组件、状态管理和测试命令 |

Figma 开发或审查任务应尽量提供带 `node-id` 的 URL。只给出“这个 Figma”但没有可识别目标时，Skill 会停止相关分支并要求补充，而不是凭空设计。

## 8. Artifact 关系

```text
PRD.md          = 产品需求真源
ADMIN_SPEC.md   = 后台信息架构与交互真源
DESIGN.md       = 跨页面设计系统真源
Figma           = 已批准页面的具体视觉真源
Code            = 实际交付行为
```

用户当前的明确说明优先。不同来源发生冲突时，应报告冲突两端并请求必要决定，不应让下游产物静默覆盖上游事实。

## 9. 更新与卸载

更新项目级 Skills：

```bash
npx skills update --project
```

更新用户级 Skills：

```bash
npx skills update --global
```

卸载项目级 Skill：

```bash
npx skills remove prd-to-admin-spec
```

卸载用户级 Skill：

```bash
npx skills remove prd-to-admin-spec --global
```

## 10. 参考

- [项目 README](README.md)
- [Agent Skills Specification](https://agentskills.io/specification)
- [`skills` CLI](https://github.com/vercel-labs/skills)
