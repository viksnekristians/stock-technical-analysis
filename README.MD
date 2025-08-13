chmod +x wait-for-it.sh
docker compose up --build

Currently manually:
python manage.py migrate

to enable ai features  (?):
docker exec -it ollama ollama pull llama3
