#!/bin/bash
set -e

echo "Starting Ollama..."
ollama serve > /tmp/ollama.log 2>&1 &

sleep 8

echo "Pulling model: $OLLAMA_MODEL"
ollama pull "$OLLAMA_MODEL"

echo "Starting Streamlit..."
streamlit run app.py --server.port 7860 --server.address 0.0.0.0