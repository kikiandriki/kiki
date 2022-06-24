ARG VERSION="0.1.0"

FROM --platform=amd64 python:3.10-slim
ARG VERSION

LABEL org.opencontainers.image.authors "matootie <matootie@icloud.com>"
LABEL org.opencontainers.image.url "https://github.com/kikiandriki/kiki#readme"
LABEL org.opencontainers.image.documentation "https://github.com/kikiandriki/kiki/wiki"
LABEL org.opencontainers.image.source "https://github.com/kikiandriki/kiki.git"
LABEL org.opencontainers.image.vendor "Kiki & Riki"
LABEL org.opencontainers.image.title "Kiki"
LABEL org.opencontainers.image.description "The official companion chat bot for the Kiki & Riki Discord server. Kiki helps power Discord integrations on the Kiki & Riki platform."

WORKDIR /app
COPY \
  dist/kiki-${VERSION}-py3-none-any.whl \
  /app/kiki-${VERSION}-py3-none-any.whl
RUN pip install /app/kiki-${VERSION}-py3-none-any.whl
CMD ["kiki"]
