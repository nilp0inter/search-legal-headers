FROM python:3-alpine
COPY search-legal-headers.py /usr/local/bin/search-legal-headers
CMD ["search-legal-headers"]
