FROM alpine:latest

RUN apk --no-cache add busybox
RUN apk add docker-cli

ADD cronjob /etc/crontabs/root

# Start cron when the container starts
CMD ["crond", "-f", "-d", "8"]