# GeneProgramsGenePrograms


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
**gene_program_1** | [**GeneProgramsFromGenesGeneProgram**](GeneProgramsFromGenesGeneProgram.md) |  | 
**gene_program_2** | [**GeneProgramsFromGenesGeneProgram**](GeneProgramsFromGenesGeneProgram.md) |  | 
**name** | **str** |  | 
**inverse_name** | **str** |  | 
**pearson_correlation** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.gene_programs_gene_programs import GeneProgramsGenePrograms

# TODO update the JSON string below
json = "{}"
# create an instance of GeneProgramsGenePrograms from a JSON string
gene_programs_gene_programs_instance = GeneProgramsGenePrograms.from_json(json)
# print the JSON string representation of the object
print(GeneProgramsGenePrograms.to_json())

# convert the object into a dict
gene_programs_gene_programs_dict = gene_programs_gene_programs_instance.to_dict()
# create an instance of GeneProgramsGenePrograms from a dict
gene_programs_gene_programs_from_dict = GeneProgramsGenePrograms.from_dict(gene_programs_gene_programs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


