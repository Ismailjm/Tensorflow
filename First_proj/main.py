import tensorflow as tf

print("TensorFlow version:", tf.__version__)

# Check if GPU support is available
if tf.test.is_built_with_cuda():
    print("TensorFlow is installed with GPU support")
else:
    print("TensorFlow is installed with CPU support")
