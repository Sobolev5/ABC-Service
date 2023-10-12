FROM python:3.11.2-buster as base
RUN echo "alias rm='rm -i'" >> ~/.bashrc && \
    echo "alias cp='cp -i'" >> ~/.bashrc && \
    echo "alias mv='mv -i'" >> ~/.bashrc && \
    echo "alias ls='ls --color=auto'" >> ~/.bashrc && \
    echo "alias ll='ls -la'" >> ~/.bashrc && \
    echo "alias grep='grep --color=auto'" >> ~/.bashrc && \
    echo "alias egrep='egrep --color=auto'" >> ~/.bashrc && \
    echo "alias fgrep='fgrep --color=auto'" >> ~/.bashrc && \
    echo "alias ports='netstat -tulanp'" >> ~/.bashrc && \
    echo "alias df='df -H'" >> ~/.bashrc && \
    echo "alias du='du -ch'" >> ~/.bashrc
RUN pip install poetry==1.1.12
COPY poetry.lock pyproject.toml /app/
RUN poetry export -o requirements.txt

FROM base as build
COPY --from=base /app/requirements.txt /tmp/requirements.txt
RUN python -m venv .venv && .venv/bin/pip install -r /tmp/requirements.txt

FROM build as prod
CMD uvicorn main:app --reload --host 0.0.0.0 --port 11022

