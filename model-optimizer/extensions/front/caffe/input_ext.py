"""
 Copyright (C) 2018-2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from extensions.ops.parameter import Parameter
from mo.front.caffe.extractors.utils import dim_to_shape
from mo.front.extractor import FrontExtractorOp


class InputFrontExtractor(FrontExtractorOp):
    op = 'input'
    enabled = True

    @classmethod
    def extract(cls, node):
        Parameter.update_node_stat(node, {'shape': dim_to_shape(node.pb.input_param.shape[0].dim)})
        return cls.enabled


class GlobalInputFrontExtractor(FrontExtractorOp):
    op = 'globalinput'
    enabled = True

    @classmethod
    def extract(cls, node):
        Parameter.update_node_stat(node)
        return cls.enabled
