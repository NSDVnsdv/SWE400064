FROM python:3.12-slim

WORKDIR /app

COPY analyze.py .

# Run as a non-root user (Docker security best practice)
RUN useradd --create-home appuser && \
    mkdir -p /data/input /data/output && \
    chown -R appuser:appuser /app /data
USER appuser

# Document the expected mount points for input/output data
VOLUME ["/data/input", "/data/output"]

ENTRYPOINT ["python", "analyze.py"]
CMD ["--input", "/data/input/input.txt", "--output", "/data/output/report.txt", "--top", "10"]
