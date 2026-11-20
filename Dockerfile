FROM python:3.12-slim
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}
WORKDIR /app
COPY dist ./dist
RUN pip install --no-cache-dir dist/*.whl gunicorn
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "leavetracker.main:app"]