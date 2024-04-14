# StreamDeploy LLM App Scaffold

This repo contains a pre-architected, production-ready LLM application that may be easily deployed to cloud thanks tothe independent containers used for the frontend, backend, and LLM service [Ollama](https://github.com/ollama/ollama).

Run the following from the root of the llm-app-scaffold directory:

```
docker-compose up --build
```

To use a model from Ollama, run Ollama pull. For example, to use mistral, run the following:
```
ollama pull mistral
```
then run the docker compose command


![LLM Application Scaffold Screenshot](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/781/172/datas/original.jpeg)

