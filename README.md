# Simulated garment dataset for virtual try-on

This repository contains the dataset used in the following papers:
- Self-Supervised Collision Handling via Generative 3D Garment Models for Virtual Try-On **(CVPR 2021)** [[Project website](http://mslab.es/projects/SelfSupervisedGarmentCollisions/)] [[Video](https://youtu.be/9AnBNco6i2U)]

- Learning-Based Animation of Clothing for Virtual Try-On **(Eurographics 2019)** [[Project website](https://dancasas.github.io/projects/LearningBasedVirtualTryOn/)] [[Video](https://youtu.be/o2KJoAhEGg8)]

## Dataset

![Teaser](teaser.gif "Teaser image")

The data is generated used a modified version of [ARCSim](http://graphics.berkeley.edu/resources/ARCSim/) and sequences from the [CMU Motion Capture Database](http://mocap.cs.cmu.edu/) converted to SMPL format in [SURREAL](https://www.di.ens.fr/willow/research/surreal/data/). Each simulated sequence is stored as a ```.pkl``` file that contains the following data:

| Key      | Description                        | Dimension                     |
|----------|------------------------------------|-------------------------------|
| *shapes*   | SMPL shape coefficients            | [num_frames, 10]              |
| *poses*    | SMPL pose coefficients             | [num_frames, 75]              |
| *vertices* | Vertices of the simulated garment  | [num_frames, num_vertices, 3] |
| *faces*    | Faces of the garment           |      [num_faces, 3]               |
| *sequence*      | Sequence identifier           |                  |
| *subject*       | Subject identifier            |    |
| *conf* | ARCSim configuration | 

## Extract meshes
**Requirements**: ```python3```, ```numpy-1.21.3```

To extract the simulated garment meshes as ```.obj``` run the following script:
```
python extract_meshes.py tshirt/simulations/tshirt_shape00_01_01.pkl
```

## Citation

If you find this dataset useful please cite our work:

```
@article {santesteban2021garmentcollisions,
    journal = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    title = {{Self-Supervised Collision Handling via Generative 3D Garment Models for Virtual Try-On}},
    author = {Santesteban, Igor and Thuerey, Nils and Otaduy, Miguel A and Casas, Dan},
    year = {2021}
}
```

```
@article {santesteban2019virtualtryon,
    journal = {Computer Graphics Forum (Proc. Eurographics)},
    title = {{Learning-Based Animation of Clothing for Virtual Try-On}},
    author = {Santesteban, Igor and Otaduy, Miguel A. and Casas, Dan},
    year = {2019},
    ISSN = {1467-8659},
    DOI = {10.1111/cgf.13643}
}
```
