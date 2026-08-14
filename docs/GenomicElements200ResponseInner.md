# GenomicElements200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | [optional] 
**name** | **str** |  | 
**method** | **str** |  | [optional] 
**source_annotation** | **str** |  | 
**type** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements200_response_inner import GenomicElements200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElements200ResponseInner from a JSON string
genomic_elements200_response_inner_instance = GenomicElements200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenomicElements200ResponseInner.to_json())

# convert the object into a dict
genomic_elements200_response_inner_dict = genomic_elements200_response_inner_instance.to_dict()
# create an instance of GenomicElements200ResponseInner from a dict
genomic_elements200_response_inner_from_dict = GenomicElements200ResponseInner.from_dict(genomic_elements200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


