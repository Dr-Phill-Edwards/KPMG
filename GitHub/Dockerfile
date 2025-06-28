FROM alpine:latest
RUN apk update && apk add git openssh
RUN adduser -D git && passwd -u git
RUN ssh-keygen -A
WORKDIR /home/git
RUN mkdir -m 700 .ssh
COPY id_rsa.pub .ssh/authorized_keys
RUN chown -R git:git .ssh
ENV GIT_REPOSITORIES_PATH=/home/git
USER git
RUN git config --global init.defaultBranch master
RUN mkdir ticar && cd ticar && git init --bare
USER root
CMD ["/usr/sbin/sshd", "-D"]

