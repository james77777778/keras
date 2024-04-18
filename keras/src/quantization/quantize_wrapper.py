from keras.src.layers.core.wrapper import Wrapper
from keras.src.models import Model


class QuantizeWrapper(Wrapper):
    def __init__(self, layer, quantize_config, **kwargs):
        kwargs["name"] = f"quantized_{layer.name}"
        super().__init__(layer, **kwargs)

        if isinstance(layer, Model):
            raise TypeError(
                "`layer` cannot be a `Model` instance. "
                f"Received: layer={layer} of the type {type(layer)}"
            )

    def build(self, input_shape):
        super().build(input_shape)

        # TODO: Add weight quantizer variables
        # TODO: Add activation quantizer variables
