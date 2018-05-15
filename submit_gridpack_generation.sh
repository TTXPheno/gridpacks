#!/bin/bash

memory=${1}
diskspace=${2}
masterqueue=${3}
name=${4}
carddir=${5}
workqueue=${6}
outputdir=${7}
jobstep=${8}
scram_arch=${9}
cmssw_version=${10}

if [ -z ${outputdir} ]; then
  outputdir=`pwd`
fi

bsub -q ${masterqueue} -C 0 -J ${name} -R "rusage[mem=${memory}:pool=${diskspace}]" "export PRODHOME=`pwd`; gridpack_generation.sh ${name} ${carddir} ${workqueue} ${outputdir} ${jobstep} ${scram_arch} ${cmssw_version}"
