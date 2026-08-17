# GenomicElement9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**type** | **str** |  | 
**source_annotation** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genomic_element9 import GenomicElement9

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement9 from a JSON string
genomic_element9_instance = GenomicElement9.from_json(json)
# print the JSON string representation of the object
print(GenomicElement9.to_json())

# convert the object into a dict
genomic_element9_dict = genomic_element9_instance.to_dict()
# create an instance of GenomicElement9 from a dict
genomic_element9_from_dict = GenomicElement9.from_dict(genomic_element9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


