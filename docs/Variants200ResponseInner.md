# Variants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**pos** | **float** |  | 
**rsid** | **List[str]** |  | [optional] 
**ref** | **str** |  | 
**alt** | **str** |  | 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 
**strain** | **List[str]** |  | [optional] 
**qual** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**annotations** | [**Variants200ResponseInnerAnnotations**](Variants200ResponseInnerAnnotations.md) |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**organism** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.variants200_response_inner import Variants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of Variants200ResponseInner from a JSON string
variants200_response_inner_instance = Variants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(Variants200ResponseInner.to_json())

# convert the object into a dict
variants200_response_inner_dict = variants200_response_inner_instance.to_dict()
# create an instance of Variants200ResponseInner from a dict
variants200_response_inner_from_dict = Variants200ResponseInner.from_dict(variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


