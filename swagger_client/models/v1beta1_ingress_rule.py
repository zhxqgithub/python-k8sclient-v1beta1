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


class V1beta1IngressRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1beta1IngressRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'host': 'str',
            'http': 'V1beta1HTTPIngressRuleValue'
        }

        self.attribute_map = {
            'host': 'host',
            'http': 'http'
        }

        self._host = None
        self._http = None

    @property
    def host(self):
        """
        Gets the host of this V1beta1IngressRule.
        Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the \"host\" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the\n	  IP in the Spec of the parent Ingress.\n2. The `:` delimiter is not respected because ports are not allowed.\n	  Currently the port of an Ingress is implicitly :80 for http and\n	  :443 for https.\nBoth these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.

        :return: The host of this V1beta1IngressRule.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this V1beta1IngressRule.
        Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the \"host\" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the\n	  IP in the Spec of the parent Ingress.\n2. The `:` delimiter is not respected because ports are not allowed.\n	  Currently the port of an Ingress is implicitly :80 for http and\n	  :443 for https.\nBoth these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.

        :param host: The host of this V1beta1IngressRule.
        :type: str
        """
        self._host = host

    @property
    def http(self):
        """
        Gets the http of this V1beta1IngressRule.


        :return: The http of this V1beta1IngressRule.
        :rtype: V1beta1HTTPIngressRuleValue
        """
        return self._http

    @http.setter
    def http(self, http):
        """
        Sets the http of this V1beta1IngressRule.


        :param http: The http of this V1beta1IngressRule.
        :type: V1beta1HTTPIngressRuleValue
        """
        self._http = http

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

