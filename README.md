# gridpacks
Repository for generating gridpacks with reweighting with amcatnlo 

Card templates can be found in the path addons/cards/UFOMODEL_template and the corresponding UFO file in addons/models
to generate a gridpack run "source submit_madpack_ttbareft.sh"
this will copy the template and replace settings in the default templates if needded according to what is specified 
in the submit script 
modify customize card to change the corresponding operators you want to use
the example gridpack gluontop_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz was tested in debug which 
also contains an example lhe output with EFT and systematics weights   

## Generate multiple gridpacks
To generate more than one gridpack use submit_gridpacks.sh

Before you start create a cms environment using the following commands:
```
source ~/.profile <-- usually not necessary (to define the aliases)
cmsrel CMSSW_9_4_6_patch1
cd CMSSW_9_4_6_patch1/src
cmsenv
export CMSSW_BASE=
```
Define the following parameters in submit_gridpacks.sh:
```
Output directory
states to analyze (e.g. ttZ ttgamma) <-- make sure you have all cards in addons/cards/
declare number of jets
declare polynomial order (e.g. 2nd, 3rd, 4th)
lxplus GRID (where to calculate)
dim6 operators and stepsize as string (e.g. 'ctZ 1 ctZI 1')
```

The script will loop over all polynomial orders and all states to analyze and create a directory structure in the output directory containing the calculated gridpacks
Available gridpacks, pkl files and STDOUTs stored at:  
```  
/afs/hephy.at/data/llechner01/TTXPheno/gridpacks/<date>/<process>/order<poly order>/  
```  
  
## List of available gridpacks:  
  
### 08/05/2018  
##### currently creating (finished ~10 days)  

| process  | poly order | # coeff | Wilson coefficients                                                                 | Link to gen. events |
|:--------:|:----------:|:-------:|:-----------------------------------------------------------------------------------:|:------------------------:|
| ttZ      | 3          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | not (yet) processed!  |
| ttW      | 3          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | not (yet) processed!  |
| ttgamma  | 3          | 15      | ctp, ctpI, cpQM, cpQ3, cpt, cptb, cptbI, ctW, ctWI, ctZ, ctZI, cbW, cbWI, ctG, ctGI | not (yet) processed!  |
  
  
### 07/05/2018  
| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events   |
|:--------:|:----------:|:-------:|:------------------------------------------:|:---------------------:|
| ttZ      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttW      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttgamma  | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
  
| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events |
|:--------:|:----------:|:-------:|:------------------------------------------:|:-------------------:|
| ttZ      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttZ events](https://cmsweb.cern.ch/das/request?input=%2FttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttZ0j_order3_8weights-7a5fde3f5bf89006ee3acec926ca87d8%2FUSER&instance=prod%2Fphys03) |
| ttW      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttW events](https://cmsweb.cern.ch/das/request?input=%2FttW0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttW0j_order3_8weights-593ea75549b4c51667dffc93040bbda1%2FUSER&instance=prod%2Fphys03) |
| ttgamma  | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | [1M ttgamma events](https://cmsweb.cern.ch/das/request?input=%2Fttgamma0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball%2Fllechner-ttgamma0j_order3_8weights-10fcfa1a1c01204983ea66975abf2caf%2FUSER&instance=prod%2Fphys03) |  
  
### 03/05/2018  
##### Error in the pdfHandler!  

| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events   |
|:--------:|:----------:|:-------:|:------------------------------------------:|:---------------------:|
| ttZ      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttW      | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttgamma  | 2          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
  
| process  | poly order | # coeff | Wilson coefficients                        | Link to gen. events   |
|:--------:|:----------:|:-------:|:------------------------------------------:|:---------------------:|
| ttZ      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttW      | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
| ttgamma  | 3          | 8       | cpQM, cpt, ctW, ctWI, ctZ, ctZI, ctG, ctGI | not (yet) processed!  |
  
