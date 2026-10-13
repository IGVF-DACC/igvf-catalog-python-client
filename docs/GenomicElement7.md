# GenomicElement7


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | [optional] 
**chr** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**name** | **str** |  | 
**source_annotation** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_element7 import GenomicElement7

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement7 from a JSON string
genomic_element7_instance = GenomicElement7.from_json(json)
# print the JSON string representation of the object
print(GenomicElement7.to_json())

# convert the object into a dict
genomic_element7_dict = genomic_element7_instance.to_dict()
# create an instance of GenomicElement7 from a dict
genomic_element7_from_dict = GenomicElement7.from_dict(genomic_element7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


