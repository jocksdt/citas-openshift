# Ejecución

```
docker run --name mysql -d -e MYSQL_ROOT_PASSWORD=asdasd mariadb
docker cp quotes.csv mysql:/tmp
docker cp quotes.sql mysql:/tmp
docker exec -it  mysql bash -c "mysql -uroot -pasdasd < /tmp/quotes.sql"
```


