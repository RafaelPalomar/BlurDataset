# BlurDataset
This is a test repository to blur a set of images using python pil

Test usage:
```bash
docker run -v /tmp/input_data:/tmp/input_data -v /tmp/output_data:/tmp/output_data -e INPUT_DATA_DIR=/tmp/input_data -e OUTPUT_DATA_DIR=/tmp/output_data blur
```