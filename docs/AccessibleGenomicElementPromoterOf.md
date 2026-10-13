# AccessibleGenomicElementPromoterOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**gene_type** | **str** |  | 
**name** | **str** |  | 
**strand** | **str** |  | [optional] 
**hgnc** | **str** |  | [optional] 
**entrez** | **str** |  | [optional] 
**collections** | **List[str]** |  | [optional] 
**study_sets** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**version** | **str** |  | 
**source_url** | **str** |  | 
**synonyms** | **List[str]** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.accessible_genomic_element_promoter_of import AccessibleGenomicElementPromoterOf

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleGenomicElementPromoterOf from a JSON string
accessible_genomic_element_promoter_of_instance = AccessibleGenomicElementPromoterOf.from_json(json)
# print the JSON string representation of the object
print(AccessibleGenomicElementPromoterOf.to_json())

# convert the object into a dict
accessible_genomic_element_promoter_of_dict = accessible_genomic_element_promoter_of_instance.to_dict()
# create an instance of AccessibleGenomicElementPromoterOf from a dict
accessible_genomic_element_promoter_of_from_dict = AccessibleGenomicElementPromoterOf.from_dict(accessible_genomic_element_promoter_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


