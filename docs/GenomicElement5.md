# GenomicElement5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**stop** | **float** |  | 
**type** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genomic_element5 import GenomicElement5

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement5 from a JSON string
genomic_element5_instance = GenomicElement5.from_json(json)
# print the JSON string representation of the object
print(GenomicElement5.to_json())

# convert the object into a dict
genomic_element5_dict = genomic_element5_instance.to_dict()
# create an instance of GenomicElement5 from a dict
genomic_element5_from_dict = GenomicElement5.from_dict(genomic_element5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


