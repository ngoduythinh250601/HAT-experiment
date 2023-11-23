If you want to use MixLosses loss function, copy the file `mixlosses_loss.py` into the package named `basicsr`. 
For example, the directory path containing the basicsr package is: 

`C:/Users/Username/AppData/Local/Programs/Python/Python311/Lib/site-packages/basicsr/losses/`.

Then, open the `__init__.py` file in that folder and add the line 

```from .mixlosses_loss import PerceptualLoss_L1Loss```

Now, you can use MixLosses loss function to train the model. You can refer to

`../options/train/train_HAT-S_SRx4_MixLosses_finetune_from_DIV2K_pretrain.yml`.