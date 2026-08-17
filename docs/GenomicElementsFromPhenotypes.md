# GenomicElementsFromPhenotypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**biological_context** | **str** |  | 
**biosample_term** | **str** |  | 
**files_filesets** | **str** |  | 
**crispr_modality** | **str** |  | [optional] 
**z_score** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**num_guides** | **float** |  | [optional] 
**num_guides_hit** | **float** |  | [optional] 
**num_guides_nonhit** | **float** |  | [optional] 
**fraction_guides_hit** | **float** |  | [optional] 
**phenotype_name** | **str** |  | [optional] 
**genomic_element** | [**GenesFromGenomicElementsGenomicElement**](GenesFromGenomicElementsGenomicElement.md) |  | 
**phenotype** | [**GenomicElementsFromPhenotypesPhenotype**](GenomicElementsFromPhenotypesPhenotype.md) |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_phenotypes import GenomicElementsFromPhenotypes

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromPhenotypes from a JSON string
genomic_elements_from_phenotypes_instance = GenomicElementsFromPhenotypes.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromPhenotypes.to_json())

# convert the object into a dict
genomic_elements_from_phenotypes_dict = genomic_elements_from_phenotypes_instance.to_dict()
# create an instance of GenomicElementsFromPhenotypes from a dict
genomic_elements_from_phenotypes_from_dict = GenomicElementsFromPhenotypes.from_dict(genomic_elements_from_phenotypes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


