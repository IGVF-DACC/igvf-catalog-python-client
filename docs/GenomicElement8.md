# GenomicElement8


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_element8 import GenomicElement8

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement8 from a JSON string
genomic_element8_instance = GenomicElement8.from_json(json)
# print the JSON string representation of the object
print(GenomicElement8.to_json())

# convert the object into a dict
genomic_element8_dict = genomic_element8_instance.to_dict()
# create an instance of GenomicElement8 from a dict
genomic_element8_from_dict = GenomicElement8.from_dict(genomic_element8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


