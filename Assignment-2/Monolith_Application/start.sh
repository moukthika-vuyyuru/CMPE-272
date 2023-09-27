apt-get update
apt-get -y install redis-server
redis-server &
python app.py