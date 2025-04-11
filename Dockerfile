FROM public.ecr.aws/docker/library/python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir flask
COPY app.py .
EXPOSE 80
CMD ["python", "app.py"]