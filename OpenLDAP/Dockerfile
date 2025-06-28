FROM debian:12-slim
RUN apt update && apt install -y slapd ldap-utils procps vim
COPY entrypoint /
COPY . /opt/ldap/
CMD ["/opt/ldap/entrypoint"]
