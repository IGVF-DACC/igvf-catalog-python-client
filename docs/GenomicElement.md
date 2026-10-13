# GenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**chr** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**source_annotation** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_element import GenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement from a JSON string
genomic_element_instance = GenomicElement.from_json(json)
# print the JSON string representation of the object
print(GenomicElement.to_json())

# convert the object into a dict
genomic_element_dict = genomic_element_instance.to_dict()
# create an instance of GenomicElement from a dict
genomic_element_from_dict = GenomicElement.from_dict(genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


