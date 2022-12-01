FROM alpine:latest
RUN apk add python3;
COPY state.json /run/runc/container/state.json
COPY runc_ver.py /usr/local/bin/ps
ENTRYPOINT [ "/proc/self/exe", "ps", "container" ]