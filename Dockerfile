FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
# FROM python:3.14-rc
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

ENV UV_INDEX_URL=https://mirrors.tencentyun.com/pypi/simple

COPY . /app
RUN uv lock
RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"

# RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# RUN pip install uv
# RUN pip install --upgrade pip
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY pyproject.toml .
# RUN uv sync
# COPY . .

# RUN source .venv/bin/activate

# CMD ["uv", "tree"]

# CMD ["ls"]
EXPOSE 9099

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9099", "--log-config=log_conf.json", "--log-level", "trace", "--use-colors"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9099", "--log-level", "trace", "--use-colors"]