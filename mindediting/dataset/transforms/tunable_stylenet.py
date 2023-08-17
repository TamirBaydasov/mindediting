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

import numpy as np


def transforms_tunable_stylenet_train(**kwargs):
    # TODO
    input_columns = ["HR", "LR"]
    output_columns = ["HR", "LR"]
    return [], input_columns, output_columns


def transforms_tunable_stylenet_val(**kwargs):
    input_columns = ["HR", "LR"]
    output_columns = ["LR", "HR"]

    def operation(HR, LR, batchInfo=1):
        scale = 255.0
        HR = [item / scale for item in HR]
        # LR = [item / scale for item in LR]
        return HR, HR

    return operation, input_columns, output_columns
