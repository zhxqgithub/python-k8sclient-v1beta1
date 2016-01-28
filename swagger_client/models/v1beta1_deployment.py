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


class V1beta1Deployment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1beta1Deployment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'spec': 'V1beta1DeploymentSpec',
            'status': 'V1beta1DeploymentStatus'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'spec': 'spec',
            'status': 'status'
        }

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._spec = None
        self._status = None

    @property
    def kind(self):
        """
        Gets the kind of this V1beta1Deployment.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.1/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1beta1Deployment.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta1Deployment.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.1/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1beta1Deployment.
        :type: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1beta1Deployment.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.1/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1beta1Deployment.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1beta1Deployment.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.1/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1beta1Deployment.
        :type: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1beta1Deployment.
        Standard object metadata.

        :return: The metadata of this V1beta1Deployment.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1beta1Deployment.
        Standard object metadata.

        :param metadata: The metadata of this V1beta1Deployment.
        :type: V1ObjectMeta
        """
        self._metadata = metadata

    @property
    def spec(self):
        """
        Gets the spec of this V1beta1Deployment.
        Specification of the desired behavior of the Deployment.

        :return: The spec of this V1beta1Deployment.
        :rtype: V1beta1DeploymentSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """
        Sets the spec of this V1beta1Deployment.
        Specification of the desired behavior of the Deployment.

        :param spec: The spec of this V1beta1Deployment.
        :type: V1beta1DeploymentSpec
        """
        self._spec = spec

    @property
    def status(self):
        """
        Gets the status of this V1beta1Deployment.
        Most recently observed status of the Deployment.

        :return: The status of this V1beta1Deployment.
        :rtype: V1beta1DeploymentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1beta1Deployment.
        Most recently observed status of the Deployment.

        :param status: The status of this V1beta1Deployment.
        :type: V1beta1DeploymentStatus
        """
        self._status = status

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

