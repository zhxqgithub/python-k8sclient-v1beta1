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


class V1beta1DeploymentSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1beta1DeploymentSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'replicas': 'int',
            'selector': 'str',
            'template': 'V1PodTemplateSpec',
            'strategy': 'V1beta1DeploymentStrategy',
            'unique_label_key': 'str'
        }

        self.attribute_map = {
            'replicas': 'replicas',
            'selector': 'selector',
            'template': 'template',
            'strategy': 'strategy',
            'unique_label_key': 'uniqueLabelKey'
        }

        self._replicas = None
        self._selector = None
        self._template = None
        self._strategy = None
        self._unique_label_key = None

    @property
    def replicas(self):
        """
        Gets the replicas of this V1beta1DeploymentSpec.
        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.

        :return: The replicas of this V1beta1DeploymentSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1beta1DeploymentSpec.
        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.

        :param replicas: The replicas of this V1beta1DeploymentSpec.
        :type: int
        """
        self._replicas = replicas

    @property
    def selector(self):
        """
        Gets the selector of this V1beta1DeploymentSpec.
        Label selector for pods. Existing ReplicationControllers whose pods are selected by this will be the ones affected by this deployment.

        :return: The selector of this V1beta1DeploymentSpec.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1beta1DeploymentSpec.
        Label selector for pods. Existing ReplicationControllers whose pods are selected by this will be the ones affected by this deployment.

        :param selector: The selector of this V1beta1DeploymentSpec.
        :type: str
        """
        self._selector = selector

    @property
    def template(self):
        """
        Gets the template of this V1beta1DeploymentSpec.
        Template describes the pods that will be created.

        :return: The template of this V1beta1DeploymentSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this V1beta1DeploymentSpec.
        Template describes the pods that will be created.

        :param template: The template of this V1beta1DeploymentSpec.
        :type: V1PodTemplateSpec
        """
        self._template = template

    @property
    def strategy(self):
        """
        Gets the strategy of this V1beta1DeploymentSpec.
        The deployment strategy to use to replace existing pods with new ones.

        :return: The strategy of this V1beta1DeploymentSpec.
        :rtype: V1beta1DeploymentStrategy
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Sets the strategy of this V1beta1DeploymentSpec.
        The deployment strategy to use to replace existing pods with new ones.

        :param strategy: The strategy of this V1beta1DeploymentSpec.
        :type: V1beta1DeploymentStrategy
        """
        self._strategy = strategy

    @property
    def unique_label_key(self):
        """
        Gets the unique_label_key of this V1beta1DeploymentSpec.
        Key of the selector that is added to existing RCs (and label key that is added to its pods) to prevent the existing RCs to select new pods (and old pods being selected by new RC). Users can set this to an empty string to indicate that the system should not add any selector and label. If unspecified, system uses \"deployment.kubernetes.io/podTemplateHash\". Value of this key is hash of DeploymentSpec.PodTemplateSpec. No label is added if this is set to empty string.

        :return: The unique_label_key of this V1beta1DeploymentSpec.
        :rtype: str
        """
        return self._unique_label_key

    @unique_label_key.setter
    def unique_label_key(self, unique_label_key):
        """
        Sets the unique_label_key of this V1beta1DeploymentSpec.
        Key of the selector that is added to existing RCs (and label key that is added to its pods) to prevent the existing RCs to select new pods (and old pods being selected by new RC). Users can set this to an empty string to indicate that the system should not add any selector and label. If unspecified, system uses \"deployment.kubernetes.io/podTemplateHash\". Value of this key is hash of DeploymentSpec.PodTemplateSpec. No label is added if this is set to empty string.

        :param unique_label_key: The unique_label_key of this V1beta1DeploymentSpec.
        :type: str
        """
        self._unique_label_key = unique_label_key

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
