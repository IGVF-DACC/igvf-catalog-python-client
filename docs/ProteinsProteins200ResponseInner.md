# ProteinsProteins200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**protein_1** | [**ProteinsProteins200ResponseInnerProtein1**](ProteinsProteins200ResponseInnerProtein1.md) |  | 
**protein_2** | [**ProteinsProteins200ResponseInnerProtein1**](ProteinsProteins200ResponseInnerProtein1.md) |  | 
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
from igvf_catalog_client.models.proteins_proteins200_response_inner import ProteinsProteins200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProteinsProteins200ResponseInner from a JSON string
proteins_proteins200_response_inner_instance = ProteinsProteins200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ProteinsProteins200ResponseInner.to_json())

# convert the object into a dict
proteins_proteins200_response_inner_dict = proteins_proteins200_response_inner_instance.to_dict()
# create an instance of ProteinsProteins200ResponseInner from a dict
proteins_proteins200_response_inner_from_dict = ProteinsProteins200ResponseInner.from_dict(proteins_proteins200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


