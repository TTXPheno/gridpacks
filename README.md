# gridpacks
Repository for generating gridpacks with reweighting with amcatnlo 

Card templates can be found in the path addons/cards/UFOMODEL_template and the corresponding UFO file in addons/models
to generate a gridpack run "source submit_madpack_ttbareft.sh"
this will copy the template and replace settings in the default templates if needded according to what is specified 
in the submit script 
modify customize card to change the corresponding operators you want to use
the example gridpack gluontop_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz was tested in debug which 
also contains an example lhe output with EFT and systematics weights   
