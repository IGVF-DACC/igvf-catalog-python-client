# AnnotationsFromGoTerms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_product_id** | **str** |  | 
**gene_product_name** | **str** |  | [optional] 
**go_term_name** | **str** |  | 
**source** | **str** |  | 
**gene_product_type** | **str** |  | 
**gene_product_symbol** | **str** |  | 
**qualifier** | **List[str]** |  | 
**organism** | **str** |  | 
**evidence** | **str** |  | 
**go_id** | **str** |  | 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.annotations_from_go_terms import AnnotationsFromGoTerms

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationsFromGoTerms from a JSON string
annotations_from_go_terms_instance = AnnotationsFromGoTerms.from_json(json)
# print the JSON string representation of the object
print(AnnotationsFromGoTerms.to_json())

# convert the object into a dict
annotations_from_go_terms_dict = annotations_from_go_terms_instance.to_dict()
# create an instance of AnnotationsFromGoTerms from a dict
annotations_from_go_terms_from_dict = AnnotationsFromGoTerms.from_dict(annotations_from_go_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


