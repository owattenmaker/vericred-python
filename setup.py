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

import sys
from setuptools import setup, find_packages

NAME = "vericred_client"
VERSION = "0.0.6"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Vericred API",
    author_email="",
    url="",
    keywords=["Swagger", "Vericred API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Vericred&#39;s API allows you to search for Health Plans that a specific doctor
accepts.

## Getting Started

Visit our [Developer Portal](https://vericred.3scale.net) to
create an account.

Once you have created an account, you can create one Application for
Production and another for our Sandbox (select the appropriate Plan when
you create the Application).

## Authentication

To authenticate, pass the API Key you created in the Developer Portal as
a &#x60;Vericred-Api-Key&#x60; header.

&#x60;curl -H &#39;Vericred-Api-Key: YOUR_KEY&#39; &quot;https://api.vericred.com/providers?search_term&#x3D;Foo&amp;zip_code&#x3D;11215&quot;&#x60;

## Versioning

Vericred&#39;s API default to the latest version.  However, if you need a specific
version, you can request it with an &#x60;Accept-Version&#x60; header.

The current version is &#x60;v3&#x60;.  Previous versions are &#x60;v1&#x60; and &#x60;v2&#x60;.

&#x60;curl -H &#39;Vericred-Api-Key: YOUR_KEY&#39; -H &#39;Accept-Version: v2&#39; &quot;https://api.vericred.com/providers?search_term&#x3D;Foo&amp;zip_code&#x3D;11215&quot;&#x60;

## Pagination

Endpoints that accept &#x60;page&#x60; and &#x60;per_page&#x60; parameters are paginated. They expose
four additional fields that contain data about your position in the response,
namely &#x60;Total&#x60;, &#x60;Per-Page&#x60;, &#x60;Link&#x60;, and &#x60;Page&#x60; as described in [RFC-5988](https://tools.ietf.org/html/rfc5988).

For example, to display 5 results per page and view the second page of a
&#x60;GET&#x60; to &#x60;/networks&#x60;, your final request would be &#x60;GET /networks?....page&#x3D;2&amp;per_page&#x3D;5&#x60;.

## Sideloading

When we return multiple levels of an object graph (e.g. &#x60;Provider&#x60;s and their &#x60;State&#x60;s
we sideload the associated data.  In this example, we would provide an Array of
&#x60;State&#x60;s and a &#x60;state_id&#x60; for each provider.  This is done primarily to reduce the
payload size since many of the &#x60;Provider&#x60;s will share a &#x60;State&#x60;

&#x60;&#x60;&#x60;
{
  providers: [{ id: 1, state_id: 1}, { id: 2, state_id: 1 }],
  states: [{ id: 1, code: &#39;NY&#39; }]
}
&#x60;&#x60;&#x60;

If you need the second level of the object graph, you can just match the
corresponding id.

## Selecting specific data

All endpoints allow you to specify which fields you would like to return.
This allows you to limit the response to contain only the data you need.

For example, let&#39;s take a request that returns the following JSON by default

&#x60;&#x60;&#x60;
{
  provider: {
    id: 1,
    name: &#39;John&#39;,
    phone: &#39;1234567890&#39;,
    field_we_dont_care_about: &#39;value_we_dont_care_about&#39;
  },
  states: [{
    id: 1,
    name: &#39;New York&#39;,
    code: &#39;NY&#39;,
    field_we_dont_care_about: &#39;value_we_dont_care_about&#39;
  }]
}
&#x60;&#x60;&#x60;

To limit our results to only return the fields we care about, we specify the
&#x60;select&#x60; query string parameter for the corresponding fields in the JSON
document.

In this case, we want to select &#x60;name&#x60; and &#x60;phone&#x60; from the &#x60;provider&#x60; key,
so we would add the parameters &#x60;select&#x3D;provider.name,provider.phone&#x60;.
We also want the &#x60;name&#x60; and &#x60;code&#x60; from the &#x60;states&#x60; key, so we would
add the parameters &#x60;select&#x3D;states.name,staes.code&#x60;.  The id field of
each document is always returned whether or not it is requested.

Our final request would be &#x60;GET /providers/12345?select&#x3D;provider.name,provider.phone,states.name,states.code&#x60;

The response would be

&#x60;&#x60;&#x60;
{
  provider: {
    id: 1,
    name: &#39;John&#39;,
    phone: &#39;1234567890&#39;
  },
  states: [{
    id: 1,
    name: &#39;New York&#39;,
    code: &#39;NY&#39;
  }]
}
&#x60;&#x60;&#x60;


    """
)
