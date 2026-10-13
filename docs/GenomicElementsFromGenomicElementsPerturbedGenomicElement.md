# GenomicElementsFromGenomicElementsPerturbedGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**type** | **str** |  | [optional] 
**source_annotation** | **str** |  | [optional] 
**promoter_of** | [**AccessibleGenomicElementPromoterOf**](AccessibleGenomicElementPromoterOf.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_genomic_elements_perturbed_genomic_element import GenomicElementsFromGenomicElementsPerturbedGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromGenomicElementsPerturbedGenomicElement from a JSON string
genomic_elements_from_genomic_elements_perturbed_genomic_element_instance = GenomicElementsFromGenomicElementsPerturbedGenomicElement.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromGenomicElementsPerturbedGenomicElement.to_json())

# convert the object into a dict
genomic_elements_from_genomic_elements_perturbed_genomic_element_dict = genomic_elements_from_genomic_elements_perturbed_genomic_element_instance.to_dict()
# create an instance of GenomicElementsFromGenomicElementsPerturbedGenomicElement from a dict
genomic_elements_from_genomic_elements_perturbed_genomic_element_from_dict = GenomicElementsFromGenomicElementsPerturbedGenomicElement.from_dict(genomic_elements_from_genomic_elements_perturbed_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


