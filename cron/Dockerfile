FROM alpine:latest

# Install cron
RUN apk --no-cache add busybox

# Add your cron job file
ADD cronjob /etc/crontabs/root

# Start cron when the container starts
CMD ["crond", "-f", "-d", "8"]