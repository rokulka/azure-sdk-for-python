# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CategoryDetail(Model):
    """An object describing additional category details.

    :param celebrities: An array of celebrities if any identified.
    :type celebrities:
     list[~azure.cognitiveservices.vision.computervision.models.CelebritiesModel]
    :param landmarks: An array of landmarks if any identified.
    :type landmarks:
     list[~azure.cognitiveservices.vision.computervision.models.LandmarksModel]
    """

    _attribute_map = {
        'celebrities': {'key': 'celebrities', 'type': '[CelebritiesModel]'},
        'landmarks': {'key': 'landmarks', 'type': '[LandmarksModel]'},
    }

    def __init__(self, *, celebrities=None, landmarks=None, **kwargs) -> None:
        super(CategoryDetail, self).__init__(**kwargs)
        self.celebrities = celebrities
        self.landmarks = landmarks
