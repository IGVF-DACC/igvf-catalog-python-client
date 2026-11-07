# GeneProgramsFromGenesGeneProgram


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
from igvf_catalog_client.models.gene_programs_from_genes_gene_program import GeneProgramsFromGenesGeneProgram

# TODO update the JSON string below
json = "{}"
# create an instance of GeneProgramsFromGenesGeneProgram from a JSON string
gene_programs_from_genes_gene_program_instance = GeneProgramsFromGenesGeneProgram.from_json(json)
# print the JSON string representation of the object
print(GeneProgramsFromGenesGeneProgram.to_json())

# convert the object into a dict
gene_programs_from_genes_gene_program_dict = gene_programs_from_genes_gene_program_instance.to_dict()
# create an instance of GeneProgramsFromGenesGeneProgram from a dict
gene_programs_from_genes_gene_program_from_dict = GeneProgramsFromGenesGeneProgram.from_dict(gene_programs_from_genes_gene_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


