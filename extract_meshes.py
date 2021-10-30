import argparse
import pickle
import os


def save_obj(filename, vertices, faces):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as fp:
        for v in vertices:
            fp.write('v %f %f %f\n' % (v[0], v[1], v[2]))

        for f in (faces + 1):  # Faces are 1-based, not 0-based in obj files
            fp.write('f %d %d %d\n' % (f[0], f[1], f[2]))
    
    print("Saved:", filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extract meshes from .pkl and save as .obj'
    )

    parser.add_argument(
        'data_path',
        type=str,
        help='path to the .pkl file that contains the simulation data'
    )

    args = parser.parse_args()

    assert os.path.exists(args.data_path), "File not found"

    with open(args.data_path, "rb") as f:
        data = pickle.load(f)

        export_dir = f"tshirt/meshes/{data['subject']}/{data['sequence']}"
        os.makedirs(export_dir, exist_ok=True)

        num_frames = data['vertices'].shape[0]
        for frame in range(num_frames):
            save_obj(
                filename=os.path.join(export_dir, f"{frame:04d}_garment.obj"),
                vertices=data['vertices'][frame],
                faces=data['faces']
            )
