# LlmQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**aql** | **str** |  | [optional] 
**aql_result** | **List[object]** |  | [optional] 
**answer** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.llm_query import LlmQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LlmQuery from a JSON string
llm_query_instance = LlmQuery.from_json(json)
# print the JSON string representation of the object
print(LlmQuery.to_json())

# convert the object into a dict
llm_query_dict = llm_query_instance.to_dict()
# create an instance of LlmQuery from a dict
llm_query_from_dict = LlmQuery.from_dict(llm_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


