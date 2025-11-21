# SE-GPMS

这是一个毕业论文进度管理系统的示例仓库，包含前端（Vite + React + TypeScript）与后端（Django + Django REST framework）的最小实现。

## 快速启动（开发）

下面的步骤在 macOS 上测试通过。请在开始前确保已安装 `python3`, `node/npm`。

### 后端（Django）

1. 进入后端目录并创建虚拟环境：

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
```

2. 安装后端依赖：

```bash
pip install -r requirements.txt
```

3. 生成并应用数据库迁移（使用默认 sqlite3）：

```bash
python manage.py makemigrations users
python manage.py migrate
```

4. （可选）创建超级用户以访问 Django Admin：

```bash
python manage.py createsuperuser
```

5. 启动后端开发服务器：

```bash
python manage.py runserver 0.0.0.0:8000
```

后端 API 示例：

- 注册：`POST /api/auth/register/`，Body JSON：
	`{ "student_id": "学工号", "email": "a@b.com", "role": "student|teacher|admin", "password": "..." }`
- 登录：`POST /api/auth/login/`，Body JSON：
	`{ "identifier": "学工号或邮箱", "password": "..." }`，返回 `{ token, user }`
- 当前用户：`GET /api/auth/me/`，需要 `Authorization: Token <token>` 头。

> 注意：开发环境中 `CORS_ALLOWED_ORIGINS` 已为本地前端开发服务器配置。如需临时放宽，请在 `backend_project/settings.py` 中启用 `CORS_ALLOW_ALL_ORIGINS = True`（仅开发）。

### 前端（Vite + React）

1. 进入前端目录并安装依赖：

```bash
cd frontend
npm install
```

2. （可选）如果 TypeScript 编译提示缺少 React 类型，可安装：

```bash
npm install -D @types/react @types/react-dom
```

3. 启动开发服务器：

```bash
npm run dev
```

前端默认在 `http://localhost:5173` 运行。若你使用不同端口（如 `3000`），后端的 `CORS_ALLOWED_ORIGINS` 需相应包含该地址或设置为允许所有来源（仅限开发）。

登录流程说明：
- 登录页面会调用后端 `POST /api/auth/login/`，成功后把 `token` 保存到浏览器 `localStorage`（键名 `token`），并在后续请求中通过 `Authorization: Token <token>` 发送。

## 开发提示

- 若后端出现 `no such table` 错误，确认已运行 `manage.py migrate`。
- 推荐将虚拟环境、数据库文件与前端构建产物加入 `.gitignore`（仓库已有相应忽略规则）。
- 想把 token 存为更安全的 HttpOnly cookie 或改用 JWT，可在后端替换认证方案（示例已使用 DRF token 认证作为入门方案）。

如需我帮你：
- 添加管理员 API（修改用户角色）；
- 在前端实现自动登录（页面刷新时用 token 调用 `/api/auth/me/` 恢复用户）；
- 将后端 Docker 化或提供 production-ready 配置。
