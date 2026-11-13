# ErrorForbidden

The error information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message | 
**code** | **str** | The error code | 
**issues** | [**List[ErrorIssue]**](ErrorIssue.md) | An array of issues that were responsible for the error | [optional] 

## Example

```python
from igvf_catalog_client.models.error_forbidden import ErrorForbidden

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorForbidden from a JSON string
error_forbidden_instance = ErrorForbidden.from_json(json)
# print the JSON string representation of the object
print(ErrorForbidden.to_json())

# convert the object into a dict
error_forbidden_dict = error_forbidden_instance.to_dict()
# create an instance of ErrorForbidden from a dict
error_forbidden_from_dict = ErrorForbidden.from_dict(error_forbidden_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


