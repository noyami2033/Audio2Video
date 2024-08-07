# Audio2Video
A simplified audio to video repo based on SadTalker : https://github.com/OpenTalker/SadTalker

## Usage (This repository is only tested on macOS cpu and AWS ubuntu cpu)
1. Download checkpoint file from [google drive](https://drive.google.com/file/d/1gwWh45pF7aelNP_P78uDJL8Sycep-K7j/view) or [github](https://github.com/OpenTalker/SadTalker/releases), put them into the checkpoints folder. Make sure all the 4 files are downloaded: checkpoints/mapping_00109-model.pth.tar, checkpoints/mapping_00229-model.pth.tar, checkpoints/SadTalker_V0.0.2_256.safetensors, checkpoints/SadTalker_V0.0.2_512.safetensors.
2. Make sure docker compose is available, ```cd Audio2Video```, then ```docker compose up```. (The input image/audio path and output video path can be set in ```entry_point.sh``` or ```processing.py```. Directly using ```docker compose run``` to set the path is not suggested because the original docker image already has an entry point).


## About this task:
1. The target class is in the ```Audio2Video.py``` file, named ```Audio2Video```.
2. Only the required files for runing ```Audio2Video.py``` are kept, other files are removed.
3. The ```generate``` function in this class can process one specified audio and one specified image to a specified video.
4. Input image format could be ```'jpg', 'png', 'jpeg'```, input audio format could be ```'wav', 'wave'``` and output video format is required to be ```mp4``` (file formats will be checked in code).
5. The ```processing.py``` file gives an example about how to use this class and generate function.
6. The docker image used ```wawa9000/sadtalker``` which is recommended by the original sadtalker repo.
7. Other settings can be changed in ```Audio2Video``` class if needed.
