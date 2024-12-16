from cerebras.modelzoo.common.run_utils import run
from cerebras.modelzoo.models import create_model
from cerebras.modelzoo.datasets import create_data_loader

# Define Model
def forecasting_model():
    model = create_model("transformer_climate_forecaster", pretrained=True)
    return model

# Define Data Loader
def forecasting_data_loader():
    data_loader = create_data_loader("climate_forecasting_dataset", split="train")
    return data_loader

if __name__ == "__main__":
    run(model_fn=forecasting_model, data_loader_fn=forecasting_data_loader)
