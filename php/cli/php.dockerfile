FROM php:8-cli-alpine3.17
 
WORKDIR /var/app-cli

CMD [ "php", "cli.php" ]