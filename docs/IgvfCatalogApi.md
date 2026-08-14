# igvf_catalog_client.IgvfCatalogApi

All URIs are relative to *https://api.catalogkg.igvf.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_coding_variants_from_genes**](IgvfCatalogApi.md#all_coding_variants_from_genes) | **GET** /genes/coding-variants/all-scores | 
[**annotations_from_go_terms**](IgvfCatalogApi.md#annotations_from_go_terms) | **GET** /go-terms/gene-products | 
[**autocomplete**](IgvfCatalogApi.md#autocomplete) | **GET** /autocomplete | 
[**biosamples_from_genomic_elements**](IgvfCatalogApi.md#biosamples_from_genomic_elements) | **GET** /genomic-elements/biosamples | 
[**biosamples_from_variants**](IgvfCatalogApi.md#biosamples_from_variants) | **GET** /variants/biosamples | 
[**coding_variants**](IgvfCatalogApi.md#coding_variants) | **GET** /coding-variants | 
[**coding_variants_count_from_gene**](IgvfCatalogApi.md#coding_variants_count_from_gene) | **GET** /coding-variants/phenotypes-count | 
[**coding_variants_from_genes**](IgvfCatalogApi.md#coding_variants_from_genes) | **GET** /genes/coding-variants/scores | 
[**coding_variants_from_phenotypes**](IgvfCatalogApi.md#coding_variants_from_phenotypes) | **GET** /phenotypes/coding-variants | 
[**coding_variants_from_variants**](IgvfCatalogApi.md#coding_variants_from_variants) | **GET** /variants/coding-variants | 
[**coding_variants_summary**](IgvfCatalogApi.md#coding_variants_summary) | **GET** /coding-variants/phenotypes/score-summary | 
[**complexes**](IgvfCatalogApi.md#complexes) | **GET** /complexes | 
[**complexes_from_proteins**](IgvfCatalogApi.md#complexes_from_proteins) | **GET** /proteins/complexes | 
[**deprecated_coding_variants_summary**](IgvfCatalogApi.md#deprecated_coding_variants_summary) | **GET** /variants/phenotypes/score-summary | 
[**disease_from_variants**](IgvfCatalogApi.md#disease_from_variants) | **GET** /variants/diseases | 
[**diseases_from_genes**](IgvfCatalogApi.md#diseases_from_genes) | **GET** /genes/diseases | 
[**drugs**](IgvfCatalogApi.md#drugs) | **GET** /drugs | 
[**drugs_from_variants**](IgvfCatalogApi.md#drugs_from_variants) | **GET** /variants/drugs | 
[**enhancer_gene_predictions**](IgvfCatalogApi.md#enhancer_gene_predictions) | **GET** /enhancer-gene-predictions | 
[**files_filesets**](IgvfCatalogApi.md#files_filesets) | **GET** /files-filesets | 
[**genes**](IgvfCatalogApi.md#genes) | **GET** /genes | 
[**genes_from_diseases**](IgvfCatalogApi.md#genes_from_diseases) | **GET** /diseases/genes | 
[**genes_from_genomic_elements**](IgvfCatalogApi.md#genes_from_genomic_elements) | **GET** /genomic-elements/genes | 
[**genes_from_pathways**](IgvfCatalogApi.md#genes_from_pathways) | **GET** /pathways/genes | 
[**genes_from_proteins**](IgvfCatalogApi.md#genes_from_proteins) | **GET** /proteins/genes | 
[**genes_from_transcripts**](IgvfCatalogApi.md#genes_from_transcripts) | **GET** /transcripts/genes | 
[**genes_from_variants**](IgvfCatalogApi.md#genes_from_variants) | **GET** /variants/genes | 
[**genes_genes**](IgvfCatalogApi.md#genes_genes) | **GET** /genes/genes | 
[**genes_proteins_from_variants**](IgvfCatalogApi.md#genes_proteins_from_variants) | **GET** /variants/genes-proteins | 
[**genes_proteins_genes_proteins**](IgvfCatalogApi.md#genes_proteins_genes_proteins) | **GET** /genes-proteins/genes-proteins | 
[**genes_structure**](IgvfCatalogApi.md#genes_structure) | **GET** /genes-structure | 
[**genomic_elements**](IgvfCatalogApi.md#genomic_elements) | **GET** /genomic-elements | 
[**genomic_elements_from_biosamples**](IgvfCatalogApi.md#genomic_elements_from_biosamples) | **GET** /biosamples/genomic-elements | 
[**genomic_elements_from_genes**](IgvfCatalogApi.md#genomic_elements_from_genes) | **GET** /genes/genomic-elements | 
[**genomic_elements_from_phenotypes**](IgvfCatalogApi.md#genomic_elements_from_phenotypes) | **GET** /phenotypes/genomic-elements | 
[**genomic_elements_from_variants**](IgvfCatalogApi.md#genomic_elements_from_variants) | **GET** /variants/genomic-elements | 
[**genomic_elements_from_variants_count**](IgvfCatalogApi.md#genomic_elements_from_variants_count) | **GET** /variants/predictions-count | 
[**genomic_elements_predictions_from_variant**](IgvfCatalogApi.md#genomic_elements_predictions_from_variant) | **GET** /variants/genomic-elements/cell-gene-predictions | 
[**go_terms_from_annotations**](IgvfCatalogApi.md#go_terms_from_annotations) | **GET** /gene-products/go-terms | 
[**grn**](IgvfCatalogApi.md#grn) | **GET** /gene-regulatory-network | 
[**health**](IgvfCatalogApi.md#health) | **GET** /health | 
[**motifs**](IgvfCatalogApi.md#motifs) | **GET** /motifs | 
[**motifs_from_proteins**](IgvfCatalogApi.md#motifs_from_proteins) | **GET** /proteins/motifs | 
[**nearest_genes**](IgvfCatalogApi.md#nearest_genes) | **GET** /variants/nearest-genes | 
[**ontology_term**](IgvfCatalogApi.md#ontology_term) | **GET** /ontology-terms | 
[**ontology_term_children**](IgvfCatalogApi.md#ontology_term_children) | **GET** /ontology-terms/{ontology_term_id}/children | 
[**ontology_term_parents**](IgvfCatalogApi.md#ontology_term_parents) | **GET** /ontology-terms/{ontology_term_id}/parents | 
[**ontology_term_transitive_closure**](IgvfCatalogApi.md#ontology_term_transitive_closure) | **GET** /ontology-terms/{ontology_term_id_start}/transitive-closure/{ontology_term_id_end} | 
[**pathways**](IgvfCatalogApi.md#pathways) | **GET** /pathways | 
[**pathways_from_genes**](IgvfCatalogApi.md#pathways_from_genes) | **GET** /genes/pathways | 
[**pathways_from_pathways**](IgvfCatalogApi.md#pathways_from_pathways) | **GET** /pathways/pathways | 
[**phenotypes_from_coding_variants**](IgvfCatalogApi.md#phenotypes_from_coding_variants) | **GET** /coding-variants/phenotypes | 
[**phenotypes_from_genomic_elements**](IgvfCatalogApi.md#phenotypes_from_genomic_elements) | **GET** /genomic-elements/phenotypes | 
[**phenotypes_from_variants**](IgvfCatalogApi.md#phenotypes_from_variants) | **GET** /variants/phenotypes | 
[**predictions_from_variants**](IgvfCatalogApi.md#predictions_from_variants) | **GET** /variants/predictions | 
[**proteins**](IgvfCatalogApi.md#proteins) | **GET** /proteins | 
[**proteins_from_complexes**](IgvfCatalogApi.md#proteins_from_complexes) | **GET** /complexes/proteins | 
[**proteins_from_genes**](IgvfCatalogApi.md#proteins_from_genes) | **GET** /genes/proteins | 
[**proteins_from_motifs**](IgvfCatalogApi.md#proteins_from_motifs) | **GET** /motifs/proteins | 
[**proteins_from_transcripts**](IgvfCatalogApi.md#proteins_from_transcripts) | **GET** /transcripts/proteins | 
[**proteins_from_variants**](IgvfCatalogApi.md#proteins_from_variants) | **GET** /variants/proteins | 
[**proteins_proteins**](IgvfCatalogApi.md#proteins_proteins) | **GET** /proteins/proteins | 
[**qtl_summary_endpoint**](IgvfCatalogApi.md#qtl_summary_endpoint) | **GET** /variants/genes/summary | 
[**qtls**](IgvfCatalogApi.md#qtls) | **GET** /qtls | 
[**studies**](IgvfCatalogApi.md#studies) | **GET** /studies | 
[**transcripts**](IgvfCatalogApi.md#transcripts) | **GET** /transcripts | 
[**transcripts_from_genes**](IgvfCatalogApi.md#transcripts_from_genes) | **GET** /genes/transcripts | 
[**transcripts_from_proteins**](IgvfCatalogApi.md#transcripts_from_proteins) | **GET** /proteins/transcripts | 
[**variant_by_frequency_source**](IgvfCatalogApi.md#variant_by_frequency_source) | **GET** /variants/freq | 
[**variant_summary**](IgvfCatalogApi.md#variant_summary) | **GET** /variants/summary | 
[**variants**](IgvfCatalogApi.md#variants) | **GET** /variants | 
[**variants_alleles**](IgvfCatalogApi.md#variants_alleles) | **GET** /variants/gnomad-alleles | 
[**variants_from_biosamples**](IgvfCatalogApi.md#variants_from_biosamples) | **GET** /biosamples/variants | 
[**variants_from_coding_variants**](IgvfCatalogApi.md#variants_from_coding_variants) | **GET** /coding-variants/variants | 
[**variants_from_diseases**](IgvfCatalogApi.md#variants_from_diseases) | **GET** /diseases/variants | 
[**variants_from_drugs**](IgvfCatalogApi.md#variants_from_drugs) | **GET** /drugs/variants | 
[**variants_from_gene_proteins**](IgvfCatalogApi.md#variants_from_gene_proteins) | **GET** /genes-proteins/variants | 
[**variants_from_genes**](IgvfCatalogApi.md#variants_from_genes) | **GET** /genes/variants | 
[**variants_from_genomic_elements**](IgvfCatalogApi.md#variants_from_genomic_elements) | **GET** /genomic-elements/variants | 
[**variants_from_phenotypes**](IgvfCatalogApi.md#variants_from_phenotypes) | **GET** /phenotypes/variants | 
[**variants_from_proteins**](IgvfCatalogApi.md#variants_from_proteins) | **GET** /proteins/variants | 
[**variants_from_variant_id**](IgvfCatalogApi.md#variants_from_variant_id) | **GET** /variants/variant-ld | 
[**variants_from_variant_id_summary**](IgvfCatalogApi.md#variants_from_variant_id_summary) | **GET** /variants/variant-ld/summary | 
[**variants_genomic_elements_genes**](IgvfCatalogApi.md#variants_genomic_elements_genes) | **GET** /variants/genomic-elements/genes | 
[**variants_region_summary**](IgvfCatalogApi.md#variants_region_summary) | **GET** /variants/region-summary | 


# **all_coding_variants_from_genes**
> List[AllCodingVariantsFromGenes200ResponseInner] all_coding_variants_from_genes(gene_id, dataset, page=page, limit=limit)

Retrieve a list of all numeric scores of associated coding variants for a gene and a dataset.<br>   Example: gene_id = ENSG00000165841, <br>   dataset = VAMP-seq

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.all_coding_variants_from_genes200_response_inner import AllCodingVariantsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str | 
    dataset = 'dataset_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.all_coding_variants_from_genes(gene_id, dataset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->all_coding_variants_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->all_coding_variants_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | 
 **dataset** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[AllCodingVariantsFromGenes200ResponseInner]**](AllCodingVariantsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotations_from_go_terms**
> List[GoTermsFromAnnotations200ResponseInner] annotations_from_go_terms(go_term_id, name=name, page=page, limit=limit)

Retrieve annotations associated with a GO term. <br>   Example: go_term_id = GO_1990590, <br>   name = has component<br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.go_terms_from_annotations200_response_inner import GoTermsFromAnnotations200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    go_term_id = 'go_term_id_example' # str | 
    name = 'name_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.annotations_from_go_terms(go_term_id, name=name, page=page, limit=limit)
        print("The response of IgvfCatalogApi->annotations_from_go_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->annotations_from_go_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **go_term_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GoTermsFromAnnotations200ResponseInner]**](GoTermsFromAnnotations200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete**
> List[Autocomplete200ResponseInner] autocomplete(term, page=page)

Autocomplete names for genes and proteins based on prefix search.<br>   Example: term = TP53, <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.autocomplete200_response_inner import Autocomplete200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    term = 'term_example' # str | 
    page = 0 # float |  (optional) (default to 0)

    try:
        api_response = api_instance.autocomplete(term, page=page)
        print("The response of IgvfCatalogApi->autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]

### Return type

[**List[Autocomplete200ResponseInner]**](Autocomplete200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **biosamples_from_genomic_elements**
> List[BiosamplesFromGenomicElements200ResponseInner] biosamples_from_genomic_elements(region=region, region_type=region_type, source=source, method=method, files_fileset=files_fileset, verbose=verbose, page=page, limit=limit)

Retrieve MPRA experiments by querying positions of genomic elements. <br>   Set verbose = true to retrieve full info on the cell ontology terms. <br>   Example: region_type = tested elements, <br>   region = chr10:100038743-100038963. <br>   files_fileset = ENCFF475FKV,<br>   method = MPRA,<br>   source = IGVF. <br>   The limit parameter controls the page size and can not exceed 50. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.biosamples_from_genomic_elements200_response_inner import BiosamplesFromGenomicElements200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str |  (optional)
    region_type = 'region_type_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.biosamples_from_genomic_elements(region=region, region_type=region_type, source=source, method=method, files_fileset=files_fileset, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->biosamples_from_genomic_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->biosamples_from_genomic_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | [optional] 
 **region_type** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[BiosamplesFromGenomicElements200ResponseInner]**](BiosamplesFromGenomicElements200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **biosamples_from_variants**
> List[BiosamplesFromVariants200ResponseInner] biosamples_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, files_fileset=files_fileset, method=method, element_id=element_id, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve data from STARR-seq, BlueSTARR, and MPRA for a given variant.<br>     At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, region, method, or files_fileset. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="mpra">MPRA</button> <button class="method-example-tab" data-method-example-tab="starr-seq">STARR-seq</button> <button class="method-example-tab" data-method-example-tab="bluestarr">BlueSTARR</button> </div> <div class="method-example-panel is-active" data-method-example-panel="mpra"> <strong>MPRA:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000001.11:1000161:C:A</li> <li>method = MPRA</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr1:1000160-1000163 (maximum length: 10kb)</li> <li>method = MPRA</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="starr-seq"> <strong>STARR-seq:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000001.11:14772:C:T</li> <li>method = STARR-seq</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr1:14771-14775 (maximum length: 10kb)</li> <li>method = STARR-seq</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="bluestarr"> <strong>BlueSTARR:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000001.11:100003415:C:A</li> <li>method = BlueSTARR</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr1:100003414-100003418 (maximum length: 10kb)</li> <li>method = BlueSTARR</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.biosamples_from_variants200_response_inner import BiosamplesFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    element_id = 'element_id_example' # str |  (optional)
    significant = 'significant_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.biosamples_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, files_fileset=files_fileset, method=method, element_id=element_id, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->biosamples_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->biosamples_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **element_id** | **str**|  | [optional] 
 **significant** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[BiosamplesFromVariants200ResponseInner]**](BiosamplesFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coding_variants**
> List[CodingVariantsFromVariants200ResponseInner] coding_variants(id=id, name=name, hgvsp=hgvsp, protein_id=protein_id, uniprot_name=uniprot_name, gene_name=gene_name, amino_acid_position=amino_acid_position, alt_amino_acid=alt_amino_acid, transcript_id=transcript_id, page=page, limit=limit)

Retrieve coding variants annotations. <br>   At least one of these fields is required: id, name, hgvsp, protein_id, uniprot_name, gene_name, transcript_id. <br>   alt_amino_acid filters by the alternate amino acid at the given position (single-letter code, use * for stop codon). <br>   Example: name = SAMD7_ENST00000335556_p.Gly253Asp_c.758_759delinsAC <br>   id = SAMD7_ENST00000335556_p.Gly253Asp_c.758_759delinsAC, <br>   hgvsp = p.Gly253Asp, <br>   gene_name = SAMD7, <br>   protein_id = ENSP00000334668, <br>   uniprot_name = SAMD7_HUMAN, <br>   amino_acid_position = 253 (range values are also available, e.g: range:0-2), <br>   alt_amino_acid = D, <br>   transcript_id = ENST00000335556.<br>   The limit parameter controls the page size and can not exceed 25. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.coding_variants_from_variants200_response_inner import CodingVariantsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    id = 'id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    hgvsp = 'hgvsp_example' # str |  (optional)
    protein_id = 'protein_id_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    amino_acid_position = 'amino_acid_position_example' # str |  (optional)
    alt_amino_acid = 'alt_amino_acid_example' # str |  (optional)
    transcript_id = 'transcript_id_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.coding_variants(id=id, name=name, hgvsp=hgvsp, protein_id=protein_id, uniprot_name=uniprot_name, gene_name=gene_name, amino_acid_position=amino_acid_position, alt_amino_acid=alt_amino_acid, transcript_id=transcript_id, page=page, limit=limit)
        print("The response of IgvfCatalogApi->coding_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->coding_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **hgvsp** | **str**|  | [optional] 
 **protein_id** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **amino_acid_position** | **str**|  | [optional] 
 **alt_amino_acid** | **str**|  | [optional] 
 **transcript_id** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[CodingVariantsFromVariants200ResponseInner]**](CodingVariantsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coding_variants_count_from_gene**
> List[VariantsRegionSummary200ResponseByMethodInner] coding_variants_count_from_gene(gene_id, files_fileset=files_fileset)

Retrieve counts of coding variants associated with phenotypes.<br>     Example: gene_id = ENSG00000165841, <br>     files_fileset = IGVFFI6893ZOAA.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_region_summary200_response_by_method_inner import VariantsRegionSummary200ResponseByMethodInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str | 
    files_fileset = 'files_fileset_example' # str |  (optional)

    try:
        api_response = api_instance.coding_variants_count_from_gene(gene_id, files_fileset=files_fileset)
        print("The response of IgvfCatalogApi->coding_variants_count_from_gene:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->coding_variants_count_from_gene: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | 
 **files_fileset** | **str**|  | [optional] 

### Return type

[**List[VariantsRegionSummary200ResponseByMethodInner]**](VariantsRegionSummary200ResponseByMethodInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coding_variants_from_genes**
> List[CodingVariantsFromGenes200ResponseInner] coding_variants_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, method=method, files_fileset=files_fileset, page=page, limit=limit)

Retrieve scores and predictions of associated coding variants for one specific gene.<br>     At least one of these fields is required: gene_id, hgnc_id, gene_name, synonym. <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="dual-ipa">DUAL-IPA</button> <button class="method-example-tab" data-method-example-tab="esm-1v">ESM-1v</button> <button class="method-example-tab" data-method-example-tab="mutpred2">MutPred2</button> <button class="method-example-tab" data-method-example-tab="sge">SGE</button> <button class="method-example-tab" data-method-example-tab="vamp-seq">VAMP-seq</button> <button class="method-example-tab" data-method-example-tab="painting">Variant painting with fluorescence</button> </div> <div class="method-example-panel is-active" data-method-example-panel="dual-ipa"> <strong>DUAL-IPA:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_name = ACSF3</li> <li>method = DUAL-IPA</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="esm-1v"> <strong>ESM-1v:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000121410</li> <li>method = ESM-1v</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="mutpred2"> <strong>MutPred2:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000196584</li> <li>method = MutPred2</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sge"> <strong>SGE:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000139618</li> <li>method = SGE</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="vamp-seq"> <strong>VAMP-seq:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000165841</li> <li>method = VAMP-seq</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="painting"> <strong>Variant painting with fluorescence:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000133703</li> <li>method = Variant painting with fluorescence</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.coding_variants_from_genes200_response_inner import CodingVariantsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.coding_variants_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, method=method, files_fileset=files_fileset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->coding_variants_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->coding_variants_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[CodingVariantsFromGenes200ResponseInner]**](CodingVariantsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coding_variants_from_phenotypes**
> List[PhenotypesFromCodingVariants200ResponseInner] coding_variants_from_phenotypes(phenotype_id=phenotype_id, phenotype_name=phenotype_name, method=method, files_fileset=files_fileset, page=page, limit=limit)

Retrieve coding variants associated with the query phenotype.<br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="dual-ipa">DUAL-IPA</button> <button class="method-example-tab" data-method-example-tab="esm-1v">ESM-1v</button> <button class="method-example-tab" data-method-example-tab="mutpred2">MutPred2</button> <button class="method-example-tab" data-method-example-tab="sge">SGE</button> <button class="method-example-tab" data-method-example-tab="vamp-seq">VAMP-seq</button> <button class="method-example-tab" data-method-example-tab="variant-painting">Variant painting via fluorescence</button> </div> <div class="method-example-panel is-active" data-method-example-panel="dual-ipa"> <strong>DUAL-IPA:</strong> <div class="method-query-example"> <strong>query by phenotype identifier</strong>  <ul> <li>phenotype_id = BAO_0040014</li> <li>method = DUAL-IPA</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI6224HZMG</li> <li>method = DUAL-IPA</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="esm-1v"> <strong>ESM-1v:</strong> <div class="method-query-example"> <strong>query by phenotype identifier</strong>  <ul> <li>phenotype_id = GO_0003674</li> <li>method = ESM-1v</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI8105TNNO</li> <li>method = ESM-1v</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="mutpred2"> <strong>MutPred2:</strong> <div class="method-query-example"> <strong>query by phenotype identifier</strong>  <ul> <li>phenotype_id = GO_0003674</li> <li>method = MutPred2</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI6893ZOAA</li> <li>method = MutPred2</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sge"> <strong>SGE:</strong> <div class="method-query-example"> <strong>query by phenotype identifier</strong>  <ul> <li>phenotype_id = NCIT_C16407</li> <li>method = SGE</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI2810SLAX</li> <li>method = SGE</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="vamp-seq"> <strong>VAMP-seq:</strong> <div class="method-query-example"> <strong>query by phenotype identifier</strong>  <ul> <li>phenotype_id = OBA_0000128</li> <li>method = VAMP-seq</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI0629IIQU</li> <li>method = VAMP-seq</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="variant-painting"> <strong>Variant painting via fluorescence:</strong> <div class="method-query-example"> <strong>query by phenotype identifier</strong>  <ul> <li>phenotype_id = GO_0008104</li> <li>method = Variant painting via fluorescence</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI9499PJFU</li> <li>method = Variant painting via fluorescence</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.phenotypes_from_coding_variants200_response_inner import PhenotypesFromCodingVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    phenotype_id = 'phenotype_id_example' # str |  (optional)
    phenotype_name = 'phenotype_name_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.coding_variants_from_phenotypes(phenotype_id=phenotype_id, phenotype_name=phenotype_name, method=method, files_fileset=files_fileset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->coding_variants_from_phenotypes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->coding_variants_from_phenotypes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phenotype_id** | **str**|  | [optional] 
 **phenotype_name** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PhenotypesFromCodingVariants200ResponseInner]**](PhenotypesFromCodingVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coding_variants_from_variants**
> List[CodingVariantsFromVariants200ResponseInner] coding_variants_from_variants(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, page=page, limit=limit)

Retrieve coding variants from dbSNFP associated with a variant.<br>     Example: variant_id = NC_000001.11:65564:A:T, <br>     spdi = NC_000001.11:65564:A:T, <br>     hgvs = NC_000001.11:g.65565A>T, <br>     ca_id = CA337806511, <br>     The limit parameter controls the page size and can not exceed 500.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.coding_variants_from_variants200_response_inner import CodingVariantsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.coding_variants_from_variants(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, page=page, limit=limit)
        print("The response of IgvfCatalogApi->coding_variants_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->coding_variants_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[CodingVariantsFromVariants200ResponseInner]**](CodingVariantsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coding_variants_summary**
> List[DeprecatedCodingVariantsSummary200ResponseInner] coding_variants_summary(variant_id=variant_id, coding_variant_id=coding_variant_id, files_fileset=files_fileset)

Retrieve scores of variants or coding_variants associated with phenotypes. Via coding variants edges.<br>     Either variant_id or coding_variant_name are required. <br>     Example: variant_id = NC_000018.10:31546002:CA:GT, <br>     coding_variant_name = DSG2_ENST00000261590_p.Gln873Val_c.2617_2618delinsGT, <br>     files_fileset = IGVFFI6893ZOAA.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.deprecated_coding_variants_summary200_response_inner import DeprecatedCodingVariantsSummary200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    variant_id = 'variant_id_example' # str |  (optional)
    coding_variant_id = 'coding_variant_id_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)

    try:
        api_response = api_instance.coding_variants_summary(variant_id=variant_id, coding_variant_id=coding_variant_id, files_fileset=files_fileset)
        print("The response of IgvfCatalogApi->coding_variants_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->coding_variants_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_id** | **str**|  | [optional] 
 **coding_variant_id** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 

### Return type

[**List[DeprecatedCodingVariantsSummary200ResponseInner]**](DeprecatedCodingVariantsSummary200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complexes**
> List[ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1] complexes(complex_id=complex_id, name=name, description=description, page=page)

Retrieve complexes.<br>   Example: complex_id = CPX-11, <br>   name = SMAD2, <br>   description = phosphorylation. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_variants200_response_inner_protein_complex_any_of1 import ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    complex_id = 'complex_id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)

    try:
        api_response = api_instance.complexes(complex_id=complex_id, name=name, description=description, page=page)
        print("The response of IgvfCatalogApi->complexes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->complexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]

### Return type

[**List[ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1]**](ProteinsFromVariants200ResponseInnerProteinComplexAnyOf1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complexes_from_proteins**
> List[ComplexesFromProteins200ResponseInner] complexes_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve complexes by querying from protein participants. Each record includes protein and complex.<br>   Set verbose = true to retrieve full info on the complexes.<br>   Protein IDs support the following formats: ENSP00000411322.1 or ENSP00000411322 (Ensembl IDs) or P67870 (Uniprot ids)<br>   Example: protein_id = ENSP00000411322.1, <br>   protein_name = CSNK2B, <br>   uniprot_name = CSK2B_HUMAN, <br>   uniprot_full_name = Casein kinase II subunit beta, <br>   dbxrefs = P67870. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.complexes_from_proteins200_response_inner import ComplexesFromProteins200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    protein_id = 'protein_id_example' # str |  (optional)
    protein_name = 'protein_name_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    uniprot_full_name = 'uniprot_full_name_example' # str |  (optional)
    dbxrefs = 'dbxrefs_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.complexes_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->complexes_from_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->complexes_from_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protein_id** | **str**|  | [optional] 
 **protein_name** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **uniprot_full_name** | **str**|  | [optional] 
 **dbxrefs** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ComplexesFromProteins200ResponseInner]**](ComplexesFromProteins200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecated_coding_variants_summary**
> List[DeprecatedCodingVariantsSummary200ResponseInner] deprecated_coding_variants_summary(variant_id=variant_id, coding_variant_id=coding_variant_id, files_fileset=files_fileset)

DEPRECATED. Please use coding-variants/phenotypes/summary.<br>     Retrieve scores of variants associated with phenotypes. Via coding variants edges.<br>     Either variant_id or coding_variant_name are required. <br>     Example: variant_id = NC_000018.10:31546002:CA:GT, <br>     coding_variant_name = DSG2_ENST00000261590_p.Gln873Val_c.2617_2618delinsGT, <br>     files_fileset = IGVFFI6893ZOAA.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.deprecated_coding_variants_summary200_response_inner import DeprecatedCodingVariantsSummary200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    variant_id = 'variant_id_example' # str |  (optional)
    coding_variant_id = 'coding_variant_id_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)

    try:
        api_response = api_instance.deprecated_coding_variants_summary(variant_id=variant_id, coding_variant_id=coding_variant_id, files_fileset=files_fileset)
        print("The response of IgvfCatalogApi->deprecated_coding_variants_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->deprecated_coding_variants_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_id** | **str**|  | [optional] 
 **coding_variant_id** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 

### Return type

[**List[DeprecatedCodingVariantsSummary200ResponseInner]**](DeprecatedCodingVariantsSummary200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disease_from_variants**
> List[DiseaseFromVariants200ResponseInner] disease_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, assertion=assertion, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve diseases and genes associated with the query variant from ClinGen. <br>   At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, or region. <br>   Example: variant_id = NC_000012.12:102917129:T:C <br>   spdi = NC_000012.12:102917129:T:C, <br>   hgvs = NC_000012.12:g.102917130T>C, <br>   rsid = rs62514891, <br>   ca_id = CA114360, <br>   chr = chr12, <br>   region = chr12:102866500-102866700 (maximum length: 10kb), <br>   assertion = Pathogenic, <br>   pmid = 2574002. <br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.disease_from_variants200_response_inner import DiseaseFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    assertion = 'assertion_example' # str |  (optional)
    pmid = 'pmid_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.disease_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, assertion=assertion, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->disease_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->disease_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **assertion** | **str**|  | [optional] 
 **pmid** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[DiseaseFromVariants200ResponseInner]**](DiseaseFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diseases_from_genes**
> List[DiseasesFromGenes200ResponseInner] diseases_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, source=source, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve disease-gene pairs from Orphanet, GenCC and ClinGen by genes.<br>     Set verbose = true to retrieve full info on the disease terms, and the variants associated with the disease from ClinGen. <br>     At least one of these fields is required: gene_id, hgnc_id, gene_name, synonym. <br>     Example: gene_id = ENSG00000171759, <br>     gene_name = PAH, <br>     synonym = PKU1, <br>     source = ClinGen, <br>     hgnc_id = HGNC:8582. <br>     The limit parameter controls the page size and can not exceed 25. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.diseases_from_genes200_response_inner import DiseasesFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.diseases_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, source=source, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->diseases_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->diseases_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[DiseasesFromGenes200ResponseInner]**](DiseasesFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drugs**
> List[DrugsFromVariants200ResponseInnerDrugAnyOf] drugs(drug_id=drug_id, name=name, page=page, limit=limit)

Retrieve drugs (chemicals). <br>   Example: drug_id = PA448497 (chemical ids from pharmGKB), <br>   name = aspirin.<br>   The limit parameter controls the page size and can not exceed 1000. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.drugs_from_variants200_response_inner_drug_any_of import DrugsFromVariants200ResponseInnerDrugAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    drug_id = 'drug_id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.drugs(drug_id=drug_id, name=name, page=page, limit=limit)
        print("The response of IgvfCatalogApi->drugs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->drugs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drug_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[DrugsFromVariants200ResponseInnerDrugAnyOf]**](DrugsFromVariants200ResponseInnerDrugAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drugs_from_variants**
> List[DrugsFromVariants200ResponseInner] drugs_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, phenotype_categories=phenotype_categories, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve drugs associated with the query variants from pharmGKB.<br>   Set verbose = true to retrieve full info on the drugs.<br>   At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, or region. <br>   Example: variant_id = NC_000001.11:230714139:T:G, <br>   spdi = NC_000001.11:230714139:T:G, <br>   hgvs = NC_000001.11:g.230714140T>G, <br>   rsid = rs5050 (at least one of the variant fields needs to be specified), <br>   ca_id = CA10610220, <br>   region = chr3:186741137-186742238 (maximum length: 10kb), <br>   the following filters on variants-drugs association can be combined for query: <br>   pmid = 20824505, <br>   phenotype_categories = Toxicity. <br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.drugs_from_variants200_response_inner import DrugsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    phenotype_categories = 'phenotype_categories_example' # str |  (optional)
    pmid = 'pmid_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.drugs_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, phenotype_categories=phenotype_categories, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->drugs_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->drugs_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **phenotype_categories** | **str**|  | [optional] 
 **pmid** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[DrugsFromVariants200ResponseInner]**](DrugsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enhancer_gene_predictions**
> List[EnhancerGenePredictions200ResponseInner] enhancer_gene_predictions(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, method=method, files_fileset=files_fileset, page=page, limit=limit)

Retrieve genomic elements and gene pairs by querying genomic elements.<br>     Set verbose = true to retrieve full info on the genes, genomic element and biosamples.<br>     method can be either ENCODE-rE2G or scE2G; if not provided, both methods are searched. <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based. <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="encode-re2g">ENCODE-rE2G</button> <button class="method-example-tab" data-method-example-tab="sce2g">scE2G</button> </div> <div class="method-example-panel is-active" data-method-example-panel="encode-re2g"> <strong>ENCODE-rE2G:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000055950</li> <li>method = ENCODE-rE2G</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sce2g"> <strong>scE2G:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000055950</li> <li>method = scE2G</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.enhancer_gene_predictions200_response_inner import EnhancerGenePredictions200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.enhancer_gene_predictions(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, method=method, files_fileset=files_fileset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->enhancer_gene_predictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->enhancer_gene_predictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[EnhancerGenePredictions200ResponseInner]**](EnhancerGenePredictions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_filesets**
> List[FilesFilesets200ResponseInner] files_filesets(file_fileset_id=file_fileset_id, fileset_id=fileset_id, lab=lab, preferred_assay_title=preferred_assay_title, method=method, crispr_modality=crispr_modality, donor_id=donor_id, sample_term=sample_term, sample_summary=sample_summary, software=software, cell_annotation=cell_annotation, cell_annotation_term=cell_annotation_term, has_genome_browser_link=has_genome_browser_link, source=source, var_class=var_class, page=page, limit=limit)

Retrieve data about a specific dataset.<br>   Example: file_fileset_id = ENCFF004PFU,<br>  fileset_id = ENCSR359DFW,<br>  lab = jesse-engreitz,<br>  preferred_assay_title = DNase-seq,<br>  method = MPRA,<br>  donor_id = ENCDO000AAK,<br>  sample_term = EFO_0002784,<br>  sample_summary = GM12878,<br>  software = Distal regulation ENCODE-rE2G,<br>  cell_annotation = mesodermal cell, <br>  cell_annotation_term = CL_0000352, <br>  class = prediction,<br>  source = ENCODE.<br>  The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.files_filesets200_response_inner import FilesFilesets200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    file_fileset_id = 'file_fileset_id_example' # str |  (optional)
    fileset_id = 'fileset_id_example' # str |  (optional)
    lab = 'lab_example' # str |  (optional)
    preferred_assay_title = 'preferred_assay_title_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    crispr_modality = 'crispr_modality_example' # str |  (optional)
    donor_id = 'donor_id_example' # str |  (optional)
    sample_term = 'sample_term_example' # str |  (optional)
    sample_summary = 'sample_summary_example' # str |  (optional)
    software = 'software_example' # str |  (optional)
    cell_annotation = 'cell_annotation_example' # str |  (optional)
    cell_annotation_term = 'cell_annotation_term_example' # str |  (optional)
    has_genome_browser_link = 'has_genome_browser_link_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    var_class = 'var_class_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.files_filesets(file_fileset_id=file_fileset_id, fileset_id=fileset_id, lab=lab, preferred_assay_title=preferred_assay_title, method=method, crispr_modality=crispr_modality, donor_id=donor_id, sample_term=sample_term, sample_summary=sample_summary, software=software, cell_annotation=cell_annotation, cell_annotation_term=cell_annotation_term, has_genome_browser_link=has_genome_browser_link, source=source, var_class=var_class, page=page, limit=limit)
        print("The response of IgvfCatalogApi->files_filesets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->files_filesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_fileset_id** | **str**|  | [optional] 
 **fileset_id** | **str**|  | [optional] 
 **lab** | **str**|  | [optional] 
 **preferred_assay_title** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **crispr_modality** | **str**|  | [optional] 
 **donor_id** | **str**|  | [optional] 
 **sample_term** | **str**|  | [optional] 
 **sample_summary** | **str**|  | [optional] 
 **software** | **str**|  | [optional] 
 **cell_annotation** | **str**|  | [optional] 
 **cell_annotation_term** | **str**|  | [optional] 
 **has_genome_browser_link** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **var_class** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[FilesFilesets200ResponseInner]**](FilesFilesets200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes**
> List[GenesFromVariants200ResponseInnerGeneAnyOf] genes(gene_id=gene_id, hgnc_id=hgnc_id, entrez=entrez, name=name, region=region, synonym=synonym, collection=collection, study_set=study_set, gene_type=gene_type, organism=organism, page=page, limit=limit)

Retrieve genes.<br>   Example: organism = Homo sapiens, <br>   name = SAMD1, <br>   region = chr1:212565300-212620800, <br>   synonym = CKLF, <br>   collection = ACMG73, <br>   study_set = MorPhiC, <br>   gene_id = ENSG00000187642 (Ensembl ids), <br>   gene_type = protein_coding, <br>   hgnc_id = HGNC:28208, <br>   entrez = ENTREZ:84808. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_from_variants200_response_inner_gene_any_of import GenesFromVariants200ResponseInnerGeneAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    entrez = 'entrez_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    collection = 'collection_example' # str |  (optional)
    study_set = 'study_set_example' # str |  (optional)
    gene_type = 'gene_type_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes(gene_id=gene_id, hgnc_id=hgnc_id, entrez=entrez, name=name, region=region, synonym=synonym, collection=collection, study_set=study_set, gene_type=gene_type, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **entrez** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **collection** | **str**|  | [optional] 
 **study_set** | **str**|  | [optional] 
 **gene_type** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesFromVariants200ResponseInnerGeneAnyOf]**](GenesFromVariants200ResponseInnerGeneAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_from_diseases**
> List[DiseasesFromGenes200ResponseInner] genes_from_diseases(disease_id=disease_id, disease_name=disease_name, source=source, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve disease-gene pairs from Orphanet and GenCC by diseases.<br>     Set verbose = true to retrieve full info on the genes and diseases. <br>     Example: disease_name = fibrosis, <br>     disease_id = Orphanet_586, <br>     source = Orphanet. <br>     Either disease_name or disease_id are required. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.diseases_from_genes200_response_inner import DiseasesFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    disease_id = 'disease_id_example' # str |  (optional)
    disease_name = 'disease_name_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_from_diseases(disease_id=disease_id, disease_name=disease_name, source=source, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_from_diseases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_from_diseases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disease_id** | **str**|  | [optional] 
 **disease_name** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[DiseasesFromGenes200ResponseInner]**](DiseasesFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_from_genomic_elements**
> List[GenomicElementsFromGenes200ResponseInner] genes_from_genomic_elements(region=region, source_annotation=source_annotation, region_type=region_type, method=method, files_fileset=files_fileset, biosample_term=biosample_term, biological_context=biological_context, cell_annotation=cell_annotation, cell_annotation_term=cell_annotation_term, source=source, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genomic elements and gene pairs by querying genomic elements.<br>     At least one of these properties must be defined: region, files_fileset, or method. <br>     Set verbose = true to retrieve full info on the genes and genomic element.<br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="crispr-screen">CRISPR screen</button> <button class="method-example-tab" data-method-example-tab="encode-re2g">ENCODE-rE2G</button> <button class="method-example-tab" data-method-example-tab="perturb-seq">Perturb-seq</button> <button class="method-example-tab" data-method-example-tab="sce2g">scE2G</button> </div> <div class="method-example-panel is-active" data-method-example-panel="crispr-screen"> <strong>CRISPR screen:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>region = chr1:4126791-4126792 (maximum length: 10kb)</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>files_fileset = ENCFF968BZL</li> <li>method = CRISPR screen</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="encode-re2g"> <strong>ENCODE-rE2G:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>region = chr1:920016-920017 (maximum length: 10kb)</li> <li>method = ENCODE-rE2G</li> <li>files_fileset = ENCFF666WIM</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>files_fileset = ENCFF666WIM</li> <li>method = ENCODE-rE2G</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="perturb-seq"> <strong>Perturb-seq:</strong> <div class="method-query-example"> <strong>Query by region</strong>  <ul> <li>region = chr1:212699339-212700840 (maximum length: 10kb)</li> <li>method = Perturb-seq</li> </ul> </div> <div class="method-query-example"> <strong>Query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI3069QCRA</li> <li>method = Perturb-seq</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sce2g"> <strong>scE2G:</strong> <div class="method-query-example"> <strong>Query by region</strong>  <ul> <li>region = chr1:169893055-169894554 (maximum length: 10kb)</li> <li>method = scE2G</li> </ul> </div> <div class="method-query-example"> <strong>Query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI4235YTNW</li> <li>method = scE2G</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genomic_elements_from_genes200_response_inner import GenomicElementsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str |  (optional)
    source_annotation = 'source_annotation_example' # str |  (optional)
    region_type = 'region_type_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    biosample_term = 'biosample_term_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    cell_annotation = 'cell_annotation_example' # str |  (optional)
    cell_annotation_term = 'cell_annotation_term_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_from_genomic_elements(region=region, source_annotation=source_annotation, region_type=region_type, method=method, files_fileset=files_fileset, biosample_term=biosample_term, biological_context=biological_context, cell_annotation=cell_annotation, cell_annotation_term=cell_annotation_term, source=source, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_from_genomic_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_from_genomic_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | [optional] 
 **source_annotation** | **str**|  | [optional] 
 **region_type** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **biosample_term** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **cell_annotation** | **str**|  | [optional] 
 **cell_annotation_term** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenomicElementsFromGenes200ResponseInner]**](GenomicElementsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_from_pathways**
> List[PathwaysFromGenes200ResponseInner] genes_from_pathways(pathway_id=pathway_id, pathway_name=pathway_name, name_aliases=name_aliases, disease_ontology_terms=disease_ontology_terms, go_biological_process=go_biological_process, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genes from pathways.<br>   Set verbose = true to retrieve full info on the genes. <br>   At least one of these fields is required: pathway_id, pathway_name, or name_aliases <br>   Example: pathway_id = R-HSA-164843, <br>   pathway_name = 2-LTR circle formation, <br>   name_aliases = 2-LTR circle formation, <br>   disease_ontology_terms = DOID_526, <br>   go_biological_process = GO_0006015. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.pathways_from_genes200_response_inner import PathwaysFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    pathway_id = 'pathway_id_example' # str |  (optional)
    pathway_name = 'pathway_name_example' # str |  (optional)
    name_aliases = 'name_aliases_example' # str |  (optional)
    disease_ontology_terms = 'disease_ontology_terms_example' # str |  (optional)
    go_biological_process = 'go_biological_process_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_from_pathways(pathway_id=pathway_id, pathway_name=pathway_name, name_aliases=name_aliases, disease_ontology_terms=disease_ontology_terms, go_biological_process=go_biological_process, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_from_pathways:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_from_pathways: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pathway_id** | **str**|  | [optional] 
 **pathway_name** | **str**|  | [optional] 
 **name_aliases** | **str**|  | [optional] 
 **disease_ontology_terms** | **str**|  | [optional] 
 **go_biological_process** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PathwaysFromGenes200ResponseInner]**](PathwaysFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_from_proteins**
> List[ProteinsFromGenes200ResponseInner] genes_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genes from proteins.<br>   Set verbose = true to retrieve full info on the genes.<br>   Protein IDs support the following formats: ENSP00000384707.1 or ENSP00000384707 (Ensembl IDs) or P49711-2 (Uniprot ids)<br>   Example: protein_id = ENSP00000384707, <br>   protein_name = CTCF, <br>   uniprot_name = CTCF_HUMAN, <br>   uniprot_full_name = Transcriptional repressor CTCF, <br>   dbxrefs = P49711, <br>   organism = Homo sapiens. <br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_genes200_response_inner import ProteinsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    protein_id = 'protein_id_example' # str |  (optional)
    protein_name = 'protein_name_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    uniprot_full_name = 'uniprot_full_name_example' # str |  (optional)
    dbxrefs = 'dbxrefs_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_from_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_from_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protein_id** | **str**|  | [optional] 
 **protein_name** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **uniprot_full_name** | **str**|  | [optional] 
 **dbxrefs** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromGenes200ResponseInner]**](ProteinsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_from_transcripts**
> List[TranscriptsFromGenes200ResponseInner] genes_from_transcripts(transcript_id=transcript_id, region=region, transcript_type=transcript_type, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genes from transcripts.<br>     Set verbose = true to retrieve full info on the genes.<br>     At least one of these fields is required: transcript_id, region or transcript_type. <br>     Example: transcript_id = ENST00000440782, <br>     region = chr1:711800-740000, <br>     transcript_type = protein_coding,<br>     organism = Homo sapiens, <br>     transcript_id = ENST00000443707 (Ensembl ID). <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.transcripts_from_genes200_response_inner import TranscriptsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    transcript_id = 'transcript_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    transcript_type = 'transcript_type_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_from_transcripts(transcript_id=transcript_id, region=region, transcript_type=transcript_type, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_from_transcripts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_from_transcripts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcript_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **transcript_type** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[TranscriptsFromGenes200ResponseInner]**](TranscriptsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_from_variants**
> List[GenesFromVariants200ResponseInner] genes_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, neg_log10_pvalue=neg_log10_pvalue, effect_size=effect_size, posterior_inclusion_probability=posterior_inclusion_probability, log2_fc=log2_fc, significant=significant, biosample_term=biosample_term, biological_context=biological_context, label=label, method=method, files_fileset=files_fileset, source=source, name=name, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve variant-gene pairs including eQTLs & splice QTLs from AFGR and eQTL Catalogue, and CRISPR screen and Variant-EFFECTS from IGVF, by variants.<br>     The following parameters can be used to set thresholds on -log10 p_value: gt (>), gte (>=), lt (<), lte (<=).<br>     posterior_inclusion_probability and log2FC also accept plain numbers (exact match) or the same gt/gte/lt/lte range syntax. significant only accepts true (omit the parameter to not filter on it).<br>     Set verbose = true to retrieve full info on the corresponding variants and genes.<br>     At least one of these properties must be defined: spdi, hgvs, rsid, ca_id, variant_id, region, method, or files_filesets. <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="eqtl">eQTL</button> <button class="method-example-tab" data-method-example-tab="spliceqtl">spliceQTL</button> <button class="method-example-tab" data-method-example-tab="variant-effects">Variant-EFFECTS</button> <button class="method-example-tab" data-method-example-tab="crispr-screen">CRISPR screen</button> </div> <div class="method-example-panel is-active" data-method-example-panel="eqtl"> <strong>eQTL:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>spdi = NC_000001.11:40241653:TGAA:TGAAATTGAA</li> <li>effect_size = gte:0.3</li> <li>method = eQTL</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>region = chr1:40241650-40241759 (maximum length: 10kb)</li> <li>method = eQTL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="spliceqtl"> <strong>spliceQTL:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>spdi = NC_000001.11:898757:AAAAAA:AAAAAAA</li> <li>effect_size = gte:0.3</li> <li>method = spliceQTL</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>region = chr1:898750-898759 (maximum length: 10kb)</li> <li>method = spliceQTL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="variant-effects"> <strong>Variant-EFFECTS:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>spdi = NC_000010.11:79347741:AGGT:TCAG</li> <li>effect_size = lt:-0.6</li> <li>method = Variant-EFFECTS</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>region = chr10:79347740-79347749 (maximum length: 10kb)</li> <li>method = Variant-EFFECTS</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="crispr-screen"> <strong>CRISPR screen:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000016.10:28930710:G:A</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr16:28930700-28930800 (maximum length: 10kb)</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>query by significance thresholds</strong>  <ul> <li>region = chr16:28930700-28930800 (maximum length: 10kb)</li> <li>posterior_inclusion_probability = gte:0.1</li> <li>log2FC = lt:-0.5</li> <li>significant = true</li> <li>method = CRISPR screen</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_from_variants200_response_inner import GenesFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    neg_log10_pvalue = 'neg_log10_pvalue_example' # str |  (optional)
    effect_size = 'effect_size_example' # str |  (optional)
    posterior_inclusion_probability = 'posterior_inclusion_probability_example' # str |  (optional)
    log2_fc = 'log2_fc_example' # str |  (optional)
    significant = 'significant_example' # str |  (optional)
    biosample_term = 'biosample_term_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, neg_log10_pvalue=neg_log10_pvalue, effect_size=effect_size, posterior_inclusion_probability=posterior_inclusion_probability, log2_fc=log2_fc, significant=significant, biosample_term=biosample_term, biological_context=biological_context, label=label, method=method, files_fileset=files_fileset, source=source, name=name, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **neg_log10_pvalue** | **str**|  | [optional] 
 **effect_size** | **str**|  | [optional] 
 **posterior_inclusion_probability** | **str**|  | [optional] 
 **log2_fc** | **str**|  | [optional] 
 **significant** | **str**|  | [optional] 
 **biosample_term** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesFromVariants200ResponseInner]**](GenesFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_genes**
> List[GenesGenes200ResponseInner] genes_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, associated_gene_id=associated_gene_id, associated_hgnc_id=associated_hgnc_id, associated_gene_name=associated_gene_name, associated_synonym=associated_synonym, z_score=z_score, interaction_type=interaction_type, label=label, method=method, source=source, name=name, files_fileset=files_fileset, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve coexpressed gene pairs from CoXPresdb and genetic interactions from BioGRID. <br>     The following parameters can be used to set thresholds on z_score from CoXPresdb: gt (>), gte (>=), lt (<), lte (<=).<br>     At least one of these fields is required: gene_id, hgnc_id, gene_name, synonym. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by source</strong> <p class="method-example-description">These examples are grouped by source; use the <code>source</code> filter to return data from a specific source.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="biogrid">BioGRID</button> <button class="method-example-tab" data-method-example-tab="coxpresdb">COXPRESdb</button> </div> <div class="method-example-panel is-active" data-method-example-panel="biogrid"> <strong>BioGRID:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>gene_id = ENSG00000112592</li> <li>associated_gene_id = ENSG00000163132</li> <li>source = BioGRID</li> <li>files_fileset = IGVFFI4317VDGK</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_id = ENSG00000112592</li> <li>source = BioGRID</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="coxpresdb"> <strong>COXPRESdb:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>gene_id = ENSG00000153048</li> <li>associated_gene_id = ENSG00000233369</li> <li>source = COXPRESdb</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_id = ENSG00000153048</li> <li>source = COXPRESdb</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_genes200_response_inner import GenesGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    associated_gene_id = 'associated_gene_id_example' # str |  (optional)
    associated_hgnc_id = 'associated_hgnc_id_example' # str |  (optional)
    associated_gene_name = 'associated_gene_name_example' # str |  (optional)
    associated_synonym = 'associated_synonym_example' # str |  (optional)
    z_score = 'z_score_example' # str |  (optional)
    interaction_type = 'interaction_type_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, associated_gene_id=associated_gene_id, associated_hgnc_id=associated_hgnc_id, associated_gene_name=associated_gene_name, associated_synonym=associated_synonym, z_score=z_score, interaction_type=interaction_type, label=label, method=method, source=source, name=name, files_fileset=files_fileset, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **associated_gene_id** | **str**|  | [optional] 
 **associated_hgnc_id** | **str**|  | [optional] 
 **associated_gene_name** | **str**|  | [optional] 
 **associated_synonym** | **str**|  | [optional] 
 **z_score** | **str**|  | [optional] 
 **interaction_type** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesGenes200ResponseInner]**](GenesGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_proteins_from_variants**
> List[GenesProteinsFromVariants200ResponseInner] genes_proteins_from_variants(variant_id, page=page, limit=limit)

Retrieve genes and proteins associated with a variant matched by ID. <br>   Example: variant_id = NC_000001.11:630556:T:C<br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_proteins_from_variants200_response_inner import GenesProteinsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    variant_id = 'variant_id_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_proteins_from_variants(variant_id, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_proteins_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_proteins_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesProteinsFromVariants200ResponseInner]**](GenesProteinsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_proteins_genes_proteins**
> List[GenesProteinsGenesProteins200ResponseInner] genes_proteins_genes_proteins(query, page=page, limit=limit)

Retrieve genes or proteins associated with either genes or proteins that match a query. <br>   Example: query = ATF1.<br>   The limit parameter controls the page size of related items and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_proteins_genes_proteins200_response_inner import GenesProteinsGenesProteins200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    query = 'query_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_proteins_genes_proteins(query, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_proteins_genes_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_proteins_genes_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesProteinsGenesProteins200ResponseInner]**](GenesProteinsGenesProteins200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes_structure**
> List[GenesStructure200ResponseInner] genes_structure(gene_id=gene_id, gene_name=gene_name, transcript_id=transcript_id, transcript_name=transcript_name, protein_id=protein_id, protein_name=protein_name, region=region, type=type, organism=organism, page=page, limit=limit)

Retrieve genes structure.<br>   you can filter by one of the four categories: gene, transcript, protein or region. <br>   Example: organism = Homo sapiens, <br>   region = chr1:212565300-212620800, <br>   gene_id = ENSG00000187642 (Ensembl ids), <br>   gene_name = ATF3, <br>   transcript_id = ENST00000443707 (Ensembl ids), <br>   type = exon, <br>   protein_id = ENSP00000305769, <br>   protein_name = SMAD1. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_structure200_response_inner import GenesStructure200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    transcript_id = 'transcript_id_example' # str |  (optional)
    transcript_name = 'transcript_name_example' # str |  (optional)
    protein_id = 'protein_id_example' # str |  (optional)
    protein_name = 'protein_name_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genes_structure(gene_id=gene_id, gene_name=gene_name, transcript_id=transcript_id, transcript_name=transcript_name, protein_id=protein_id, protein_name=protein_name, region=region, type=type, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genes_structure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genes_structure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **transcript_id** | **str**|  | [optional] 
 **transcript_name** | **str**|  | [optional] 
 **protein_id** | **str**|  | [optional] 
 **protein_name** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesStructure200ResponseInner]**](GenesStructure200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genomic_elements**
> List[GenomicElements200ResponseInner] genomic_elements(region=region, source_annotation=source_annotation, type=type, method=method, source=source, organism=organism, page=page, limit=limit, files_fileset=files_fileset)

Retrieve genomic elements.<br>   Example: region = chr1:1157520-1158189, <br>   source_annotation = dELS: distal Enhancer-like signal, <br>   type = candidate cis regulatory element, <br>   files_fileset = IGVFFI5749WPVK, <br>   source = ENCODE. <br>   The limit parameter controls the page size and can not exceed 1000. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genomic_elements200_response_inner import GenomicElements200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str |  (optional)
    source_annotation = 'source_annotation_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)

    try:
        api_response = api_instance.genomic_elements(region=region, source_annotation=source_annotation, type=type, method=method, source=source, organism=organism, page=page, limit=limit, files_fileset=files_fileset)
        print("The response of IgvfCatalogApi->genomic_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genomic_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | [optional] 
 **source_annotation** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 

### Return type

[**List[GenomicElements200ResponseInner]**](GenomicElements200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genomic_elements_from_biosamples**
> List[BiosamplesFromGenomicElements200ResponseInner] genomic_elements_from_biosamples(biosample_name=biosample_name, method=method, source=source, files_fileset=files_fileset, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve MPRA expriments by querying cell ontology terms. <br>   Set verbose = true to retrieve full info on the tested genomic elements. <br>   Example: biosample_name = hepg2, <br>   method = MPRA, <br>   source = IGVF, <br>   files_fileset = ENCFF475FKV. <br>   The limit parameter controls the page size and can not exceed 50. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.biosamples_from_genomic_elements200_response_inner import BiosamplesFromGenomicElements200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    biosample_name = 'biosample_name_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genomic_elements_from_biosamples(biosample_name=biosample_name, method=method, source=source, files_fileset=files_fileset, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genomic_elements_from_biosamples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genomic_elements_from_biosamples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biosample_name** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[BiosamplesFromGenomicElements200ResponseInner]**](BiosamplesFromGenomicElements200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genomic_elements_from_genes**
> List[GenomicElementsFromGenes200ResponseInner] genomic_elements_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, method=method, files_fileset=files_fileset, biosample_term=biosample_term, biological_context=biological_context, cell_annotation=cell_annotation, cell_annotation_term=cell_annotation_term, source=source, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genomic elements and gene pairs by querying genes.<br>     One of these fields is required: gene_id, hgnc_id, gene_name, synonym, method, or files_fileset. <br>     Set verbose = true to retrieve full info on the genes and genomic element.<br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="crispr-screen">CRISPR screen</button> <button class="method-example-tab" data-method-example-tab="encode-re2g">ENCODE-rE2G</button> <button class="method-example-tab" data-method-example-tab="perturb-seq">Perturb-seq</button> <button class="method-example-tab" data-method-example-tab="sce2g">scE2G</button> </div> <div class="method-example-panel is-active" data-method-example-panel="crispr-screen"> <strong>CRISPR screen:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>gene_id = ENSG00000116198</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>method = CRISPR screen</li> <li>files_fileset = ENCFF968BZL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="encode-re2g"> <strong>ENCODE-rE2G:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000225880</li> <li>biosample_term = EFO_0002330</li> <li>method = ENCODE-rE2G</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = ENCFF425TLX</li> <li>method = ENCODE-rE2G</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="perturb-seq"> <strong>Perturb-seq:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000123685</li> <li>method = Perturb-seq</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI3069QCRA</li> <li>method = Perturb-seq</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sce2g"> <strong>scE2G:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000156875</li> <li>method = scE2G</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI4235YTNW</li> <li>method = scE2G</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genomic_elements_from_genes200_response_inner import GenomicElementsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    biosample_term = 'biosample_term_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    cell_annotation = 'cell_annotation_example' # str |  (optional)
    cell_annotation_term = 'cell_annotation_term_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genomic_elements_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, method=method, files_fileset=files_fileset, biosample_term=biosample_term, biological_context=biological_context, cell_annotation=cell_annotation, cell_annotation_term=cell_annotation_term, source=source, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genomic_elements_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genomic_elements_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **biosample_term** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **cell_annotation** | **str**|  | [optional] 
 **cell_annotation_term** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenomicElementsFromGenes200ResponseInner]**](GenomicElementsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genomic_elements_from_phenotypes**
> List[PhenotypesFromGenomicElements200ResponseInner] genomic_elements_from_phenotypes(files_fileset=files_fileset, phenotype_id=phenotype_id, phenotype_name=phenotype_name, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genomic elements associated with phenotypes.<br>     At least one of these properties must be defined: phenotype_id, phenotype_name, or files_fileset. <br>     Set significant = true to return only significant associations.<br>     Set verbose = true to retrieve full info on the genomic element.<br>     Example: phenotype_id = GO_0008283, <br>     phenotype_name = cell population proliferation, <br>     significant = true, <br>     files_fileset = IGVFFI9584UDAS. <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.phenotypes_from_genomic_elements200_response_inner import PhenotypesFromGenomicElements200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    files_fileset = 'files_fileset_example' # str |  (optional)
    phenotype_id = 'phenotype_id_example' # str |  (optional)
    phenotype_name = 'phenotype_name_example' # str |  (optional)
    significant = 'significant_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genomic_elements_from_phenotypes(files_fileset=files_fileset, phenotype_id=phenotype_id, phenotype_name=phenotype_name, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genomic_elements_from_phenotypes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genomic_elements_from_phenotypes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files_fileset** | **str**|  | [optional] 
 **phenotype_id** | **str**|  | [optional] 
 **phenotype_name** | **str**|  | [optional] 
 **significant** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PhenotypesFromGenomicElements200ResponseInner]**](PhenotypesFromGenomicElements200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genomic_elements_from_variants**
> List[GenomicElementsFromVariants200ResponseInner] genomic_elements_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, biosample_term=biosample_term, biological_context=biological_context, method=method, files_fileset=files_fileset, page=page, limit=limit)

Retrieve genomic elements associated with a given variant.<br>   Example: variant_id = NC_000001.11:976214:A:G, <br>   hgvs = NC_000001.11:g.976215A>G,<br>   spdi = NC_000001.11:976214:A:G, <br>   rsid = rs7417106, <br>   ca_id = CA507079, <br>   region = chr1:766254-766554, <br>   biosample_term = EFO_0002067, <br>   biological_context = K562, <br>   method = caQTL, <br>   files_fileset = ENCFF103XRK, <br>   The limit parameter controls the page size and can not exceed 300. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genomic_elements_from_variants200_response_inner import GenomicElementsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    biosample_term = 'biosample_term_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.genomic_elements_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, biosample_term=biosample_term, biological_context=biological_context, method=method, files_fileset=files_fileset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->genomic_elements_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genomic_elements_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **biosample_term** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenomicElementsFromVariants200ResponseInner]**](GenomicElementsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genomic_elements_from_variants_count**
> object genomic_elements_from_variants_count(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, files_fileset=files_fileset)

Retrieve counts of element gene predictions and cell types associated with a given variant.<br>   At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, or files_filesets. <br>   Example: variant_id = NC_000001.11:1628997:GGG:GG,<br>   hgvs = NC_000001.11:g.1629000del,<br>   spdi = NC_000001.11:1628997:GGG:GG,<br>   ca_id = CA1522823495,<br>   files_fileset = ENCFF705MLV.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    files_fileset = 'files_fileset_example' # str |  (optional)

    try:
        api_response = api_instance.genomic_elements_from_variants_count(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, files_fileset=files_fileset)
        print("The response of IgvfCatalogApi->genomic_elements_from_variants_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genomic_elements_from_variants_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **files_fileset** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genomic_elements_predictions_from_variant**
> GenomicElementsPredictionsFromVariant200Response genomic_elements_predictions_from_variant(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region)

Retrieve predicted associated genes and cell types for a given variant. <br>   Example: variant_id = NC_000012.12:69248967:C:T,<br>   spdi = NC_000012.12:69248967:C:T, <br>   hgvs = NC_000012.12:g.69248968C>T,<br>   rsid = rs544450198,<br>   ca_id = CA10655063,<br>   region = chr1:1157520-1158189 (maximum length: 10kb).

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genomic_elements_predictions_from_variant200_response import GenomicElementsPredictionsFromVariant200Response
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)

    try:
        api_response = api_instance.genomic_elements_predictions_from_variant(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region)
        print("The response of IgvfCatalogApi->genomic_elements_predictions_from_variant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->genomic_elements_predictions_from_variant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 

### Return type

[**GenomicElementsPredictionsFromVariant200Response**](GenomicElementsPredictionsFromVariant200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **go_terms_from_annotations**
> List[GoTermsFromAnnotations200ResponseInner] go_terms_from_annotations(query, name=name, page=page, limit=limit)

Retrieve GO terms from either proteins or transcripts. <br>   Example: query = ENSP00000384707, <br>   name = involved in<br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.go_terms_from_annotations200_response_inner import GoTermsFromAnnotations200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    query = 'query_example' # str | 
    name = 'name_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.go_terms_from_annotations(query, name=name, page=page, limit=limit)
        print("The response of IgvfCatalogApi->go_terms_from_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->go_terms_from_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **name** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GoTermsFromAnnotations200ResponseInner]**](GoTermsFromAnnotations200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grn**
> List[Grn200ResponseInner] grn(regulator_gene_id=regulator_gene_id, regulator_hgnc_id=regulator_hgnc_id, regulator_gene_name=regulator_gene_name, regulator_synonym=regulator_synonym, response_gene_id=response_gene_id, response_hgnc_id=response_hgnc_id, response_gene_name=response_gene_name, response_synonym=response_synonym, neg_log10_pvalue=neg_log10_pvalue, neg_log10_pvalue_adj=neg_log10_pvalue_adj, method=method, files_fileset=files_fileset, significant=significant, crispr_modality=crispr_modality, page=page, limit=limit)

Retrieve regulatory or response genes for a given regulatory gene. The network is modeled as: (regulators) -> (responses).<br>     files_fileset filters results to a single files_fileset accession (e.g. files_fileset = IGVFFI3069QCRA). significant only accepts true (omit the parameter to not filter on it).<br>     crispr_modality accepts knockout, interference, or activation.<br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="crispr-screen">CRISPR screen</button> <button class="method-example-tab" data-method-example-tab="perturb-seq">Perturb-seq</button> </div> <div class="method-example-panel is-active" data-method-example-panel="crispr-screen"> <strong>CRISPR screen:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>regulator_gene_id = ENSG00000143190</li> <li>p_value = gte:0.9</li> <li>method = CRISPR screen</li> <li>crispr_modality = interference</li> <li>files_fileset = IGVFFI1336XWXJ</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>regulator_gene_name = POU2F1</li> <li>method = CRISPR screen</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="perturb-seq"> <strong>Perturb-seq:</strong> <div class="method-query-example"> <strong>Query by regulator gene</strong>  <ul> <li>regulator_gene_id = ENSG00000143190</li> <li>method = Perturb-seq</li> </ul> </div> <div class="method-query-example"> <strong>Query by response gene</strong>  <ul> <li>response_gene_name = TSPAN6</li> <li>method = Perturb-seq</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.grn200_response_inner import Grn200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    regulator_gene_id = 'regulator_gene_id_example' # str |  (optional)
    regulator_hgnc_id = 'regulator_hgnc_id_example' # str |  (optional)
    regulator_gene_name = 'regulator_gene_name_example' # str |  (optional)
    regulator_synonym = 'regulator_synonym_example' # str |  (optional)
    response_gene_id = 'response_gene_id_example' # str |  (optional)
    response_hgnc_id = 'response_hgnc_id_example' # str |  (optional)
    response_gene_name = 'response_gene_name_example' # str |  (optional)
    response_synonym = 'response_synonym_example' # str |  (optional)
    neg_log10_pvalue = 'neg_log10_pvalue_example' # str |  (optional)
    neg_log10_pvalue_adj = 'neg_log10_pvalue_adj_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    significant = 'significant_example' # str |  (optional)
    crispr_modality = 'crispr_modality_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.grn(regulator_gene_id=regulator_gene_id, regulator_hgnc_id=regulator_hgnc_id, regulator_gene_name=regulator_gene_name, regulator_synonym=regulator_synonym, response_gene_id=response_gene_id, response_hgnc_id=response_hgnc_id, response_gene_name=response_gene_name, response_synonym=response_synonym, neg_log10_pvalue=neg_log10_pvalue, neg_log10_pvalue_adj=neg_log10_pvalue_adj, method=method, files_fileset=files_fileset, significant=significant, crispr_modality=crispr_modality, page=page, limit=limit)
        print("The response of IgvfCatalogApi->grn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->grn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regulator_gene_id** | **str**|  | [optional] 
 **regulator_hgnc_id** | **str**|  | [optional] 
 **regulator_gene_name** | **str**|  | [optional] 
 **regulator_synonym** | **str**|  | [optional] 
 **response_gene_id** | **str**|  | [optional] 
 **response_hgnc_id** | **str**|  | [optional] 
 **response_gene_name** | **str**|  | [optional] 
 **response_synonym** | **str**|  | [optional] 
 **neg_log10_pvalue** | **str**|  | [optional] 
 **neg_log10_pvalue_adj** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **significant** | **str**|  | [optional] 
 **crispr_modality** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[Grn200ResponseInner]**](Grn200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health**
> Health200Response health()

Health check endpoint for the API service

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.health200_response import Health200Response
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)

    try:
        api_response = api_instance.health()
        print("The response of IgvfCatalogApi->health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Health200Response**](Health200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motifs**
> List[MotifsFromProteins200ResponseInnerMotifAnyOf] motifs(tf_name=tf_name, source=source, files_fileset=files_fileset, method=method, organism=organism, page=page, limit=limit)

Retrieve transcription factor binding motifs from HOCOMOCO and SEMpl.<br>     method can be either HOCOMOCO or SEMpl; if not provided, both methods are searched. <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based. <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="hocomoco">HOCOMOCO</button> <button class="method-example-tab" data-method-example-tab="sempl">SEMpl</button> </div> <div class="method-example-panel is-active" data-method-example-panel="hocomoco"> <strong>HOCOMOCO:</strong> <div class="method-query-example"> <strong>query by tf_name</strong>  <ul> <li>tf_name = STAT3_HUMAN</li> <li>source = HOCOMOCOv11</li> <li>method = HOCOMOCO</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI1626MMBD</li> <li>method = HOCOMOCO</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sempl"> <strong>SEMpl:</strong> <div class="method-query-example"> <strong>query by tf_name</strong>  <ul> <li>tf_name = AHR</li> <li>method = SEMpl</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI5279OTVZ</li> <li>method = SEMpl</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.motifs_from_proteins200_response_inner_motif_any_of import MotifsFromProteins200ResponseInnerMotifAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    tf_name = 'tf_name_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.motifs(tf_name=tf_name, source=source, files_fileset=files_fileset, method=method, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->motifs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->motifs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tf_name** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[MotifsFromProteins200ResponseInnerMotifAnyOf]**](MotifsFromProteins200ResponseInnerMotifAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motifs_from_proteins**
> List[MotifsFromProteins200ResponseInner] motifs_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, files_fileset=files_fileset, method=method, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve motifs for proteins.<br>     Set verbose = true to retrieve full info on the motifs.<br>     Protein IDs support the following formats: ENSP00000384707.1 or ENSP00000384707 (Ensembl IDs) or P49711-2 (Uniprot ids)<br>     method can be either HOCOMOCO or SEMpl; if not provided, both methods are searched. <br>     The limit parameter controls the page size and can not exceed 1000. <br>     Pagination is 0-based. <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="hocomoco">HOCOMOCO</button> <button class="method-example-tab" data-method-example-tab="sempl">SEMpl</button> </div> <div class="method-example-panel is-active" data-method-example-panel="hocomoco"> <strong>HOCOMOCO:</strong> <div class="method-query-example"> <strong>query by protein identifier</strong>  <ul> <li>protein_id = ENSP00000384707</li> <li>method = HOCOMOCO</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI1626MMBD</li> <li>method = HOCOMOCO</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sempl"> <strong>SEMpl:</strong> <div class="method-query-example"> <strong>query by protein identifier</strong>  <ul> <li>protein_id = ENSP00000384707</li> <li>method = SEMpl</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI5279OTVZ</li> <li>method = SEMpl</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.motifs_from_proteins200_response_inner import MotifsFromProteins200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    protein_id = 'protein_id_example' # str |  (optional)
    protein_name = 'protein_name_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    uniprot_full_name = 'uniprot_full_name_example' # str |  (optional)
    dbxrefs = 'dbxrefs_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.motifs_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, files_fileset=files_fileset, method=method, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->motifs_from_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->motifs_from_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protein_id** | **str**|  | [optional] 
 **protein_name** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **uniprot_full_name** | **str**|  | [optional] 
 **dbxrefs** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[MotifsFromProteins200ResponseInner]**](MotifsFromProteins200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nearest_genes**
> List[GenesFromVariants200ResponseInnerGeneAnyOf] nearest_genes(region)

Retrieve a list of human genes if region is in a coding variant. Otherwise, it returns the nearest human genes on each side. <br>   Example: region = chr1:1157520-1158189 (maximum length: 10kb).

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_from_variants200_response_inner_gene_any_of import GenesFromVariants200ResponseInnerGeneAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str | 

    try:
        api_response = api_instance.nearest_genes(region)
        print("The response of IgvfCatalogApi->nearest_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->nearest_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | 

### Return type

[**List[GenesFromVariants200ResponseInnerGeneAnyOf]**](GenesFromVariants200ResponseInnerGeneAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ontology_term**
> List[ProteinsFromVariants200ResponseInnerBiosampleTermAnyOf] ontology_term(term_id=term_id, name=name, synonyms=synonyms, source=source, subontology=subontology, files_fileset=files_fileset, page=page, limit=limit)

Retrieve ontology terms.<br>   Example: term_id = Orphanet_101435, <br>   name = Rare genetic eye disease, <br>   synonyms = WTC11, <br>   source = EFO, <br>   subontology = molecular_function, <br>   files_fileset = IGVFFI7407XTPX. <br>   The limit parameter controls the page size and can not exceed 1000. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_variants200_response_inner_biosample_term_any_of import ProteinsFromVariants200ResponseInnerBiosampleTermAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    term_id = 'term_id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    synonyms = 'synonyms_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    subontology = 'subontology_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.ontology_term(term_id=term_id, name=name, synonyms=synonyms, source=source, subontology=subontology, files_fileset=files_fileset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->ontology_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->ontology_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **synonyms** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **subontology** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromVariants200ResponseInnerBiosampleTermAnyOf]**](ProteinsFromVariants200ResponseInnerBiosampleTermAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ontology_term_children**
> List[OntologyTermParents200ResponseInner] ontology_term_children(ontology_term_id, page=page, limit=limit)

Retrieve all child nodes of an ontology term.<br>   Example: ontology_term_id = CHEBI_20857. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.ontology_term_parents200_response_inner import OntologyTermParents200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    ontology_term_id = 'ontology_term_id_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.ontology_term_children(ontology_term_id, page=page, limit=limit)
        print("The response of IgvfCatalogApi->ontology_term_children:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->ontology_term_children: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ontology_term_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[OntologyTermParents200ResponseInner]**](OntologyTermParents200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ontology_term_parents**
> List[OntologyTermParents200ResponseInner] ontology_term_parents(ontology_term_id, page=page, limit=limit)

Retrieve all parent nodes of an ontology term.<br>   Example: ontology_term_id = CHEBI_100001. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.ontology_term_parents200_response_inner import OntologyTermParents200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    ontology_term_id = 'ontology_term_id_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.ontology_term_parents(ontology_term_id, page=page, limit=limit)
        print("The response of IgvfCatalogApi->ontology_term_parents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->ontology_term_parents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ontology_term_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[OntologyTermParents200ResponseInner]**](OntologyTermParents200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ontology_term_transitive_closure**
> OntologyTermTransitiveClosure200Response ontology_term_transitive_closure(ontology_term_id_start, ontology_term_id_end)

Retrieve all paths between two ontology terms (i.e. transitive closure).<br>   Example: ontology_term_id_start = UBERON_0003663, <br>   ontology_term_id_end = UBERON_0014892

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.ontology_term_transitive_closure200_response import OntologyTermTransitiveClosure200Response
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    ontology_term_id_start = 'ontology_term_id_start_example' # str | 
    ontology_term_id_end = 'ontology_term_id_end_example' # str | 

    try:
        api_response = api_instance.ontology_term_transitive_closure(ontology_term_id_start, ontology_term_id_end)
        print("The response of IgvfCatalogApi->ontology_term_transitive_closure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->ontology_term_transitive_closure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ontology_term_id_start** | **str**|  | 
 **ontology_term_id_end** | **str**|  | 

### Return type

[**OntologyTermTransitiveClosure200Response**](OntologyTermTransitiveClosure200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pathways**
> List[PathwaysFromGenes200ResponseInnerPathwayAnyOf] pathways(id=id, name=name, is_in_disease=is_in_disease, name_aliases=name_aliases, is_top_level_pathway=is_top_level_pathway, disease_ontology_terms=disease_ontology_terms, go_biological_process=go_biological_process, organism=organism, page=page, limit=limit)

Retrieve pathways from Reactome.<br>   Example: id = R-HSA-164843, <br>   name = 2-LTR circle formation, <br>   is_in_disease = true. <br>   name_aliases = 2-LTR circle formation, <br>   is_top_level_pathway = true. <br>   disease_ontology_terms = DOID_526, <br>   go_biological_process = GO_0006015. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.pathways_from_genes200_response_inner_pathway_any_of import PathwaysFromGenes200ResponseInnerPathwayAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    id = 'id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    is_in_disease = True # bool |  (optional)
    name_aliases = 'name_aliases_example' # str |  (optional)
    is_top_level_pathway = True # bool |  (optional)
    disease_ontology_terms = 'disease_ontology_terms_example' # str |  (optional)
    go_biological_process = 'go_biological_process_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.pathways(id=id, name=name, is_in_disease=is_in_disease, name_aliases=name_aliases, is_top_level_pathway=is_top_level_pathway, disease_ontology_terms=disease_ontology_terms, go_biological_process=go_biological_process, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->pathways:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->pathways: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **is_in_disease** | **bool**|  | [optional] 
 **name_aliases** | **str**|  | [optional] 
 **is_top_level_pathway** | **bool**|  | [optional] 
 **disease_ontology_terms** | **str**|  | [optional] 
 **go_biological_process** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PathwaysFromGenes200ResponseInnerPathwayAnyOf]**](PathwaysFromGenes200ResponseInnerPathwayAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pathways_from_genes**
> List[PathwaysFromGenes200ResponseInner] pathways_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve pathways from genes.<br>   Set verbose = true to retrieve full info on the pathways and genes. <br>   At least one of these fields is required: gene_id, hgnc_id, gene_name, synonym. <br>   Example: gene_id = ENSG00000183840, <br>   hgnc_id = HGNC:4496, <br>   gene_name = GPR39, <br>   synonym = ZnR. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.pathways_from_genes200_response_inner import PathwaysFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.pathways_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->pathways_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->pathways_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PathwaysFromGenes200ResponseInner]**](PathwaysFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pathways_from_pathways**
> List[PathwaysFromPathways200ResponseInner] pathways_from_pathways(pathway_id=pathway_id, pathway_name=pathway_name, name_aliases=name_aliases, disease_ontology_terms=disease_ontology_terms, go_biological_process=go_biological_process, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve related pathway pairs from Reactome. <br>   Set verbose = true to retrieve full info on the pathway pairs. <br>   At least one of these fields is required: pathway_id, pathway_name, or name_aliases. <br>   Example: pathway_id = R-HSA-164843, <br>   pathway_name = 2-LTR circle formation, <br>   name_aliases = 2-LTR circle formation, <br>   disease_ontology_terms = DOID_526, <br>   go_biological_process = GO_0006015. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.pathways_from_pathways200_response_inner import PathwaysFromPathways200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    pathway_id = 'pathway_id_example' # str |  (optional)
    pathway_name = 'pathway_name_example' # str |  (optional)
    name_aliases = 'name_aliases_example' # str |  (optional)
    disease_ontology_terms = 'disease_ontology_terms_example' # str |  (optional)
    go_biological_process = 'go_biological_process_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.pathways_from_pathways(pathway_id=pathway_id, pathway_name=pathway_name, name_aliases=name_aliases, disease_ontology_terms=disease_ontology_terms, go_biological_process=go_biological_process, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->pathways_from_pathways:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->pathways_from_pathways: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pathway_id** | **str**|  | [optional] 
 **pathway_name** | **str**|  | [optional] 
 **name_aliases** | **str**|  | [optional] 
 **disease_ontology_terms** | **str**|  | [optional] 
 **go_biological_process** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PathwaysFromPathways200ResponseInner]**](PathwaysFromPathways200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phenotypes_from_coding_variants**
> List[PhenotypesFromCodingVariants200ResponseInner] phenotypes_from_coding_variants(coding_variant_name=coding_variant_name, hgvsp=hgvsp, uniprot_name=uniprot_name, gene_name=gene_name, amino_acid_position=amino_acid_position, transcript_id=transcript_id, method=method, files_fileset=files_fileset, page=page, limit=limit)

Retrieve phenotypes associated with the query coding variant.<br>     At least one of these fields is required: coding_variant_name, hgvsp, uniprot_name, gene_name, amino_acid_position, transcript_id, method, files_fileset. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="dual-ipa">DUAL-IPA</button> <button class="method-example-tab" data-method-example-tab="esm-1v">ESM-1v</button> <button class="method-example-tab" data-method-example-tab="mutpred2">MutPred2</button> <button class="method-example-tab" data-method-example-tab="sge">SGE</button> <button class="method-example-tab" data-method-example-tab="vamp-seq">VAMP-seq</button> <button class="method-example-tab" data-method-example-tab="variant-painting">Variant painting via fluorescence</button> </div> <div class="method-example-panel is-active" data-method-example-panel="dual-ipa"> <strong>DUAL-IPA:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>coding_variant_name = ACSF3_ENST00000317447_p.Ala17Pro_c.49G-C</li> <li>method = DUAL-IPA</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_name = ACSF3</li> <li>method = DUAL-IPA</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="esm-1v"> <strong>ESM-1v:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>coding_variant_name = A1BG_ENST00000263100_p.Ala118Asn_c.352_353delinsAA</li> <li>method = ESM-1v</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_name = A1BG</li> <li>method = ESM-1v</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="mutpred2"> <strong>MutPred2:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>coding_variant_name = A1BG_ENST00000263100_p.Ala118Arg_c.352_353delinsCG</li> <li>method = MutPred2</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_name = A1BG</li> <li>method = MutPred2</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sge"> <strong>SGE:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>coding_variant_name = BRCA2_ENST00000380152__NC_000013.11:g.32319075A-C_splicing</li> <li>method = SGE</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_name = BRCA2</li> <li>method = SGE</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="vamp-seq"> <strong>VAMP-seq:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>coding_variant_name = CYP2C19_ENST00000371321_p.Ala103=_c.309T-G</li> <li>method = VAMP-seq</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_name = CYP2C19</li> <li>method = VAMP-seq</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="variant-painting"> <strong>Variant painting via fluorescence:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>coding_variant_name = LITAF_ENST00000622633_p.Pro135Thr_c.403C-A</li> <li>method = Variant painting via fluorescence</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_name = LITAF</li> <li>method = Variant painting via fluorescence</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.phenotypes_from_coding_variants200_response_inner import PhenotypesFromCodingVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    coding_variant_name = 'coding_variant_name_example' # str |  (optional)
    hgvsp = 'hgvsp_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    amino_acid_position = 3.4 # float |  (optional)
    transcript_id = 'transcript_id_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.phenotypes_from_coding_variants(coding_variant_name=coding_variant_name, hgvsp=hgvsp, uniprot_name=uniprot_name, gene_name=gene_name, amino_acid_position=amino_acid_position, transcript_id=transcript_id, method=method, files_fileset=files_fileset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->phenotypes_from_coding_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->phenotypes_from_coding_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coding_variant_name** | **str**|  | [optional] 
 **hgvsp** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **amino_acid_position** | **float**|  | [optional] 
 **transcript_id** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PhenotypesFromCodingVariants200ResponseInner]**](PhenotypesFromCodingVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phenotypes_from_genomic_elements**
> List[PhenotypesFromGenomicElements200ResponseInner] phenotypes_from_genomic_elements(region=region, files_fileset=files_fileset, phenotype_id=phenotype_id, phenotype_name=phenotype_name, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genomic element to phenotype associations by querying genomic elements.<br>     At least one of these properties must be defined: region, files_fileset, phenotype_id, or phenotype_name. <br>     Set significant = true to return only significant associations.<br>     Set verbose = true to retrieve full info on the genomic element.<br>     Example: phenotype_id = GO_0016477, <br>     phenotype_name = cell migration, <br>     significant = true, <br>     files_fileset = IGVFFI5135QZCS, <br>     region = chr1:101174581-101175330 (maximum length: 10kb). <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.phenotypes_from_genomic_elements200_response_inner import PhenotypesFromGenomicElements200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    phenotype_id = 'phenotype_id_example' # str |  (optional)
    phenotype_name = 'phenotype_name_example' # str |  (optional)
    significant = 'significant_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.phenotypes_from_genomic_elements(region=region, files_fileset=files_fileset, phenotype_id=phenotype_id, phenotype_name=phenotype_name, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->phenotypes_from_genomic_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->phenotypes_from_genomic_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **phenotype_id** | **str**|  | [optional] 
 **phenotype_name** | **str**|  | [optional] 
 **significant** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PhenotypesFromGenomicElements200ResponseInner]**](PhenotypesFromGenomicElements200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phenotypes_from_variants**
> List[PhenotypesFromVariants200ResponseInner] phenotypes_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, phenotype_id=phenotype_id, neg_log10_pvalue=neg_log10_pvalue, method=method, label=label, var_class=var_class, organism=organism, verbose=verbose, page=page, limit=limit, files_fileset=files_fileset)

Retrieve variant-trait pairs from GWAS, SGE, cV2F, and CRISPR screens by variants.<br>     Filters on phenotype ontology id can be used together.<br>     The following parameters can be used to set thresholds on -log10 p_value: gt (>), gte (>=), lt (<), lte (<=).<br>     Set verbose = true to retrieve full info on the studies.<br>     At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, region, method, or files_fileset. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="gwas">GWAS</button> <button class="method-example-tab" data-method-example-tab="sge">SGE</button> <button class="method-example-tab" data-method-example-tab="cv2f">cV2F</button> <button class="method-example-tab" data-method-example-tab="crispr-screen">CRISPR screen</button> </div> <div class="method-example-panel is-active" data-method-example-panel="gwas"> <strong>GWAS:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000001.11:5277210:G:A</li> <li>neg_log10_pvalue = gte:5</li> <li>method = GWAS</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr1:5270008-5277214</li> <li>method = GWAS</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sge"> <strong>SGE:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000007.14:152660654:T:A</li> <li>method = SGE</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr7:152655654-152664654</li> <li>method = SGE</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="cv2f"> <strong>cV2F:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000001.11:91420:T:C</li> <li>method = cV2F</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr1:91418-91424</li> <li>method = cV2F</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="crispr-screen"> <strong>CRISPR screen:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000019.10:11105332:TGC:CGG</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr19:11105000-11106000</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI2014OOZP</li> <li>method = CRISPR screen</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.phenotypes_from_variants200_response_inner import PhenotypesFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    phenotype_id = 'phenotype_id_example' # str |  (optional)
    neg_log10_pvalue = 'neg_log10_pvalue_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    var_class = 'var_class_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)

    try:
        api_response = api_instance.phenotypes_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, phenotype_id=phenotype_id, neg_log10_pvalue=neg_log10_pvalue, method=method, label=label, var_class=var_class, organism=organism, verbose=verbose, page=page, limit=limit, files_fileset=files_fileset)
        print("The response of IgvfCatalogApi->phenotypes_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->phenotypes_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **phenotype_id** | **str**|  | [optional] 
 **neg_log10_pvalue** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **var_class** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 

### Return type

[**List[PhenotypesFromVariants200ResponseInner]**](PhenotypesFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predictions_from_variants**
> List[PredictionsFromVariants200ResponseInner] predictions_from_variants(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, files_fileset=files_fileset, method=method, limit=limit, page=page)

Retrieve element gene predictions associated with a given variant.<br>   At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, or files_filesets. <br>   Example: variant_id = NC_000001.11:976214:A:G, <br>   hgvs = NC_000001.11:g.976215A>G,<br>   spdi = NC_000001.11:976214:A:G, <br>   rsid = rs7417106, <br>   ca_id = CA507079, <br>   files_filesets = ENCFF103XRK. <br>   The limit parameter controls the page size and can not exceed 300. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.predictions_from_variants200_response_inner import PredictionsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    files_fileset = 'files_fileset_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    limit = 3.4 # float |  (optional)
    page = 0 # float |  (optional) (default to 0)

    try:
        api_response = api_instance.predictions_from_variants(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, files_fileset=files_fileset, method=method, limit=limit, page=page)
        print("The response of IgvfCatalogApi->predictions_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->predictions_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **files_fileset** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]

### Return type

[**List[PredictionsFromVariants200ResponseInner]**](PredictionsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proteins**
> List[ProteinsFromGenes200ResponseInnerProteinAnyOf] proteins(protein_id=protein_id, name=name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, page=page, limit=limit)

Retrieve proteins.<br>   Protein IDs support the following formats: ENSP00000384707.1 or ENSP00000384707 (Ensembl IDs) or P49711-2 (Uniprot ids)<br>   Example: protein_id = ENSP00000384707, <br>   name = CTCF, <br>   uniprot_name = CTCF_HUMAN, <br>   uniprot_full_name = Transcriptional repressor CTCF, <br>   dbxrefs = P49711, <br>   organism = Homo sapiens. <br>   The limit parameter controls the page size and can not exceed 50. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_genes200_response_inner_protein_any_of import ProteinsFromGenes200ResponseInnerProteinAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    protein_id = 'protein_id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    uniprot_full_name = 'uniprot_full_name_example' # str |  (optional)
    dbxrefs = 'dbxrefs_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.proteins(protein_id=protein_id, name=name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protein_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **uniprot_full_name** | **str**|  | [optional] 
 **dbxrefs** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromGenes200ResponseInnerProteinAnyOf]**](ProteinsFromGenes200ResponseInnerProteinAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proteins_from_complexes**
> List[ComplexesFromProteins200ResponseInner] proteins_from_complexes(complex_id=complex_id, complex_name=complex_name, description=description, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve protein participants for complexes. Each record includes complex and protein.<br>   Set verbose = true to retrieve full info on the complex and protein.<br>   Example: complex_id = CPX-9, <br>   complex_name = SMAD2, <br>   description = phosphorylation.<br>   The limit parameter controls the page size and can not exceed 50. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.complexes_from_proteins200_response_inner import ComplexesFromProteins200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    complex_id = 'complex_id_example' # str |  (optional)
    complex_name = 'complex_name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.proteins_from_complexes(complex_id=complex_id, complex_name=complex_name, description=description, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->proteins_from_complexes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->proteins_from_complexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_id** | **str**|  | [optional] 
 **complex_name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ComplexesFromProteins200ResponseInner]**](ComplexesFromProteins200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proteins_from_genes**
> List[ProteinsFromGenes200ResponseInner] proteins_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve proteins from genes.<br>   Set verbose = true to retrieve full info on the proteins. <br>   At least one of these fields is required: gene_id, hgnc_id, gene_name, synonym. <br>   Example: gene_name = ATF3, <br>   synonym = CKLF, <br>   gene_id = ENSG00000170558 (Ensembl ID), <br>   hgnc_id = HGNC:13723. <br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_genes200_response_inner import ProteinsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.proteins_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->proteins_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->proteins_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromGenes200ResponseInner]**](ProteinsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proteins_from_motifs**
> List[MotifsFromProteins200ResponseInner] proteins_from_motifs(tf_name=tf_name, source=source, files_fileset=files_fileset, method=method, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve proteins and complexes for motifs.<br>     Set verbose = true to retrieve full info on the proteins and complexes.<br>     method can be either HOCOMOCO or SEMpl; if not provided, both methods are searched. <br>     The limit parameter controls the page size and can not exceed 1000. <br>     Pagination is 0-based. <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="hocomoco">HOCOMOCO</button> <button class="method-example-tab" data-method-example-tab="sempl">SEMpl</button> </div> <div class="method-example-panel is-active" data-method-example-panel="hocomoco"> <strong>HOCOMOCO:</strong> <div class="method-query-example"> <strong>query by tf_name</strong>  <ul> <li>tf_name = ATF1_HUMAN</li> <li>source = HOCOMOCOv11</li> <li>method = HOCOMOCO</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI1626MMBD</li> <li>method = HOCOMOCO</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sempl"> <strong>SEMpl:</strong> <div class="method-query-example"> <strong>query by tf_name</strong>  <ul> <li>tf_name = AHR</li> <li>method = SEMpl</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI5279OTVZ</li> <li>method = SEMpl</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.motifs_from_proteins200_response_inner import MotifsFromProteins200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    tf_name = 'tf_name_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.proteins_from_motifs(tf_name=tf_name, source=source, files_fileset=files_fileset, method=method, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->proteins_from_motifs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->proteins_from_motifs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tf_name** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[MotifsFromProteins200ResponseInner]**](MotifsFromProteins200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proteins_from_transcripts**
> List[ProteinsFromTranscripts200ResponseInner] proteins_from_transcripts(transcript_id=transcript_id, region=region, transcript_type=transcript_type, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve proteins from transcripts.<br>     Set verbose = true to retrieve full info on the proteins.<br>     At least one of these fields is required: transcript_id, region or transcript_type. <br>     Example: transcript_id = ENST00000264010, <br>     region = chr16:67562500-67640000, <br>     transcript_type = protein_coding, <br>     organism = Homo sapiens, <br>     transcript_id = ENST00000401394 (Ensembl ID). <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_transcripts200_response_inner import ProteinsFromTranscripts200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    transcript_id = 'transcript_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    transcript_type = 'transcript_type_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.proteins_from_transcripts(transcript_id=transcript_id, region=region, transcript_type=transcript_type, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->proteins_from_transcripts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->proteins_from_transcripts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcript_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **transcript_type** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromTranscripts200ResponseInner]**](ProteinsFromTranscripts200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proteins_from_variants**
> List[ProteinsFromVariants200ResponseInner] proteins_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, label=label, source=source, method=method, files_fileset=files_fileset, name=name, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve allele-specific transcription factor binding events from ADASTRA in cell type-specific context, <br>     allele-specific transcription factor binding events from GVATdb, pQTL from UKB by querying variants, and predicted allele specific binding from SEMpl.<br>     Set verbose = true to retrieve full info on the variant-transcription factor pairs, and ontology terms of the cell types.<br>     At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, region, method, or files_fileset. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="adastra">ADASTRA</button> <button class="method-example-tab" data-method-example-tab="gvatdb">GVATdb</button> <button class="method-example-tab" data-method-example-tab="semvar">SEMVAR</button> <button class="method-example-tab" data-method-example-tab="pqtl">pQTL</button> </div> <div class="method-example-panel is-active" data-method-example-panel="adastra"> <strong>ADASTRA:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>variant_id = NC_000005.10:59317579:G:T</li> <li>method = ADASTRA</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr5:150575301-150575304</li> <li>method = ADASTRA</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="gvatdb"> <strong>GVATdb:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>variant_id = NC_000010.11:112626979:C:T</li> <li>method = GVATdb</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr10:112626978-112626982</li> <li>method = GVATdb</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="semvar"> <strong>SEMVAR:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000001.11:100091094:A:C</li> <li>method = SEMVAR</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr1:100091093-100091097</li> <li>method = SEMVAR</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="pqtl"> <strong>pQTL:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>spdi = NC_000002.12:27508072:T:C</li> <li>method = pQTL</li> </ul> </div> <div class="method-query-example"> <strong>query by region</strong>  <ul> <li>region = chr2:27508070-27508074</li> <li>method = pQTL</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_variants200_response_inner import ProteinsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.proteins_from_variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, label=label, source=source, method=method, files_fileset=files_fileset, name=name, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->proteins_from_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->proteins_from_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromVariants200ResponseInner]**](ProteinsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proteins_proteins**
> List[ProteinsProteins200ResponseInner] proteins_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, associated_protein_id=associated_protein_id, associated_protein_name=associated_protein_name, associated_uniprot_name=associated_uniprot_name, associated_uniprot_full_name=associated_uniprot_full_name, associated_dbxrefs=associated_dbxrefs, pmid=pmid, detection_method=detection_method, interaction_type=interaction_type, label=label, method=method, source=source, files_fileset=files_fileset, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve protein-protein interactions.<br>   Set verbose = true to retrieve full info on the proteins. <br>   Protein IDs support the following formats: ENSP00000384707.1 or ENSP00000384707 (Ensembl IDs) or P49711-2 (Uniprot ids)<br>   Example: protein_id = ENSP00000384707.1, <br>   protein_name = CTCF, <br>   uniprot_name = CTCF_HUMAN, <br>   uniprot_full_name = Transcriptional repressor CTCF, <br>   dbxrefs = P49711, <br>   detection_method = affinity chromatography technology, <br>   interaction_type = physical association, <br>   pmid = 28514442, <br>   associated_protein_id = ENSP00000428899, <br>   associated_protein_name = TNPO1, <br>   associated_uniprot_name = TNPO1_HUMAN, <br>   associated_uniprot_full_name = Transportin-1, <br>   associated_dbxrefs = DIP-29335N, <br>   label = affinity chromatography technology, <br>   method = physical association, <br>   source = BioGRID, <br>   files_fileset = IGVFFI4317VDGK, <br>   organism = Homo sapiens. <br>   The limit parameter controls the page size and can not exceed 250. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_proteins200_response_inner import ProteinsProteins200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    protein_id = 'protein_id_example' # str |  (optional)
    protein_name = 'protein_name_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    uniprot_full_name = 'uniprot_full_name_example' # str |  (optional)
    dbxrefs = 'dbxrefs_example' # str |  (optional)
    associated_protein_id = 'associated_protein_id_example' # str |  (optional)
    associated_protein_name = 'associated_protein_name_example' # str |  (optional)
    associated_uniprot_name = 'associated_uniprot_name_example' # str |  (optional)
    associated_uniprot_full_name = 'associated_uniprot_full_name_example' # str |  (optional)
    associated_dbxrefs = 'associated_dbxrefs_example' # str |  (optional)
    pmid = 'pmid_example' # str |  (optional)
    detection_method = 'detection_method_example' # str |  (optional)
    interaction_type = 'interaction_type_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.proteins_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, associated_protein_id=associated_protein_id, associated_protein_name=associated_protein_name, associated_uniprot_name=associated_uniprot_name, associated_uniprot_full_name=associated_uniprot_full_name, associated_dbxrefs=associated_dbxrefs, pmid=pmid, detection_method=detection_method, interaction_type=interaction_type, label=label, method=method, source=source, files_fileset=files_fileset, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->proteins_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->proteins_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protein_id** | **str**|  | [optional] 
 **protein_name** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **uniprot_full_name** | **str**|  | [optional] 
 **dbxrefs** | **str**|  | [optional] 
 **associated_protein_id** | **str**|  | [optional] 
 **associated_protein_name** | **str**|  | [optional] 
 **associated_uniprot_name** | **str**|  | [optional] 
 **associated_uniprot_full_name** | **str**|  | [optional] 
 **associated_dbxrefs** | **str**|  | [optional] 
 **pmid** | **str**|  | [optional] 
 **detection_method** | **str**|  | [optional] 
 **interaction_type** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsProteins200ResponseInner]**](ProteinsProteins200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qtl_summary_endpoint**
> List[QtlSummaryEndpoint200ResponseInner] qtl_summary_endpoint(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, page=page, limit=limit, files_fileset=files_fileset)

Retrieve a summary of associated genes from GTEx eQTLs & splice QTLs by internal variant ids.<br>     Example: <br>     variant_id = NC_000001.11:40242002:G:A,<br>     spdi = NC_000001.11:40242002:G:A,<br>     hgvs = NC_000001.11:g.40242003G>A,<br>     ca_id = CA16051554,<br>     files_fileset = IGVFFI9602ILPC.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.qtl_summary_endpoint200_response_inner import QtlSummaryEndpoint200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)

    try:
        api_response = api_instance.qtl_summary_endpoint(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, page=page, limit=limit, files_fileset=files_fileset)
        print("The response of IgvfCatalogApi->qtl_summary_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->qtl_summary_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 

### Return type

[**List[QtlSummaryEndpoint200ResponseInner]**](QtlSummaryEndpoint200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qtls**
> List[Qtls200ResponseInner] qtls(gene_id=gene_id, gene_name=gene_name, variant_id=variant_id, spdi=spdi, rsid=rsid, ca_id=ca_id, region=region, biological_context=biological_context, method=method, source=source, organism=organism, page=page, limit=limit)

Retrieve QTLs from gene, variant, or region.<br>     Define exactly one query type: gene (gene_id or gene_name), variant (variant_id, spdi, rsid, or ca_id), or region.<br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="eqtl">eQTL</button> <button class="method-example-tab" data-method-example-tab="spliceqtl">spliceQTL</button> <button class="method-example-tab" data-method-example-tab="pqtl">pQTL</button> <button class="method-example-tab" data-method-example-tab="caqtl">caQTL</button> </div> <div class="method-example-panel is-active" data-method-example-panel="eqtl"> <strong>eQTL:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>spdi = NC_000001.11:40241653:TGAA:TGAAATTGAA</li> <li>method = eQTL</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>gene_id = ENSG00000259943</li> <li>method = eQTL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="spliceqtl"> <strong>spliceQTL:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>variant_id = NC_000001.11:898757:AAAAAA:AAAAAAA</li> <li>method = spliceQTL</li> </ul> </div> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000131236</li> <li>method = spliceQTL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="pqtl"> <strong>pQTL:</strong> <div class="method-query-example"> <strong>query by variant identifier</strong>  <ul> <li>variant_id = NC_000002.12:27508072:T:C</li> <li>method = pQTL</li> </ul> </div> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000084734</li> <li>method = pQTL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="caqtl"> <strong>caQTL:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>variant_id = NC_000001.11:40241653:TGAA:TGAAATTGAA</li> <li>method = caQTL</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>region = chr1:40232650-40241654</li> <li>method = caQTL</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.qtls200_response_inner import Qtls200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    spdi = 'spdi_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.qtls(gene_id=gene_id, gene_name=gene_name, variant_id=variant_id, spdi=spdi, rsid=rsid, ca_id=ca_id, region=region, biological_context=biological_context, method=method, source=source, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->qtls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->qtls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **spdi** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[Qtls200ResponseInner]**](Qtls200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies**
> List[GenesFromVariants200ResponseInnerStudyAnyOf] studies(study_id=study_id, pmid=pmid, files_fileset=files_fileset, page=page)

Retrieve studies from GWAS. <br>   Example: study_id = GCST007798, <br>   pmid = 30929738, <br>   files_fileset = IGVFFI1309WDQG. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_from_variants200_response_inner_study_any_of import GenesFromVariants200ResponseInnerStudyAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    study_id = 'study_id_example' # str |  (optional)
    pmid = 'pmid_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)

    try:
        api_response = api_instance.studies(study_id=study_id, pmid=pmid, files_fileset=files_fileset, page=page)
        print("The response of IgvfCatalogApi->studies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->studies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  | [optional] 
 **pmid** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]

### Return type

[**List[GenesFromVariants200ResponseInnerStudyAnyOf]**](GenesFromVariants200ResponseInnerStudyAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcripts**
> List[TranscriptsFromGenes200ResponseInnerTranscriptAnyOf] transcripts(transcript_id=transcript_id, region=region, transcript_type=transcript_type, organism=organism, page=page, limit=limit)

Retrieve transcripts. <br>   Example: region = chr20:9537369-9839076, <br>   transcript_type = protein_coding, <br>   transcript_id = ENST00000443707 (Ensembl ids), <br>   organism = Homo sapiens. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.transcripts_from_genes200_response_inner_transcript_any_of import TranscriptsFromGenes200ResponseInnerTranscriptAnyOf
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    transcript_id = 'transcript_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    transcript_type = 'transcript_type_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.transcripts(transcript_id=transcript_id, region=region, transcript_type=transcript_type, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->transcripts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->transcripts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcript_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **transcript_type** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[TranscriptsFromGenes200ResponseInnerTranscriptAnyOf]**](TranscriptsFromGenes200ResponseInnerTranscriptAnyOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcripts_from_genes**
> List[TranscriptsFromGenes200ResponseInner] transcripts_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve transcripts from genes.<br>     Set verbose = true to retrieve full info on the transcripts.<br>     At least one of these fields is required: gene_id, hgnc_id, gene_name, synonym. <br>     Example: gene_name = ATF3, <br>     hgnc_id = HGNC:28208, <br>     synonym = CKLF, <br>     organism = Homo sapiens, <br>     gene_id = ENSG00000187642 (Ensembl ids). <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.transcripts_from_genes200_response_inner import TranscriptsFromGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.transcripts_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->transcripts_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->transcripts_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[TranscriptsFromGenes200ResponseInner]**](TranscriptsFromGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcripts_from_proteins**
> List[ProteinsFromTranscripts200ResponseInner] transcripts_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve transcripts from proteins.<br>     Set verbose = true to retrieve full info on the transcripts.<br>     Protein IDs support the following formats: ENSP00000384707.1 or ENSP00000384707 (Ensembl IDs) or P49711-2 (Uniprot ids)<br>     Example: protein_name = CTCF, <br>     uniprot_name = CTCF_HUMAN, <br>     uniprot_full_name = Transcriptional repressor CTCF, <br>     dbxrefs = P49711, <br>     protein_id = ENSP00000384707, <br>     organism = Homo sapiens. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_transcripts200_response_inner import ProteinsFromTranscripts200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    protein_id = 'protein_id_example' # str |  (optional)
    protein_name = 'protein_name_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    uniprot_full_name = 'uniprot_full_name_example' # str |  (optional)
    dbxrefs = 'dbxrefs_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.transcripts_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->transcripts_from_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->transcripts_from_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protein_id** | **str**|  | [optional] 
 **protein_name** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **uniprot_full_name** | **str**|  | [optional] 
 **dbxrefs** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromTranscripts200ResponseInner]**](ProteinsFromTranscripts200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_by_frequency_source**
> List[Variants200ResponseInner] variant_by_frequency_source(source, spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, region=region, gencode_category=gencode_category, minimum_af=minimum_af, maximum_af=maximum_af, organism=organism, page=page, limit=limit)

Retrieve genetic variants within a genomic region by frequencies.<br>   Source is required. <br>    Example: region = chr3:186741137-186742238 (maximum length: 10kb), <br>    source = bravo_af, <br>    GENCODE_category = coding (or noncoding), <br>    spdi = NC_000003.12:186741142:G:A, <br>    hgvs = NC_000003.12:g.186741143G>A, <br>    rsid = rs1720801112, <br>    ca_id = CA739473472, <br>    minimum_af: 0, <br>    maximum_af:0.8. <br>    Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants200_response_inner import Variants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    source = 'source_example' # str | 
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    gencode_category = 'gencode_category_example' # str |  (optional)
    minimum_af = 0 # float |  (optional) (default to 0)
    maximum_af = 1 # float |  (optional) (default to 1)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variant_by_frequency_source(source, spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, region=region, gencode_category=gencode_category, minimum_af=minimum_af, maximum_af=maximum_af, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variant_by_frequency_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variant_by_frequency_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **gencode_category** | **str**|  | [optional] 
 **minimum_af** | **float**|  | [optional] [default to 0]
 **maximum_af** | **float**|  | [optional] [default to 1]
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[Variants200ResponseInner]**](Variants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_summary**
> VariantSummary200Response variant_summary(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism)

Retrieve genetic variants summary.<br>    Example: variant_id = NC_000020.11:3658947:A:G, <br>    spdi = NC_000020.11:3658947:A:G, <br>    hgvs = NC_000020.11:g.3658948A>G. <br>    ca_id = CA739473472

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variant_summary200_response import VariantSummary200Response
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)

    try:
        api_response = api_instance.variant_summary(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism)
        print("The response of IgvfCatalogApi->variant_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variant_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]

### Return type

[**VariantSummary200Response**](VariantSummary200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants**
> List[Variants200ResponseInner] variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, gencode_category=gencode_category, mouse_strain=mouse_strain, organism=organism, page=page, limit=limit)

Retrieve genetic variants.<br>   Example: organism = Homo sapiens or Mus musculus.<br>   mouse_strain = CAST_EiJ (only for mouse variants). <br>   The examples below are specific to Homo sapiens: <br>   region = chr1:1157520-1158189 (maximum length: 10kb), <br>   GENCODE_category = coding or noncoding (only for human variants), <br>   rsid = rs58658771,  <br>   spdi = NC_000020.11:3658947:A:G, <br>   hgvs = NC_000020.11:g.3658948A>G, <br>   ca_id = CA739473472, <br>   variant_id = NC_000020.11:3658947:A:G. <br>   The limit parameter controls the page size and can not exceed 500. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants200_response_inner import Variants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    gencode_category = 'gencode_category_example' # str |  (optional)
    mouse_strain = 'mouse_strain_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, gencode_category=gencode_category, mouse_strain=mouse_strain, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **gencode_category** | **str**|  | [optional] 
 **mouse_strain** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[Variants200ResponseInner]**](Variants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_alleles**
> List[List[VariantsAlleles200ResponseInnerInner]] variants_alleles(region)

Retrieve GNOMAD alleles for variants in a given region.<br>    Example: region = chr1:1157520-1158520 (maximum length: 10kb).<br>    Region limit: 1kb pairs.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_alleles200_response_inner_inner import VariantsAlleles200ResponseInnerInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str | 

    try:
        api_response = api_instance.variants_alleles(region)
        print("The response of IgvfCatalogApi->variants_alleles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_alleles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | 

### Return type

**List[List[VariantsAlleles200ResponseInnerInner]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_biosamples**
> List[BiosamplesFromVariants200ResponseInner] variants_from_biosamples(biosample_id=biosample_id, biosample_name=biosample_name, files_fileset=files_fileset, method=method, element_id=element_id, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve data from STARR-seq, BlueSTARR, and MPRA for a given biosample.<br>     At least one of these fields is required: biosample_id or biosample_name. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="mpra">MPRA</button> <button class="method-example-tab" data-method-example-tab="starr-seq">STARR-seq</button> <button class="method-example-tab" data-method-example-tab="bluestarr">BlueSTARR</button> </div> <div class="method-example-panel is-active" data-method-example-panel="mpra"> <strong>MPRA:</strong> <div class="method-query-example"> <strong>query by biosample identifier</strong>  <ul> <li>biosample_id = EFO_0001182</li> <li>method = MPRA</li> <li>element_id = MPRA_chr1_1000079_1000279_GRCh38_plus_IGVFFI7321WGMD</li> <li>significant = true</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="starr-seq"> <strong>STARR-seq:</strong> <div class="method-query-example"> <strong>query by biosample identifier</strong>  <ul> <li>biosample_id = EFO_0002067</li> <li>method = STARR-seq</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="bluestarr"> <strong>BlueSTARR:</strong> <div class="method-query-example"> <strong>query by biosample identifier</strong>  <ul> <li>biosample_id = EFO_0002067</li> <li>method = BlueSTARR</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.biosamples_from_variants200_response_inner import BiosamplesFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    biosample_id = 'biosample_id_example' # str |  (optional)
    biosample_name = 'biosample_name_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    element_id = 'element_id_example' # str |  (optional)
    significant = 'significant_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_biosamples(biosample_id=biosample_id, biosample_name=biosample_name, files_fileset=files_fileset, method=method, element_id=element_id, significant=significant, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_biosamples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_biosamples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biosample_id** | **str**|  | [optional] 
 **biosample_name** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **element_id** | **str**|  | [optional] 
 **significant** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[BiosamplesFromVariants200ResponseInner]**](BiosamplesFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_coding_variants**
> List[VariantsFromCodingVariants200ResponseInner] variants_from_coding_variants(coding_variant_name=coding_variant_name, hgvsp=hgvsp, protein_id=protein_id, uniprot_name=uniprot_name, gene_name=gene_name, amino_acid_position=amino_acid_position, alt_amino_acid=alt_amino_acid, transcript_id=transcript_id, page=page, limit=limit)

Retrieve variants associated with a coding variant.<br>     alt_amino_acid filters by the alternate amino acid at the given position (single-letter code, use * for stop codon). <br>     Example: coding_variant_name = SAMD7_ENST00000335556_p.Gly253Asp_c.758_759delinsAC, <br>     hgvsp = p.Gly253Asp, <br>     gene_name = SAMD7, <br>     protein_id = ENSP00000334668, <br>     uniprot_name = SAMD7_HUMAN, <br>     transcript_id = ENST00000335556, <br>     amino_acid_position = 253, <br>     alt_amino_acid = D, <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_from_coding_variants200_response_inner import VariantsFromCodingVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    coding_variant_name = 'coding_variant_name_example' # str |  (optional)
    hgvsp = 'hgvsp_example' # str |  (optional)
    protein_id = 'protein_id_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    amino_acid_position = 'amino_acid_position_example' # str |  (optional)
    alt_amino_acid = 'alt_amino_acid_example' # str |  (optional)
    transcript_id = 'transcript_id_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_coding_variants(coding_variant_name=coding_variant_name, hgvsp=hgvsp, protein_id=protein_id, uniprot_name=uniprot_name, gene_name=gene_name, amino_acid_position=amino_acid_position, alt_amino_acid=alt_amino_acid, transcript_id=transcript_id, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_coding_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_coding_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coding_variant_name** | **str**|  | [optional] 
 **hgvsp** | **str**|  | [optional] 
 **protein_id** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **amino_acid_position** | **str**|  | [optional] 
 **alt_amino_acid** | **str**|  | [optional] 
 **transcript_id** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[VariantsFromCodingVariants200ResponseInner]**](VariantsFromCodingVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_diseases**
> List[DiseaseFromVariants200ResponseInner] variants_from_diseases(disease_id=disease_id, disease_name=disease_name, assertion=assertion, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve variants and genes associated with the query disease from ClinGen. <br>   Either disease_id or disease_name is required. <br>   Example: disease_id = MONDO_0009861, <br>   disease_name = phenylketonuria, <br>   assertion = Pathogenic, <br>   pmid = 2574002. <br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.disease_from_variants200_response_inner import DiseaseFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    disease_id = 'disease_id_example' # str |  (optional)
    disease_name = 'disease_name_example' # str |  (optional)
    assertion = 'assertion_example' # str |  (optional)
    pmid = 'pmid_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_diseases(disease_id=disease_id, disease_name=disease_name, assertion=assertion, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_diseases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_diseases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disease_id** | **str**|  | [optional] 
 **disease_name** | **str**|  | [optional] 
 **assertion** | **str**|  | [optional] 
 **pmid** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[DiseaseFromVariants200ResponseInner]**](DiseaseFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_drugs**
> List[VariantsFromDrugs200ResponseInner] variants_from_drugs(drug_id=drug_id, drug_name=drug_name, phenotype_categories=phenotype_categories, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve variants associated with the query drugs from pharmGKB.<br>   Set verbose = true to retrieve full info on the variants. <br>   Either drug_id or drug_name is required. <br>   Example: drug_id = PA448497, <br>   drug_name = aspirin, <br>   pmid = 20824505, <br>   phenotype_categories = Toxicity. <br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_from_drugs200_response_inner import VariantsFromDrugs200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    drug_id = 'drug_id_example' # str |  (optional)
    drug_name = 'drug_name_example' # str |  (optional)
    phenotype_categories = 'phenotype_categories_example' # str |  (optional)
    pmid = 'pmid_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_drugs(drug_id=drug_id, drug_name=drug_name, phenotype_categories=phenotype_categories, pmid=pmid, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_drugs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_drugs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drug_id** | **str**|  | [optional] 
 **drug_name** | **str**|  | [optional] 
 **phenotype_categories** | **str**|  | [optional] 
 **pmid** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[VariantsFromDrugs200ResponseInner]**](VariantsFromDrugs200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_gene_proteins**
> List[GenesProteinsFromVariants200ResponseInner] variants_from_gene_proteins(query, page=page, limit=limit)

Retrieve variants associated with genes or proteins that match a query. <br>   Example: query = ATF1.<br>   The limit parameter controls the page size and can not exceed 100. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_proteins_from_variants200_response_inner import GenesProteinsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    query = 'query_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_gene_proteins(query, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_gene_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_gene_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesProteinsFromVariants200ResponseInner]**](GenesProteinsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_genes**
> List[GenesFromVariants200ResponseInner] variants_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, neg_log10_pvalue=neg_log10_pvalue, effect_size=effect_size, posterior_inclusion_probability=posterior_inclusion_probability, log2_fc=log2_fc, significant=significant, biosample_term=biosample_term, biological_context=biological_context, label=label, method=method, files_fileset=files_fileset, source=source, name=name, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve variant-gene pairs including eQTLs & splice QTLs from AFGR and eQTL Catalogue, and CRISPR screen and Variant-EFFECTS from IGVF, by Ensembl gene ids.<br>     The following parameters can be used to set thresholds on -log10 p_value: gt (>), gte (>=), lt (<), lte (<=).<br>     Set verbose = true to retrieve full info on the corresponding variants and genes.<br>     At least one of these properties must be defined: gene_id, hgnc_id, gene_name, region, synonym, method, or files_fileset. <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="eqtl">eQTL</button> <button class="method-example-tab" data-method-example-tab="spliceqtl">spliceQTL</button> <button class="method-example-tab" data-method-example-tab="variant-effects">Variant-EFFECTS</button> <button class="method-example-tab" data-method-example-tab="crispr-screen">CRISPR screen</button> </div> <div class="method-example-panel is-active" data-method-example-panel="eqtl"> <strong>eQTL:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>gene_id = ENSG00000187642</li> <li>neg_log10_pvalue = gte:24.5</li> <li>method = eQTL</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>synonym = PERM1</li> <li>method = eQTL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="spliceqtl"> <strong>spliceQTL:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>gene_id = ENSG00000188976</li> <li>neg_log10_pvalue = gt:45</li> <li>effect_size = gt:0.5</li> <li>method = spliceQTL</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>synonym = NOC2L</li> <li>method = spliceQTL</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="variant-effects"> <strong>Variant-EFFECTS:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>gene_id = ENSG00000108179</li> <li>neg_log10_pvalue = gt:13.1</li> <li>method = Variant-EFFECTS</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>synonym = PPIF</li> <li>method = Variant-EFFECTS</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="crispr-screen"> <strong>CRISPR screen:</strong> <div class="method-query-example"> <strong>query by gene identifier</strong>  <ul> <li>gene_id = ENSG00000177455</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>query by gene name</strong>  <ul> <li>gene_name = CD19</li> <li>method = CRISPR screen</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genes_from_variants200_response_inner import GenesFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str |  (optional)
    hgnc_id = 'hgnc_id_example' # str |  (optional)
    gene_name = 'gene_name_example' # str |  (optional)
    synonym = 'synonym_example' # str |  (optional)
    neg_log10_pvalue = 'neg_log10_pvalue_example' # str |  (optional)
    effect_size = 'effect_size_example' # str |  (optional)
    posterior_inclusion_probability = 'posterior_inclusion_probability_example' # str |  (optional)
    log2_fc = 'log2_fc_example' # str |  (optional)
    significant = 'significant_example' # str |  (optional)
    biosample_term = 'biosample_term_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_genes(gene_id=gene_id, hgnc_id=hgnc_id, gene_name=gene_name, synonym=synonym, neg_log10_pvalue=neg_log10_pvalue, effect_size=effect_size, posterior_inclusion_probability=posterior_inclusion_probability, log2_fc=log2_fc, significant=significant, biosample_term=biosample_term, biological_context=biological_context, label=label, method=method, files_fileset=files_fileset, source=source, name=name, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | [optional] 
 **hgnc_id** | **str**|  | [optional] 
 **gene_name** | **str**|  | [optional] 
 **synonym** | **str**|  | [optional] 
 **neg_log10_pvalue** | **str**|  | [optional] 
 **effect_size** | **str**|  | [optional] 
 **posterior_inclusion_probability** | **str**|  | [optional] 
 **log2_fc** | **str**|  | [optional] 
 **significant** | **str**|  | [optional] 
 **biosample_term** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenesFromVariants200ResponseInner]**](GenesFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_genomic_elements**
> List[GenomicElementsFromVariants200ResponseInner] variants_from_genomic_elements(region=region, region_type=region_type, biosample_term=biosample_term, biological_context=biological_context, method=method, files_fileset=files_fileset, page=page, limit=limit)

Retrieve variants associated with genomic elements.<br>   Example: region = chr1:976210-976314, <br>   region_type = accessible dna elements, <br>   biosample_term = EFO_0002067, <br>   biological_context = K562, <br>   method = caQTL. <br>   The limit parameter controls the page size and can not exceed 300. <br>   Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.genomic_elements_from_variants200_response_inner import GenomicElementsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str |  (optional)
    region_type = 'region_type_example' # str |  (optional)
    biosample_term = 'biosample_term_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_genomic_elements(region=region, region_type=region_type, biosample_term=biosample_term, biological_context=biological_context, method=method, files_fileset=files_fileset, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_genomic_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_genomic_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | [optional] 
 **region_type** | **str**|  | [optional] 
 **biosample_term** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[GenomicElementsFromVariants200ResponseInner]**](GenomicElementsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_phenotypes**
> List[PhenotypesFromVariants200ResponseInner] variants_from_phenotypes(phenotype_id=phenotype_id, phenotype_name=phenotype_name, neg_log10_pvalue=neg_log10_pvalue, method=method, label=label, var_class=var_class, files_fileset=files_fileset, source=source, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve variant-trait pairs from GWAS, SGE, cV2F, and CRISPR screens by phenotypes.<br>     The following parameters can be used to set thresholds on -log10 p_value: gt (>), gte (>=), lt (<), lte (<=).<br>     Set verbose = true to retrieve full info on the studies.<br>     At least one of these fields is required: phenotype_id, phenotype_name, method, or files_fileset. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="gwas">GWAS</button> <button class="method-example-tab" data-method-example-tab="sge">SGE</button> <button class="method-example-tab" data-method-example-tab="cv2f">cV2F</button> <button class="method-example-tab" data-method-example-tab="crispr-screen">CRISPR screen</button> </div> <div class="method-example-panel is-active" data-method-example-panel="gwas"> <strong>GWAS:</strong> <div class="method-query-example"> <strong>Single result</strong>  <ul> <li>phenotype_id = EFO_0010325</li> <li>method = GWAS</li> </ul> </div> <div class="method-query-example"> <strong>Group results</strong>  <ul> <li>neg_log10_pvalue = gte:5</li> <li>method = GWAS</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="sge"> <strong>SGE:</strong> <div class="method-query-example"> <strong>Query by phenotype identifier</strong>  <ul> <li>phenotype_id = NCIT_C16407</li> <li>method = SGE</li> </ul> </div> <div class="method-query-example"> <strong>Query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI3125FMNW</li> <li>method = SGE</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="cv2f"> <strong>cV2F:</strong> <div class="method-query-example"> <strong>query by phenotype identifier</strong>  <ul> <li>phenotype_id = GO_0003674</li> <li>method = cV2F</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI3063JRLI</li> <li>method = cV2F</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="crispr-screen"> <strong>CRISPR screen:</strong> <div class="method-query-example"> <strong>Query by phenotype identifier</strong>  <ul> <li>phenotype_id = NTR_0001118</li> <li>method = CRISPR screen</li> </ul> </div> <div class="method-query-example"> <strong>Query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI2014OOZP</li> <li>method = CRISPR screen</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.phenotypes_from_variants200_response_inner import PhenotypesFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    phenotype_id = 'phenotype_id_example' # str |  (optional)
    phenotype_name = 'phenotype_name_example' # str |  (optional)
    neg_log10_pvalue = 'neg_log10_pvalue_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    var_class = 'var_class_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_phenotypes(phenotype_id=phenotype_id, phenotype_name=phenotype_name, neg_log10_pvalue=neg_log10_pvalue, method=method, label=label, var_class=var_class, files_fileset=files_fileset, source=source, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_phenotypes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_phenotypes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phenotype_id** | **str**|  | [optional] 
 **phenotype_name** | **str**|  | [optional] 
 **neg_log10_pvalue** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **var_class** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[PhenotypesFromVariants200ResponseInner]**](PhenotypesFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_proteins**
> List[ProteinsFromVariants200ResponseInner] variants_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, label=label, source=source, method=method, files_fileset=files_fileset, name=name, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve allele-specific transcription factor binding events from ADASTRA in cell type-specific context, <br>     allele-specific transcription factor binding events from GVATdb, pQTL from UKB by querying proteins, and predicted allele specific binding from SEMpl.<br>     Protein IDs support the following formats: ENSP00000384707.1 or ENSP00000384707 (Ensembl IDs) or P49711-2 (Uniprot ids).<br>     Set verbose = true to retrieve full info on the variant-transcription factor pairs, and the ontology terms of the cell types.<br>     At least one of these fields is required: protein_id, protein_name, uniprot_name, uniprot_full_name, dbxrefs, method, or files_fileset. <br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based. <br> <br>     <div class="method-examples"> <strong>Examples by method</strong> <p class="method-example-description">These examples are grouped by method; use the <code>method</code> filter to return data from a specific method.</p> <div class="method-example-tabs"> <button class="method-example-tab is-active" data-method-example-tab="adastra">ADASTRA</button> <button class="method-example-tab" data-method-example-tab="gvatdb">GVATdb</button> <button class="method-example-tab" data-method-example-tab="semvar">SEMVAR</button> <button class="method-example-tab" data-method-example-tab="pqtl">pQTL</button> </div> <div class="method-example-panel is-active" data-method-example-panel="adastra"> <strong>ADASTRA:</strong> <div class="method-query-example"> <strong>query by protein identifier</strong>  <ul> <li>protein_id = ENSP00000281043</li> <li>method = ADASTRA</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="gvatdb"> <strong>GVATdb:</strong> <div class="method-query-example"> <strong>query by protein identifier</strong>  <ul> <li>protein_id = ENSP00000315417</li> <li>method = GVATdb</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="semvar"> <strong>SEMVAR:</strong> <div class="method-query-example"> <strong>query by protein identifier</strong>  <ul> <li>protein_id = ENSP00000351458</li> <li>method = SEMVAR</li> </ul> </div> <div class="method-query-example"> <strong>query by files_fileset</strong> <p class="method-query-example-note">Each files_fileset maps to at most one method, so a <code>method</code> filter is usually not necessary.</p> <ul> <li>files_fileset = IGVFFI0005WRQP</li> <li>method = SEMVAR</li> </ul> </div> </div> <div class="method-example-panel" data-method-example-panel="pqtl"> <strong>pQTL:</strong> <div class="method-query-example"> <strong>query by protein identifier</strong>  <ul> <li>protein_id = ENSP00000263100</li> <li>method = pQTL</li> </ul> </div> </div> </div>

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.proteins_from_variants200_response_inner import ProteinsFromVariants200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    protein_id = 'protein_id_example' # str |  (optional)
    protein_name = 'protein_name_example' # str |  (optional)
    uniprot_name = 'uniprot_name_example' # str |  (optional)
    uniprot_full_name = 'uniprot_full_name_example' # str |  (optional)
    dbxrefs = 'dbxrefs_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    method = 'method_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_proteins(protein_id=protein_id, protein_name=protein_name, uniprot_name=uniprot_name, uniprot_full_name=uniprot_full_name, dbxrefs=dbxrefs, label=label, source=source, method=method, files_fileset=files_fileset, name=name, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_proteins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_proteins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protein_id** | **str**|  | [optional] 
 **protein_name** | **str**|  | [optional] 
 **uniprot_name** | **str**|  | [optional] 
 **uniprot_full_name** | **str**|  | [optional] 
 **dbxrefs** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **method** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[ProteinsFromVariants200ResponseInner]**](ProteinsFromVariants200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_variant_id**
> List[VariantsFromVariantID200ResponseInner] variants_from_variant_id(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, r2=r2, d_prime=d_prime, ancestry=ancestry, organism=organism, verbose=verbose, page=page, limit=limit)

Retrieve genetic variants in linkage disequilibrium (LD).<br>    The following parameters can be used to set thresholds on r2 and d_prime: gt (>), gte (>=), lt (<), lte (<=).<br>     Set verbose = true to retrieve full info on the variants.<br>      At least one of these fields is required: variant_id, spdi, hgvs, rsid, ca_id, or region.<br>     Example: variant_id = NC_000011.10:9083634:A:T,<br>     spdi = NC_000011.10:9083634:A:T, <br>     hgvs = NC_000011.10:g.9083635A>T, <br>     rsid = rs60960132, <br>     ca_id = CA217534780, <br>     region = chr17:7166090-7166095 (maximum length: 10kb), <br>     r2 = gte:0.8, <br>     d_prime = gt:0.9, <br>     ancestry = EUR. <br>     The limit parameter controls the page size and can not exceed 500. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_from_variant_id200_response_inner import VariantsFromVariantID200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    rsid = 'rsid_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    region = 'region_example' # str |  (optional)
    r2 = 'r2_example' # str |  (optional)
    d_prime = 'd_prime_example' # str |  (optional)
    ancestry = 'ancestry_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    verbose = false # str |  (optional) (default to false)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_variant_id(spdi=spdi, hgvs=hgvs, rsid=rsid, ca_id=ca_id, variant_id=variant_id, region=region, r2=r2, d_prime=d_prime, ancestry=ancestry, organism=organism, verbose=verbose, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_variant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_variant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **rsid** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **r2** | **str**|  | [optional] 
 **d_prime** | **str**|  | [optional] 
 **ancestry** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **verbose** | **str**|  | [optional] [default to false]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[VariantsFromVariantID200ResponseInner]**](VariantsFromVariantID200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_from_variant_id_summary**
> List[VariantsFromVariantIDSummary200ResponseInner] variants_from_variant_id_summary(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, page=page, limit=limit)

Retrieve a summary of genetic variants in linkage disequilibrium (LD).<br>     Example: variant_id = NC_000001.11:954257:G:C,<br>     hgvs = NC_000011.10:g.9090011A>G,<br>     spdi = NC_000011.10:9090010:A:G,<br>     ca_id = CA10655063<br>     The limit parameter controls the page size and can not exceed 100. <br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_from_variant_id_summary200_response_inner import VariantsFromVariantIDSummary200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_from_variant_id_summary(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_from_variant_id_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_from_variant_id_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[VariantsFromVariantIDSummary200ResponseInner]**](VariantsFromVariantIDSummary200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_genomic_elements_genes**
> List[VariantsGenomicElementsGenes200ResponseInner] variants_genomic_elements_genes(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, files_fileset=files_fileset, biosample_term=biosample_term, biological_context=biological_context, nearby_genes=nearby_genes, organism=organism, page=page, limit=limit)

Retrieve genes whose expression is modulated by perturbing genomic elements that overlap a variant.<br>     The query starts from a variant, finds overlapping Perturb-seq genomic elements, then returns element-gene associations.<br>     By default (nearby_genes = true), only nearby genes on the same chromosome as the variant are returned, and the overlapping genomic element must be within 2 Mb of the gene TSS; distance_to_tss is included in the response.<br>     Set nearby_genes = false to return all genes linked to the overlapping elements regardless of chromosome or distance.<br>     At least one variant identifier is required: variant_id, spdi, hgvs, or ca_id.<br>     Example: variant_id = NC_000001.11:109426297:G:C,<br>     spdi = NC_000001.11:109426297:G:C,<br>     nearby_genes = true,<br>     files_fileset = IGVFFI0206LUDV,<br>     biological_context = HCASMC-hTERT,<br>     biosample_term = EFO_0022614.<br>     The limit parameter controls the page size and can not exceed 100.<br>     Pagination is 0-based.

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_genomic_elements_genes200_response_inner import VariantsGenomicElementsGenes200ResponseInner
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    spdi = 'spdi_example' # str |  (optional)
    hgvs = 'hgvs_example' # str |  (optional)
    ca_id = 'ca_id_example' # str |  (optional)
    variant_id = 'variant_id_example' # str |  (optional)
    files_fileset = 'files_fileset_example' # str |  (optional)
    biosample_term = 'biosample_term_example' # str |  (optional)
    biological_context = 'biological_context_example' # str |  (optional)
    nearby_genes = true # str |  (optional) (default to true)
    organism = Homo sapiens # str |  (optional) (default to Homo sapiens)
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.variants_genomic_elements_genes(spdi=spdi, hgvs=hgvs, ca_id=ca_id, variant_id=variant_id, files_fileset=files_fileset, biosample_term=biosample_term, biological_context=biological_context, nearby_genes=nearby_genes, organism=organism, page=page, limit=limit)
        print("The response of IgvfCatalogApi->variants_genomic_elements_genes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_genomic_elements_genes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spdi** | **str**|  | [optional] 
 **hgvs** | **str**|  | [optional] 
 **ca_id** | **str**|  | [optional] 
 **variant_id** | **str**|  | [optional] 
 **files_fileset** | **str**|  | [optional] 
 **biosample_term** | **str**|  | [optional] 
 **biological_context** | **str**|  | [optional] 
 **nearby_genes** | **str**|  | [optional] [default to true]
 **organism** | **str**|  | [optional] [default to Homo sapiens]
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] 

### Return type

[**List[VariantsGenomicElementsGenes200ResponseInner]**](VariantsGenomicElementsGenes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_region_summary**
> VariantsRegionSummary200Response variants_region_summary(region)

Retrieve a summary count of all methods reporting variants in a given region.<br>     Example: region = chr1:1157520-1158520 (maximum length: 10kb).

### Example


```python
import igvf_catalog_client
from igvf_catalog_client.models.variants_region_summary200_response import VariantsRegionSummary200Response
from igvf_catalog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.catalogkg.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_client.Configuration(
    host = "https://api.catalogkg.igvf.org/api"
)


# Enter a context with an instance of the API client
with igvf_catalog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_client.IgvfCatalogApi(api_client)
    region = 'region_example' # str | 

    try:
        api_response = api_instance.variants_region_summary(region)
        print("The response of IgvfCatalogApi->variants_region_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IgvfCatalogApi->variants_region_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | 

### Return type

[**VariantsRegionSummary200Response**](VariantsRegionSummary200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

