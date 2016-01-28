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


class V1beta1HorizontalPodAutoscalerStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1beta1HorizontalPodAutoscalerStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observed_generation': 'int',
            'last_scale_time': 'str',
            'current_replicas': 'int',
            'desired_replicas': 'int',
            'current_cpu_utilization_percentage': 'int'
        }

        self.attribute_map = {
            'observed_generation': 'observedGeneration',
            'last_scale_time': 'lastScaleTime',
            'current_replicas': 'currentReplicas',
            'desired_replicas': 'desiredReplicas',
            'current_cpu_utilization_percentage': 'currentCPUUtilizationPercentage'
        }

        self._observed_generation = None
        self._last_scale_time = None
        self._current_replicas = None
        self._desired_replicas = None
        self._current_cpu_utilization_percentage = None

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1beta1HorizontalPodAutoscalerStatus.
        most recent generation observed by this autoscaler.

        :return: The observed_generation of this V1beta1HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1beta1HorizontalPodAutoscalerStatus.
        most recent generation observed by this autoscaler.

        :param observed_generation: The observed_generation of this V1beta1HorizontalPodAutoscalerStatus.
        :type: int
        """
        self._observed_generation = observed_generation

    @property
    def last_scale_time(self):
        """
        Gets the last_scale_time of this V1beta1HorizontalPodAutoscalerStatus.
        last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.

        :return: The last_scale_time of this V1beta1HorizontalPodAutoscalerStatus.
        :rtype: str
        """
        return self._last_scale_time

    @last_scale_time.setter
    def last_scale_time(self, last_scale_time):
        """
        Sets the last_scale_time of this V1beta1HorizontalPodAutoscalerStatus.
        last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.

        :param last_scale_time: The last_scale_time of this V1beta1HorizontalPodAutoscalerStatus.
        :type: str
        """
        self._last_scale_time = last_scale_time

    @property
    def current_replicas(self):
        """
        Gets the current_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        current number of replicas of pods managed by this autoscaler.

        :return: The current_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """
        Sets the current_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        current number of replicas of pods managed by this autoscaler.

        :param current_replicas: The current_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        :type: int
        """
        self._current_replicas = current_replicas

    @property
    def desired_replicas(self):
        """
        Gets the desired_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        desired number of replicas of pods managed by this autoscaler.

        :return: The desired_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._desired_replicas

    @desired_replicas.setter
    def desired_replicas(self, desired_replicas):
        """
        Sets the desired_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        desired number of replicas of pods managed by this autoscaler.

        :param desired_replicas: The desired_replicas of this V1beta1HorizontalPodAutoscalerStatus.
        :type: int
        """
        self._desired_replicas = desired_replicas

    @property
    def current_cpu_utilization_percentage(self):
        """
        Gets the current_cpu_utilization_percentage of this V1beta1HorizontalPodAutoscalerStatus.
        current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.

        :return: The current_cpu_utilization_percentage of this V1beta1HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._current_cpu_utilization_percentage

    @current_cpu_utilization_percentage.setter
    def current_cpu_utilization_percentage(self, current_cpu_utilization_percentage):
        """
        Sets the current_cpu_utilization_percentage of this V1beta1HorizontalPodAutoscalerStatus.
        current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.

        :param current_cpu_utilization_percentage: The current_cpu_utilization_percentage of this V1beta1HorizontalPodAutoscalerStatus.
        :type: int
        """
        self._current_cpu_utilization_percentage = current_cpu_utilization_percentage

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

