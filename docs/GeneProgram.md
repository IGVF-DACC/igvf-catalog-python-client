# GeneProgram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**source_url** | **str** |  | [optional] 
**files_filesets** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**label** | **str** |  | 
**biosample_term** | **str** |  | [optional] 
**biological_context** | **str** |  | [optional] 
**treatments_term_ids** | **List[str]** |  | [optional] 
**perturbation** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**program_id** | **str** |  | 
**reported_gene_count** | **int** |  | 

## Example

```python
from igvf_catalog_client.models.gene_program import GeneProgram

# TODO update the JSON string below
json = "{}"
# create an instance of GeneProgram from a JSON string
gene_program_instance = GeneProgram.from_json(json)
# print the JSON string representation of the object
print(GeneProgram.to_json())

# convert the object into a dict
gene_program_dict = gene_program_instance.to_dict()
# create an instance of GeneProgram from a dict
gene_program_from_dict = GeneProgram.from_dict(gene_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


