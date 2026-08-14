# GoTermsFromAnnotations200ResponseInner


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
from igvf_catalog_client.models.go_terms_from_annotations200_response_inner import GoTermsFromAnnotations200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoTermsFromAnnotations200ResponseInner from a JSON string
go_terms_from_annotations200_response_inner_instance = GoTermsFromAnnotations200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GoTermsFromAnnotations200ResponseInner.to_json())

# convert the object into a dict
go_terms_from_annotations200_response_inner_dict = go_terms_from_annotations200_response_inner_instance.to_dict()
# create an instance of GoTermsFromAnnotations200ResponseInner from a dict
go_terms_from_annotations200_response_inner_from_dict = GoTermsFromAnnotations200ResponseInner.from_dict(go_terms_from_annotations200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


