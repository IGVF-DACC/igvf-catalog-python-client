# ProteinsProteins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**protein_1** | [**ProteinsProteinsProtein1**](ProteinsProteinsProtein1.md) |  | 
**protein_2** | [**ProteinsProteinsProtein1**](ProteinsProteinsProtein1.md) |  | 
**detection_method** | **str** |  | 
**detection_method_code** | **str** |  | 
**interaction_type** | **List[str]** |  | 
**interaction_type_code** | **List[str]** |  | 
**confidence_value_biogrid** | **float** |  | 
**confidence_value_intact** | **float** |  | 
**label** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**source_url** | **str** |  | 
**source** | **str** |  | 
**organism** | **str** |  | 
**pmids** | **List[str]** |  | 
**name** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.proteins_proteins import ProteinsProteins

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsProteins from a JSON string
proteins_proteins_instance = ProteinsProteins.from_json(json)
# print the JSON string representation of the object
print(ProteinsProteins.to_json())

# convert the object into a dict
proteins_proteins_dict = proteins_proteins_instance.to_dict()
# create an instance of ProteinsProteins from a dict
proteins_proteins_from_dict = ProteinsProteins.from_dict(proteins_proteins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


