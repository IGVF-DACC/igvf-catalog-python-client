# ProteinComplexOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**uniprot_names** | **List[str]** |  | [optional] 
**uniprot_full_names** | **List[str]** |  | [optional] 
**uniprot_ids** | **List[str]** |  | [optional] 
**mane_select** | **bool** |  | [optional] 
**organism** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.protein_complex_option import ProteinComplexOption

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinComplexOption from a JSON string
protein_complex_option_instance = ProteinComplexOption.from_json(json)
# print the JSON string representation of the object
print(ProteinComplexOption.to_json())

# convert the object into a dict
protein_complex_option_dict = protein_complex_option_instance.to_dict()
# create an instance of ProteinComplexOption from a dict
protein_complex_option_from_dict = ProteinComplexOption.from_dict(protein_complex_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


