# PathwaysFromGenes200ResponseInnerPathwayAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organism** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**id_version** | **str** |  | 
**is_in_disease** | **bool** |  | 
**name_aliases** | **List[str]** |  | 
**is_top_level_pathway** | **bool** |  | 
**disease_ontology_terms** | **List[str]** |  | 
**go_biological_process** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**label** | **str** |  | 
**files_filesets** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.pathways_from_genes200_response_inner_pathway_any_of import PathwaysFromGenes200ResponseInnerPathwayAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaysFromGenes200ResponseInnerPathwayAnyOf from a JSON string
pathways_from_genes200_response_inner_pathway_any_of_instance = PathwaysFromGenes200ResponseInnerPathwayAnyOf.from_json(json)
# print the JSON string representation of the object
print(PathwaysFromGenes200ResponseInnerPathwayAnyOf.to_json())

# convert the object into a dict
pathways_from_genes200_response_inner_pathway_any_of_dict = pathways_from_genes200_response_inner_pathway_any_of_instance.to_dict()
# create an instance of PathwaysFromGenes200ResponseInnerPathwayAnyOf from a dict
pathways_from_genes200_response_inner_pathway_any_of_from_dict = PathwaysFromGenes200ResponseInnerPathwayAnyOf.from_dict(pathways_from_genes200_response_inner_pathway_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


