# GenomicElement11


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | [optional] 
**name** | **str** |  | 
**aliases** | **List[str]** |  | [optional] 
**method** | **str** |  | [optional] 
**source_annotation** | **str** |  | 
**type** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genomic_element11 import GenomicElement11

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement11 from a JSON string
genomic_element11_instance = GenomicElement11.from_json(json)
# print the JSON string representation of the object
print(GenomicElement11.to_json())

# convert the object into a dict
genomic_element11_dict = genomic_element11_instance.to_dict()
# create an instance of GenomicElement11 from a dict
genomic_element11_from_dict = GenomicElement11.from_dict(genomic_element11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


