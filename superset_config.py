# superset_config.py
# Configuration Superset pour utiliser PostgreSQL

import os

# Base de données PostgreSQL pour les métadonnées
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://bi_user:bi_password123@postgres:5432/superset')

# Configuration Redis (cache)
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

# Cache
CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': 1,
}

# Data cache
DATA_CACHE_CONFIG = CACHE_CONFIG

# Secret key
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY', 'CHANGE_ME_TO_A_COMPLEX_RANDOM_SECRET')

# Désactiver les exemples
SUPERSET_LOAD_EXAMPLES = False

# Feature flags
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}
