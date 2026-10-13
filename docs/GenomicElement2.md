# GenomicElement2


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
**source_annotation** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_element2 import GenomicElement2

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement2 from a JSON string
genomic_element2_instance = GenomicElement2.from_json(json)
# print the JSON string representation of the object
print(GenomicElement2.to_json())

# convert the object into a dict
genomic_element2_dict = genomic_element2_instance.to_dict()
# create an instance of GenomicElement2 from a dict
genomic_element2_from_dict = GenomicElement2.from_dict(genomic_element2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


