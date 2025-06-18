import os
import wandb

wandb.require("core")

wandb_api_key = os.getenv("WANDB_API_KEY")
wandb.login(key=wandb_api_key)

run = wandb.init()

artifact = run.use_artifact('r-dovbeta-set-university-org/wandb-registry-model/locally-created:v0', type='model')
path = artifact.get_path("best.pt")
path.download('./model/')