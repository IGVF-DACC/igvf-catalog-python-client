# LlmQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**aql** | **str** |  | [optional] 
**aql_result** | **List[object]** |  | [optional] 
**answer** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.llm_query200_response import LlmQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LlmQuery200Response from a JSON string
llm_query200_response_instance = LlmQuery200Response.from_json(json)
# print the JSON string representation of the object
print(LlmQuery200Response.to_json())

# convert the object into a dict
llm_query200_response_dict = llm_query200_response_instance.to_dict()
# create an instance of LlmQuery200Response from a dict
llm_query200_response_from_dict = LlmQuery200Response.from_dict(llm_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


