路由：`figma-to-design-md` -> `figma-to-admin-page`，然后停止。

理由：目标 Figma frame 和现有 React 项目均可用，`ADMIN_SPEC.md` 已存在，可直接复用；但 `DESIGN.md` 缺失，且用户明确要求后续整个后台沿用这套设计，因此应先从该 Figma 提取可复用设计系统，再按目标 frame 实现用户管理页。无需执行 `prd-to-admin-spec`、`prd-to-admin-design` 或 `admin-ui-review`。
