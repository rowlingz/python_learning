echo 'kill django server...'
sudo kill -9 8996
sleep 1 
echo 'killed'

echo 'start server'
python manage.py runserver 127.0.0.1:8000
echo 'started!!'
