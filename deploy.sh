echo 'Start venv'
source ./.venv/bin/activate
echo 'Done...'

echo 'Make migrations'
python manage.py makemigrations

echo 'migrate'
python manage.py migrate
echo 'Migrate done...'

echo 'Running npm build'
npm run build
echo 'Done...'

echo 'Format index.html as Jinja template'
python format_index_html.py
echo 'Done...'

echo 'Collect static'
python manage.py collectstatic --noinput
echo 'Done...'

export PORT=8000
echo 'Server runnning on port ' $PORT
python manage.py runserver
