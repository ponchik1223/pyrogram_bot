docker-compose up -d 
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
alembic upgrade head
python3 main
