#!/usr/bin/python
# -*- coding: UTF-8 -*-

from core.engine import Engine
from utils.global_var import create_config

if __name__ == "__main__":
    # TODO(ysh329): add args for backend / threads / powermode / armeabi etc.
    config_dict = create_config("tnn")
    tnn = Engine(config_dict)
    model_dict = tnn.prepare_models()
    device_dict = tnn.prepare_devices()
    tnn.set_config("model_dict", model_dict)
    tnn.set_config("device_dict", device_dict)

    tnn.prepare_models_for_devices()
    tnn.prepare_benchmark_assets_for_devices()

    bench_dict = tnn.benchmark()
    summary_list = tnn.generate_benchmark_summary(bench_dict)