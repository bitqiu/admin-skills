路由决定：仅执行 `prd-to-admin-spec`，读取根目录 `PRD.md` 并整理后台页面规格，产出 `ADMIN_SPEC.md` 后立即停止。

理由：当前缺少页面规格，而用户明确只需要页面规格；因此不进入 `prd-to-admin-design`、`figma-to-design-md`、`figma-to-admin-page` 或 `admin-ui-review`，也不创建 Figma、不编写前端代码。
