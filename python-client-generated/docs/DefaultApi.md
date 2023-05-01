# swagger_client.DefaultApi

All URIs are relative to *http://example.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](DefaultApi.md#users_get) | **GET** /users | Get all users
[**users_id_delete**](DefaultApi.md#users_id_delete) | **DELETE** /users/{id} | Delete a user by ID
[**users_id_get**](DefaultApi.md#users_id_get) | **GET** /users/{id} | Get a user by ID
[**users_id_put**](DefaultApi.md#users_id_put) | **PUT** /users/{id} | Update a user by ID
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Create a new user

# **users_get**
> list[InlineResponse200] users_get()

Get all users

Returns a list of all users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get all users
    api_response = api_instance.users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_delete**
> users_id_delete(id)

Delete a user by ID

Deletes a user with the given ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 56 # int | The ID of the user

try:
    # Delete a user by ID
    api_instance.users_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_get**
> InlineResponse200 users_id_get(id)

Get a user by ID

Returns a user with the given ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 56 # int | The ID of the user

try:
    # Get a user by ID
    api_response = api_instance.users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_put**
> InlineResponse200 users_id_put(id, body=body)

Update a user by ID

Updates a user with the given ID and name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 56 # int | The ID of the user
body = swagger_client.UsersIdBody() # UsersIdBody |  (optional)

try:
    # Update a user by ID
    api_response = api_instance.users_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user | 
 **body** | [**UsersIdBody**](UsersIdBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> InlineResponse200 users_post(body=body)

Create a new user

Creates a new user with the given name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UsersBody() # UsersBody |  (optional)

try:
    # Create a new user
    api_response = api_instance.users_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersBody**](UsersBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

