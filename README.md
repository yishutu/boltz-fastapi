# `boltz-fastapi`: FastAPI Interface for Boltz-2

Links:
* Boltz-2: https://github.com/jwohlwend/boltz

Installation:
```
docker build -t boltz-fastapi .
```

Running:
```
docker run -d -p 18000:18000 --gpus all --shm-size 1g boltz-fastapi
```

After that, you may POST json data to http://localhost:18000/predict to do the Boltz-2 prediction.
For the information required, see https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md as the YAML part for the properties required.
The MSA server option has been turned on.