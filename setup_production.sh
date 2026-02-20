#!/usr/bin/env bash
# =============================================================================
# setup_production.sh  —  Briane production stack installer
# Ejecutar como: sudo bash setup_production.sh
# =============================================================================
set -euo pipefail

APP_USER="alex"
APP_DIR="/home/alex/Briane/backend"
VENV="$APP_DIR/venv"

echo "==> [1/6] Instalando Nginx..."
apt-get install -y nginx

echo "==> [2/6] Creando directorio de logs..."
mkdir -p /var/log/briane
chown "$APP_USER:$APP_USER" /var/log/briane

echo "==> [3/6] Instalando servicio systemd para Gunicorn..."
cat > /etc/systemd/system/briane.service << 'EOF'
[Unit]
Description=Briane – Gunicorn WSGI Application Server
Documentation=https://gunicorn.org
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=notify
NotifyAccess=all
User=alex
Group=alex
WorkingDirectory=/home/alex/Briane/backend
EnvironmentFile=/home/alex/Briane/backend/.env

# Crea /run/briane/ automáticamente en cada arranque (tmpfs)
RuntimeDirectory=briane
RuntimeDirectoryMode=0755

ExecStart=/home/alex/Briane/backend/venv/bin/gunicorn \
    --config /home/alex/Briane/backend/gunicorn.conf.py \
    briane_backend.wsgi:application

# Recarga graceful con: sudo systemctl reload briane
ExecReload=/bin/kill -s HUP $MAINPID

KillMode=mixed
TimeoutStopSec=30

# Reinicio automático si el proceso cae
Restart=on-failure
RestartSec=5
StartLimitIntervalSec=60
StartLimitBurst=5

[Install]
WantedBy=multi-user.target
EOF

echo "==> [4/6] Configurando Nginx (reverse proxy)..."
cat > /etc/nginx/sites-available/briane << 'EOF'
# ─── Upstream: Gunicorn via Unix socket ───────────────────────────────────────
upstream briane_app {
    server unix:/run/briane/gunicorn.sock fail_timeout=0;
}

# ─── Servidor HTTP ────────────────────────────────────────────────────────────
server {
    listen 80;
    listen [::]:80;
    server_name _;            # Cambiar por el dominio real: server_name briane.com www.briane.com;

    client_max_body_size 20M; # Para subir CVs y archivos

    # ── Gzip ────────────────────────────────────────────────────────────────
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types
        text/plain text/css text/xml application/json
        application/javascript application/xml+rss
        application/atom+xml image/svg+xml;

    # ── Archivos estáticos — servidos por Nginx directamente (sin Python) ──
    location /static/ {
        alias /home/alex/Briane/backend/staticfiles/;
        expires 1y;
        add_header Cache-Control "public, immutable";
        access_log off;
    }

    # ── Archivos multimedia (CVs, imágenes) ─────────────────────────────────
    location /media/ {
        alias /home/alex/Briane/backend/media/;
        expires 6M;
        add_header Cache-Control "public";
        access_log off;
    }

    # ── Django / Gunicorn ────────────────────────────────────────────────────
    location / {
        proxy_pass         http://briane_app;
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
        proxy_redirect     off;

        proxy_connect_timeout  10s;
        proxy_send_timeout    120s;
        proxy_read_timeout    120s;

        # Buffering: Nginx absorbe la respuesta completa antes de enviarla
        # al cliente lento, liberando al worker de Gunicorn más rápido
        proxy_buffering    on;
        proxy_buffer_size  16k;
        proxy_buffers      8 16k;
    }

    # ── Logs ────────────────────────────────────────────────────────────────
    access_log /var/log/nginx/briane_access.log;
    error_log  /var/log/nginx/briane_error.log warn;
}

# ─── HTTPS (descomentar cuando tengas certificado SSL) ────────────────────────
# server {
#     listen 443 ssl http2;
#     listen [::]:443 ssl http2;
#     server_name briane.com www.briane.com;
#
#     ssl_certificate     /etc/letsencrypt/live/briane.com/fullchain.pem;
#     ssl_certificate_key /etc/letsencrypt/live/briane.com/privkey.pem;
#     ssl_protocols       TLSv1.2 TLSv1.3;
#     ssl_ciphers         ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:...;
#     ssl_prefer_server_ciphers off;
#     ssl_session_cache   shared:SSL:10m;
#     ssl_session_timeout 10m;
#
#     add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
#
#     # El resto del config de locations va aquí igual que en HTTP
# }
#
# # Redirigir HTTP → HTTPS
# server {
#     listen 80;
#     server_name briane.com www.briane.com;
#     return 301 https://$host$request_uri;
# }
EOF

# Activar el site y deshabilitar el default
ln -sf /etc/nginx/sites-available/briane /etc/nginx/sites-enabled/briane
rm -f /etc/nginx/sites-enabled/default

echo "==> [5/6] Verificando config de Nginx..."
nginx -t

echo "==> [6/6] Habilitando e iniciando servicios..."
systemctl daemon-reload
systemctl enable briane
systemctl enable nginx
systemctl restart briane
systemctl reload nginx

echo ""
echo "============================================================"
echo "  Briane production stack instalado correctamente"
echo "============================================================"
echo "  Gunicorn: sudo systemctl status briane"
echo "  Nginx:    sudo systemctl status nginx"
echo "  Logs app: tail -f /var/log/briane/error.log"
echo "  Logs web: tail -f /var/log/nginx/briane_access.log"
echo ""
echo "  Recarga graceful (sin downtime):"
echo "    sudo systemctl reload briane"
echo "============================================================"
