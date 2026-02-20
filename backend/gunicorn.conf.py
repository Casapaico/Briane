"""
Gunicorn configuration — Briane production server
"""
import multiprocessing

# ── Bind ──────────────────────────────────────────────────────────────────────
# Unix socket es más rápido que TCP para comunicación local con Nginx
bind = "unix:/run/briane/gunicorn.sock"

# ── Workers ───────────────────────────────────────────────────────────────────
# Fórmula recomendada: (2 × CPUs) + 1
# Ajustar si el servidor está dedicado al 100% a este servicio
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
threads = 2          # hilos por worker para peticiones concurrentes ligeras

# ── Timeouts ──────────────────────────────────────────────────────────────────
timeout      = 120   # segundos antes de matar un worker bloqueado
keepalive    = 5     # segundos que el socket se mantiene abierto (keep-alive HTTP)
graceful_timeout = 30  # segundos para que los workers terminen sus requests al reiniciar

# ── Proceso ───────────────────────────────────────────────────────────────────
proc_name    = "briane_gunicorn"
preload_app  = True  # carga la app una vez en el master → fork() → workers más rápidos y menor RAM

# ── Logging ───────────────────────────────────────────────────────────────────
accesslog = "/var/log/briane/access.log"
errorlog  = "/var/log/briane/error.log"
loglevel  = "info"
access_log_format = (
    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s '
    '"%(f)s" "%(a)s" %(D)sµs'
)

# ── Seguridad ─────────────────────────────────────────────────────────────────
limit_request_line   = 4094
limit_request_fields = 100
forwarded_allow_ips  = "127.0.0.1"   # confiar solo en Nginx local

# ── Systemd integration ───────────────────────────────────────────────────────
# Gunicorn 20+ notifica a systemd automáticamente cuando los workers están listos
# Compatible con Type=notify en el archivo .service
