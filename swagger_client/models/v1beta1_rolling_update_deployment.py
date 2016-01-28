# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1beta1RollingUpdateDeployment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1beta1RollingUpdateDeployment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'max_unavailable': 'str',
            'max_surge': 'str',
            'min_ready_seconds': 'int'
        }

        self.attribute_map = {
            'max_unavailable': 'maxUnavailable',
            'max_surge': 'maxSurge',
            'min_ready_seconds': 'minReadySeconds'
        }

        self._max_unavailable = None
        self._max_surge = None
        self._min_ready_seconds = None

    @property
    def max_unavailable(self):
        """
        Gets the max_unavailable of this V1beta1RollingUpdateDeployment.
        The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0 if MaxSurge is 0. By default, a fixed value of 1 is used. Example: when this is set to 30%, the old RC can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.

        :return: The max_unavailable of this V1beta1RollingUpdateDeployment.
        :rtype: str
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        """
        Sets the max_unavailable of this V1beta1RollingUpdateDeployment.
        The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0 if MaxSurge is 0. By default, a fixed value of 1 is used. Example: when this is set to 30%, the old RC can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old RC can be scaled down further, followed by scaling up the new RC, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.

        :param max_unavailable: The max_unavailable of this V1beta1RollingUpdateDeployment.
        :type: str
        """
        self._max_unavailable = max_unavailable

    @property
    def max_surge(self):
        """
        Gets the max_surge of this V1beta1RollingUpdateDeployment.
        The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. By default, a value of 1 is used. Example: when this is set to 30%, the new RC can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is atmost 130% of desired pods.

        :return: The max_surge of this V1beta1RollingUpdateDeployment.
        :rtype: str
        """
        return self._max_surge

    @max_surge.setter
    def max_surge(self, max_surge):
        """
        Sets the max_surge of this V1beta1RollingUpdateDeployment.
        The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. By default, a value of 1 is used. Example: when this is set to 30%, the new RC can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new RC can be scaled up further, ensuring that total number of pods running at any time during the update is atmost 130% of desired pods.

        :param max_surge: The max_surge of this V1beta1RollingUpdateDeployment.
        :type: str
        """
        self._max_surge = max_surge

    @property
    def min_ready_seconds(self):
        """
        Gets the min_ready_seconds of this V1beta1RollingUpdateDeployment.
        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)

        :return: The min_ready_seconds of this V1beta1RollingUpdateDeployment.
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """
        Sets the min_ready_seconds of this V1beta1RollingUpdateDeployment.
        Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)

        :param min_ready_seconds: The min_ready_seconds of this V1beta1RollingUpdateDeployment.
        :type: int
        """
        self._min_ready_seconds = min_ready_seconds

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

