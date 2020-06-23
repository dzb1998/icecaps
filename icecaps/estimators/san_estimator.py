import tensorflow as tf
import copy
import random
from collections import OrderedDict

from icecaps.estimators.estimator_group import EstimatorGroup
from icecaps.estimators.estimator_chain import EstimatorChain
from icecaps.estimators.san_encoder_estimator import SanEncoderEstimator
from icecaps.estimators.san_decoder_estimator import SanDecoderEstimator
from icecaps.estimators.noise_layer import NoiseLayer
from icecaps.estimators.abstract_icecaps_estimator import AbstractIcecapsEstimator
from icecaps.estimators.abstract_recurrent_estimator import AbstractRecurrentEstimator
from icecaps.estimators.abstract_transformer_estimator import AbstractTransformerEstimator


class SanEstimator(EstimatorChain):

    def __init__(self, model_dir="/tmp", params=dict(), config=None, scope="", is_mmi_model=False):
        self.encoder = SanEncoderEstimator(
            model_dir, params, config=config, scope=scope+"/encoder")
        self.decoder = SanDecoderEstimator(
            model_dir, params, config=config, scope=scope+"/decoder", is_mmi_model=is_mmi_model)
        super().__init__([self.encoder, self.decoder],
                         model_dir, params, config, scope)

    @classmethod
    def list_params(cls, expected_params=None):
        print("San Encoder:")
        SanEncoderEstimator.list_params(expected_params)
        print()
        print("San Decoder:")
        SanDecoderEstimator.list_params(expected_params)
        print()
