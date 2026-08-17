# LlmQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**password** | **str** |  | 
**verbose** | **str** |  | [optional] [default to 'false']

## Example

```python
from igvf_catalog_client.models.llm_query_request import LlmQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LlmQueryRequest from a JSON string
llm_query_request_instance = LlmQueryRequest.from_json(json)
# print the JSON string representation of the object
print(LlmQueryRequest.to_json())

# convert the object into a dict
llm_query_request_dict = llm_query_request_instance.to_dict()
# create an instance of LlmQueryRequest from a dict
llm_query_request_from_dict = LlmQueryRequest.from_dict(llm_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


