IN=$(echo $(sudo lsof -i -P | grep ':5432 ') | tr " " "\n")
arrIN=(${IN//;/ })
sudo kill -9 ${arrIN[1]}
sudo docker-compose up