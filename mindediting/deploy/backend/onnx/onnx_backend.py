# Copyright © 2023 Huawei Technologies Co, Ltd. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

from backend.backend_metaclass import Backend


class OnnxBackend(Backend):
    """ONNXRuntime wrapper for inference.

    Args:
        model_file (str): Input onnx model file.
    """

    def __init__(self, model_file: str):
        super().__init__(model_file)

    def run(self, input_list):
        """Run inference with ONNXRuntime session."""
        print(input_list)
