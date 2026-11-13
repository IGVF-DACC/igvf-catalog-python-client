# ErrorNotFound

The error information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message | 
**code** | **str** | The error code | 
**issues** | [**List[ErrorIssue]**](ErrorIssue.md) | An array of issues that were responsible for the error | [optional] 

## Example

```python
from igvf_catalog_client.models.error_not_found import ErrorNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorNotFound from a JSON string
error_not_found_instance = ErrorNotFound.from_json(json)
# print the JSON string representation of the object
print(ErrorNotFound.to_json())

# convert the object into a dict
error_not_found_dict = error_not_found_instance.to_dict()
# create an instance of ErrorNotFound from a dict
error_not_found_from_dict = ErrorNotFound.from_dict(error_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


