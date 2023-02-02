FROM php:7.2-cli
 
WORKDIR /var/app-cli

CMD [ "php", "cli.php" ]