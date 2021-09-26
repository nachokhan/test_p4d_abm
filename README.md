# test_p4d_abm

# Setup
## Install requirements
pip install -r requirements.txt
## Create configuration files
for i in $(find . -name '*._sample'); do cp "$i" "${i%.*}"; done;

## Install Docker Postgress
### Pull Docker Postgress image
sudo docker pull postgres:latest
### Run docker image
For running this the file called exactly docker-compose.yml should exist.
sudo docker-compose up
### Dump DB into docker volume
#### Enter the container's bash.
sudo docker exec -it pg_container_pix4d_test bash
#### Connect to psql terminal
psql -h pg_container_pix4d_test -d pix4d_test -U root
#### Dump the data file in the dB
psql -h pg_container_pix4d_test -d pix4d_test -U root -f infile




# DATABASE 
## Connect to the database
### Enter the container's bash.
sudo docker exec -it pg_container_pix4d_test bash
### Connect to psql terminalk
psql -h pg_container_pix4d_test -d pix4d_test -U root
### Dump the data file in the dB
psql -h pg_container_pix4d_test -d pix4d_test -U root -f infile







# Usefull commands

## Docker
### List volumes
sudo docker volume ls
### Remove volume
sudo docker volume rm -f <name>
If this gives error, should also remove the associated container: the long ID between brackets: [xxxxxxxxxxx]
### Remove container
sudo docker rm <id>

## BASH
### Check open port
sudo lsof -i -P | grep ':5432 '  (1 = Closed, 0=Opened)
### Close port
sudo kill <pid>