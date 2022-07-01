# logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
log_base_path = f"{BASE_DIR}/../logs/"

Path(log_base_path).mkdir(parents=True, exist_ok=True)

logger_file_path = f'{log_base_path}logs.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'verbose': {
            'format': 'Level: {levelname} - Time: {asctime} - Name: {name} - Message: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },

        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': logger_file_path,
            'when': 'midnight',
            'backupCount': 10,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['django.server', 'file', 'console'],
            'level': 'DEBUG',
        },
    }, "root": {
        "level": "DEBUG",
        "handlers": ["console", 'file', ],
    }

}
