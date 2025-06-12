from boltz.main import predict
import yaml
import json
from fastapi import FastAPI, HTTPException
from tempfile import TemporaryDirectory
from pathlib import Path

app = FastAPI()

@app.post("/predict")
def get_prediction(json_data: dict) -> dict:
    """
    Endpoint to get predictions from the Boltz server.
    """
    try:
        with TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            # Save the input JSON to a temporary yaml file
            input_yaml_file = tmpdir_path / "input.yaml"
            with open(input_yaml_file, 'w') as file:
                yaml.dump(json_data, file)
            # Call the predict function from boltz.main
            predict.callback(
                data = input_yaml_file,
                out_dir = tmpdir_path,
                use_msa_server = True
            )
            print(*tmpdir_path.glob("*"), sep="\n")

            # Read the output (boltz_results_input/predictions/input) from the temporary directory
            results_path = tmpdir_path / "boltz_results_input" / "predictions" / "input"
            if not results_path.exists():
                raise HTTPException(status_code=500, detail="Prediction results not found.")
            with open(results_path / "confidence_input_model_0.json", 'r') as file:
                confidence = json.load(file)
            if (affinity_path := results_path / "affinity_input.json").exists():
                with open(affinity_path, 'r') as file:
                    affinity = json.load(file)
            else:
                affinity = None
            with open(results_path / "input_model_0.cif", 'r') as file:
                structure = file.read()
            
        # Return the results as a dict
        results = {
            "confidence": confidence,
            "structure": structure
        }
        if affinity is not None:
            results["affinity"] = affinity
        return results

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Prediction task failed: {str(e)}")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=18000)