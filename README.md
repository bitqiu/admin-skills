# Admin UI Skills

一组用于 B2B 后台管理系统需求、设计、开发和验收的 Agent Skills，可安装到 `npx skills` 支持的多种 AI 工具。

项目将产品需求、页面规格、设计系统、Figma 和代码拆成各自可追踪的产物，避免不同阶段重复推导业务规则或重新创建组件。

完整的安装、调用和场景示例见 [使用说明](USAGE.md)。

## 快速开始

这是 Skill 的源码与分发仓库，`skills/` 不是业务项目中的自动发现目录。请使用 [`skills`](https://www.npmjs.com/package/skills) CLI 安装。

交互式选择 Skill、AI 工具和安装范围：

```bash
npx skills add bitqiu/admin-skills
```

将全部 Skills 安装到当前项目中所有受支持的 AI 工具：

```bash
npx skills add bitqiu/admin-skills --all
```

追加 `--global` 可改为用户级安装。完整选项、单 Skill 安装和更新方式见 [使用说明](USAGE.md)。

可以直接描述最终目标，让 `admin-workflow` 选择最短路径：

```text
使用 admin-workflow Skill，根据 PRD 和现有 Figma 完成用户管理模块的设计与前端实现。
```

也可以显式调用单个 Skill，在指定产物完成后停止：

```text
使用 prd-to-admin-spec Skill，读取 PRD.md 并生成 ADMIN_SPEC.md。不要创建 Figma 或修改前端代码。
```

## Skills

| Skill | 职责 | 典型产物 |
|---|---|---|
| [`admin-workflow`](skills/admin-workflow/SKILL.md) | 检测现有产物并编排最短有效路径 | 路由、阶段执行结果 |
| [`prd-to-admin-spec`](skills/prd-to-admin-spec/SKILL.md) | 将需求证据整理为后台信息架构和交互规格 | `ADMIN_SPEC.md` |
| [`figma-to-design-md`](skills/figma-to-design-md/SKILL.md) | 从 Figma 提取可实现的设计系统 | `DESIGN.md`、明暗预览 |
| [`prd-to-admin-design`](skills/prd-to-admin-design/SKILL.md) | 根据规格和设计系统创建后台 Figma 页面 | Figma pages / frames |
| [`figma-to-admin-page`](skills/figma-to-admin-page/SKILL.md) | 在现有 React、Vue 等项目中实现指定 Figma 页面 | 前端 route、组件和测试 |
| [`admin-ui-review`](skills/admin-ui-review/SKILL.md) | 审查需求、设计系统、Figma 和代码的一致性 | Findings，或明确要求的修复 |

## 工作流

完整交付的依赖关系是：

```text
PRD.md
  -> ADMIN_SPEC.md
  -> Figma page
  -> Frontend code
  -> Review

Existing Figma
  -> DESIGN.md
  -> Figma page / Frontend code / Review
```

`admin-workflow` 会根据目标和现有产物删除不必要的阶段。例如：

- 只整理页面规格：`prd-to-admin-spec`
- 已有规格，继续设计：`prd-to-admin-design`
- 已有 Figma，建立长期设计基准：`figma-to-design-md`
- 已有 Figma 和前端项目：`figma-to-admin-page`
- 只检查现有实现：`admin-ui-review`

存在直接产物依赖的阶段按顺序执行。稳定且仍适用的产物会被复用，不会为了走完整流程而重复生成。

## Artifact 边界

| Artifact | 负责决定 |
|---|---|
| `PRD.md` | 产品目标、业务规则和验收要求 |
| `ADMIN_SPEC.md` | 后台模块、页面、字段、操作、权限和状态 |
| `DESIGN.md` | 跨页面 token、组件、布局和交互规则 |
| Figma | 已批准页面的具体视觉和交互表达 |
| Code | 实际交付行为和工程实现 |

用户当前的明确要求高于上述默认边界。发现来源冲突时应报告冲突，不应让下游产物静默改写上游事实。

## 项目结构

```text
skills/
├── admin-workflow/
├── prd-to-admin-spec/
├── figma-to-design-md/
├── prd-to-admin-design/
├── figma-to-admin-page/
└── admin-ui-review/
scripts/
└── validate_repo.py
tests/
└── test_validate_output.py
```

每个 Skill 以 `SKILL.md` 为入口，可按需包含：

- `agents/openai.yaml`：桌面端展示和默认提示
- `references/`：仅在对应工作模式下读取的详细规则
- `scripts/`：需要确定性执行的辅助工具
- `evals/evals.json`：用于行为评测的代表性请求

## 验证

运行仓库结构与元数据检查：

```bash
python3 scripts/validate_repo.py
```

运行确定性单元测试：

```bash
python3 -m unittest discover -s tests -v
```

## 维护原则

- 每个 Skill 只拥有一个明确阶段，避免互相复制完整 instructions。
- `description` 保持简短且可区分，关键触发场景放在开头。
- 条件性细节放入 `references/`，并从 `SKILL.md` 明确说明何时读取。
- 新增或修复行为时补充可观察的 eval expectation；不要只匹配固定措辞。
- 修改脚本后运行正例、反例和边界测试。
- 不把示例 Figma URL、推测的业务规则或不可访问的外部产物当作已验证事实。

格式规范参见 [Agent Skills Specification](https://agentskills.io/specification)，安装工具参见 [`skills` CLI](https://github.com/vercel-labs/skills)。
