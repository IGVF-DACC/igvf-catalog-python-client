# GenesFromGenomicElementsGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | [optional] 
**chr** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_from_genomic_elements_genomic_element import GenesFromGenomicElementsGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromGenomicElementsGenomicElement from a JSON string
genes_from_genomic_elements_genomic_element_instance = GenesFromGenomicElementsGenomicElement.from_json(json)
# print the JSON string representation of the object
print(GenesFromGenomicElementsGenomicElement.to_json())

# convert the object into a dict
genes_from_genomic_elements_genomic_element_dict = genes_from_genomic_elements_genomic_element_instance.to_dict()
# create an instance of GenesFromGenomicElementsGenomicElement from a dict
genes_from_genomic_elements_genomic_element_from_dict = GenesFromGenomicElementsGenomicElement.from_dict(genes_from_genomic_elements_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


