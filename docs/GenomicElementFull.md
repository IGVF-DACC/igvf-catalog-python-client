# GenomicElementFull


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
from igvf_catalog_client.models.genomic_element_full import GenomicElementFull

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementFull from a JSON string
genomic_element_full_instance = GenomicElementFull.from_json(json)
# print the JSON string representation of the object
print(GenomicElementFull.to_json())

# convert the object into a dict
genomic_element_full_dict = genomic_element_full_instance.to_dict()
# create an instance of GenomicElementFull from a dict
genomic_element_full_from_dict = GenomicElementFull.from_dict(genomic_element_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


