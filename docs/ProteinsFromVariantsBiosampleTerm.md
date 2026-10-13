# ProteinsFromVariantsBiosampleTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 
**term_id** | **str** |  | 
**name** | **str** |  | 
**synonyms** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**subontology** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.proteins_from_variants_biosample_term import ProteinsFromVariantsBiosampleTerm

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsFromVariantsBiosampleTerm from a JSON string
proteins_from_variants_biosample_term_instance = ProteinsFromVariantsBiosampleTerm.from_json(json)
# print the JSON string representation of the object
print(ProteinsFromVariantsBiosampleTerm.to_json())

# convert the object into a dict
proteins_from_variants_biosample_term_dict = proteins_from_variants_biosample_term_instance.to_dict()
# create an instance of ProteinsFromVariantsBiosampleTerm from a dict
proteins_from_variants_biosample_term_from_dict = ProteinsFromVariantsBiosampleTerm.from_dict(proteins_from_variants_biosample_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


