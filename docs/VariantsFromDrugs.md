# VariantsFromDrugs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**BiosamplesFromVariantsVariant**](BiosamplesFromVariantsVariant.md) |  | [optional] 
**to** | **str** |  | 
**gene_symbol** | **List[str]** |  | [optional] 
**pmid** | **str** |  | [optional] 
**study_parameters** | [**List[StudyParameters]**](StudyParameters.md) |  | [optional] 
**phenotype_categories** | **List[str]** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.variants_from_drugs import VariantsFromDrugs

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsFromDrugs from a JSON string
variants_from_drugs_instance = VariantsFromDrugs.from_json(json)
# print the JSON string representation of the object
print(VariantsFromDrugs.to_json())

# convert the object into a dict
variants_from_drugs_dict = variants_from_drugs_instance.to_dict()
# create an instance of VariantsFromDrugs from a dict
variants_from_drugs_from_dict = VariantsFromDrugs.from_dict(variants_from_drugs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


