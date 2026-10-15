# GenomicElement4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**regulator_gene** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genomic_element4 import GenomicElement4

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElement4 from a JSON string
genomic_element4_instance = GenomicElement4.from_json(json)
# print the JSON string representation of the object
print(GenomicElement4.to_json())

# convert the object into a dict
genomic_element4_dict = genomic_element4_instance.to_dict()
# create an instance of GenomicElement4 from a dict
genomic_element4_from_dict = GenomicElement4.from_dict(genomic_element4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


