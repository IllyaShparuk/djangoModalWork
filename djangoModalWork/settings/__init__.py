from .base import *
import os


if os.environ.get('ENV_NAME') == 'Production':  # Для Deploy задаємо ENV_NAME як Production для доступу до production.py
    from .production import *
else:  # Інакше отримуємо всі значення з local.py
    from .local import *
