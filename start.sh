if [[ "$OSTYPE" =~ ^linux ]]; then
    python3 main.py
fi

if [[ "$OSTYPE" =- ^win32 ]]; then
    python main.py
fi