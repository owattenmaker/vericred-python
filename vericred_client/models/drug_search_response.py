# coding: utf-8

"""
Copyright 2016 SmartBear Software

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


class DrugSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DrugSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'meta': 'Meta',
            'drugs': 'list[Drug]',
            'drug_packages': 'list[DrugPackage]'
        }

        self.attribute_map = {
            'meta': 'meta',
            'drugs': 'drugs',
            'drug_packages': 'drug_packages'
        }

        self._meta = None
        self._drugs = None
        self._drug_packages = None

    @property
    def meta(self):
        """
        Gets the meta of this DrugSearchResponse.
        Metadata for query

        :return: The meta of this DrugSearchResponse.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this DrugSearchResponse.
        Metadata for query

        :param meta: The meta of this DrugSearchResponse.
        :type: Meta
        """
        self._meta = meta

    @property
    def drugs(self):
        """
        Gets the drugs of this DrugSearchResponse.
        Drugs found in query

        :return: The drugs of this DrugSearchResponse.
        :rtype: list[Drug]
        """
        return self._drugs

    @drugs.setter
    def drugs(self, drugs):
        """
        Sets the drugs of this DrugSearchResponse.
        Drugs found in query

        :param drugs: The drugs of this DrugSearchResponse.
        :type: list[Drug]
        """
        self._drugs = drugs

    @property
    def drug_packages(self):
        """
        Gets the drug_packages of this DrugSearchResponse.
        DrugPackages

        :return: The drug_packages of this DrugSearchResponse.
        :rtype: list[DrugPackage]
        """
        return self._drug_packages

    @drug_packages.setter
    def drug_packages(self, drug_packages):
        """
        Sets the drug_packages of this DrugSearchResponse.
        DrugPackages

        :param drug_packages: The drug_packages of this DrugSearchResponse.
        :type: list[DrugPackage]
        """
        self._drug_packages = drug_packages

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
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
