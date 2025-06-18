# Використовуємо базовий образ Bitnami PyTorch
FROM bitnami/pytorch:2.3.1

# Переходимо на root для встановлення системних бібліотек
USER root

# Встановлюємо libGL для OpenCV
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Повертаємось до стандартного користувача Bitnami
USER 1001

# Створюємо директорію для кешу WANDB
RUN mkdir -p /app/.cache/wandb
ENV WANDB_CACHE_DIR=/app/.cache/wandb

# Створюємо директорію для моделі
RUN mkdir -p /app/model

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо необхідні файли
COPY requirements.txt requirements.txt
COPY download_model.py download_model.py
COPY main.py main.py
COPY start.sh start.sh

# Встановлюємо залежності
RUN pip install -r requirements.txt

# Додатково видаляємо стандартний entrypoint Bitnami, якщо це необхідно
RUN rm /opt/bitnami/scripts/pytorch/entrypoint.sh

# Встановлюємо entrypoint на start.sh
ENTRYPOINT ["./start.sh"]
