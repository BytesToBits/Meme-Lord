source venv/bin/activate
while (true) do
git pull
poetry install
poetry run python3 main.py
echo "Bot stopped, restarting in 5 seconds..."
done
