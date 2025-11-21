# Backend (Django) — 最小示例

说明：此目录提供一个最小的 Django 后端骨架，包含注册与登录的 REST API（基于 Token）。

安装依赖（建议在虚拟环境中执行）：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

初始化并运行：

```bash
cd backend
python manage.py migrate
python manage.py createsuperuser  # 可选，用于 admin
python manage.py runserver 0.0.0.0:8000
```

API:
- `POST /api/auth/register/`  body: `{ "student_id": "学工号", "email": "a@b.com", "role": "student|teacher|admin", "password": "..." }` 返回 token 与用户信息
- `POST /api/auth/login/` body: `{ "identifier": "学工号或邮箱", "password": "..." }` 返回 token 与用户信息

说明：
- 学工号被保存在 `User.username` 字段中，`Profile.role` 保存角色。
- 这是一个开发样例；生产环境请做好安全设置、SECRET_KEY 管理、CORS 配置、以及使用 HTTPS。 
