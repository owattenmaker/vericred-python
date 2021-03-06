# coding: utf-8

"""
    Vericred API

    Vericred's API allows you to search for Health Plans that a specific doctor
accepts.

## Getting Started

Visit our [Developer Portal](https://vericred.3scale.net) to
create an account.

Once you have created an account, you can create one Application for
Production and another for our Sandbox (select the appropriate Plan when
you create the Application).

## Authentication

To authenticate, pass the API Key you created in the Developer Portal as
a `Vericred-Api-Key` header.

`curl -H 'Vericred-Api-Key: YOUR_KEY' "https://api.vericred.com/providers?search_term=Foo&zip_code=11215"`

## Versioning

Vericred's API default to the latest version.  However, if you need a specific
version, you can request it with an `Accept-Version` header.

The current version is `v3`.  Previous versions are `v1` and `v2`.

`curl -H 'Vericred-Api-Key: YOUR_KEY' -H 'Accept-Version: v2' "https://api.vericred.com/providers?search_term=Foo&zip_code=11215"`

## Pagination

Endpoints that accept `page` and `per_page` parameters are paginated. They expose
four additional fields that contain data about your position in the response,
namely `Total`, `Per-Page`, `Link`, and `Page` as described in [RFC-5988](https://tools.ietf.org/html/rfc5988).

For example, to display 5 results per page and view the second page of a
`GET` to `/networks`, your final request would be `GET /networks?....page=2&per_page=5`.

## Sideloading

When we return multiple levels of an object graph (e.g. `Provider`s and their `State`s
we sideload the associated data.  In this example, we would provide an Array of
`State`s and a `state_id` for each provider.  This is done primarily to reduce the
payload size since many of the `Provider`s will share a `State`

```
{
  providers: [{ id: 1, state_id: 1}, { id: 2, state_id: 1 }],
  states: [{ id: 1, code: 'NY' }]
}
```

If you need the second level of the object graph, you can just match the
corresponding id.

## Selecting specific data

All endpoints allow you to specify which fields you would like to return.
This allows you to limit the response to contain only the data you need.

For example, let's take a request that returns the following JSON by default

```
{
  provider: {
    id: 1,
    name: 'John',
    phone: '1234567890',
    field_we_dont_care_about: 'value_we_dont_care_about'
  },
  states: [{
    id: 1,
    name: 'New York',
    code: 'NY',
    field_we_dont_care_about: 'value_we_dont_care_about'
  }]
}
```

To limit our results to only return the fields we care about, we specify the
`select` query string parameter for the corresponding fields in the JSON
document.

In this case, we want to select `name` and `phone` from the `provider` key,
so we would add the parameters `select=provider.name,provider.phone`.
We also want the `name` and `code` from the `states` key, so we would
add the parameters `select=states.name,staes.code`.  The id field of
each document is always returned whether or not it is requested.

Our final request would be `GET /providers/12345?select=provider.name,provider.phone,states.name,states.code`

The response would be

```
{
  provider: {
    id: 1,
    name: 'John',
    phone: '1234567890'
  },
  states: [{
    id: 1,
    name: 'New York',
    code: 'NY'
  }]
}
```



    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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

from pprint import pformat
from six import iteritems
import re


class Applicant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, dob=None, member_id=None, name=None, relationship=None, smoker=None, ssn=None):
        """
        Applicant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'dob': 'date',
            'member_id': 'str',
            'name': 'str',
            'relationship': 'str',
            'smoker': 'bool',
            'ssn': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'dob': 'dob',
            'member_id': 'member_id',
            'name': 'name',
            'relationship': 'relationship',
            'smoker': 'smoker',
            'ssn': 'ssn'
        }

        self._id = id
        self._dob = dob
        self._member_id = member_id
        self._name = name
        self._relationship = relationship
        self._smoker = smoker
        self._ssn = ssn

    @property
    def id(self):
        """
        Gets the id of this Applicant.
        Primary key

        :return: The id of this Applicant.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Applicant.
        Primary key

        :param id: The id of this Applicant.
        :type: int
        """

        self._id = id

    @property
    def dob(self):
        """
        Gets the dob of this Applicant.
        Date of Birth

        :return: The dob of this Applicant.
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """
        Sets the dob of this Applicant.
        Date of Birth

        :param dob: The dob of this Applicant.
        :type: date
        """

        self._dob = dob

    @property
    def member_id(self):
        """
        Gets the member_id of this Applicant.
        Member token

        :return: The member_id of this Applicant.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this Applicant.
        Member token

        :param member_id: The member_id of this Applicant.
        :type: str
        """

        self._member_id = member_id

    @property
    def name(self):
        """
        Gets the name of this Applicant.
        Full name of the Applicant

        :return: The name of this Applicant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Applicant.
        Full name of the Applicant

        :param name: The name of this Applicant.
        :type: str
        """

        self._name = name

    @property
    def relationship(self):
        """
        Gets the relationship of this Applicant.
        Relationship of the Applicant to the Member

        :return: The relationship of this Applicant.
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """
        Sets the relationship of this Applicant.
        Relationship of the Applicant to the Member

        :param relationship: The relationship of this Applicant.
        :type: str
        """

        self._relationship = relationship

    @property
    def smoker(self):
        """
        Gets the smoker of this Applicant.
        Does the Applicant smoke?

        :return: The smoker of this Applicant.
        :rtype: bool
        """
        return self._smoker

    @smoker.setter
    def smoker(self, smoker):
        """
        Sets the smoker of this Applicant.
        Does the Applicant smoke?

        :param smoker: The smoker of this Applicant.
        :type: bool
        """

        self._smoker = smoker

    @property
    def ssn(self):
        """
        Gets the ssn of this Applicant.
        Applicant's Social Security Number

        :return: The ssn of this Applicant.
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """
        Sets the ssn of this Applicant.
        Applicant's Social Security Number

        :param ssn: The ssn of this Applicant.
        :type: str
        """

        self._ssn = ssn

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
