# GenomicElement10


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**chr** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**source_annotation** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_element10 import GenomicElement10

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement10 from a JSON string
genomic_element10_instance = GenomicElement10.from_json(json)
# print the JSON string representation of the object
print(GenomicElement10.to_json())

# convert the object into a dict
genomic_element10_dict = genomic_element10_instance.to_dict()
# create an instance of GenomicElement10 from a dict
genomic_element10_from_dict = GenomicElement10.from_dict(genomic_element10_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


