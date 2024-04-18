# Support QAT for Keras

## TODO

- [ ] Add Quantizers (LastValue, MovingAverage, No)
- [ ] Add QuantizeWrapper
- [ ] Add GraphTransformer
- [ ] Add example of QAT for simple CNN (Conv2D + BN + ReLU)

## References

- [TFMOT, default_8bit](https://github.com/tensorflow/model-optimization/tree/master/tensorflow_model_optimization/python/core/quantization/keras/default_8bit)
- [TFMOT, Quantizers](https://github.com/tensorflow/model-optimization/blob/master/tensorflow_model_optimization/python/core/quantization/keras/quantizers.py)
- [TFMOT, QuantizeWrapper](https://github.com/tensorflow/model-optimization/blob/master/tensorflow_model_optimization/python/core/quantization/keras/quantize_wrapper.py)
- [TFMOT, QuantizeAwareActivation](https://github.com/tensorflow/model-optimization/blob/master/tensorflow_model_optimization/python/core/quantization/keras/quantize_aware_activation.py)
- [TFMOT, Default8BitQuantizeConfig](https://github.com/tensorflow/model-optimization/blob/master/tensorflow_model_optimization/python/core/quantization/keras/default_8bit/default_8bit_quantize_registry.py#L286)
- [TFMOT, Transform](https://github.com/tensorflow/model-optimization/blob/master/tensorflow_model_optimization/python/core/quantization/keras/graph_transformations/transforms.py#L156)
