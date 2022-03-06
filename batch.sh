#!/bin/bash

id=$1
find ../ssl/src/ -type f|grep $id|xargs cp -t vc/src/
find ../ssl/tgt_22050/ -type f|grep $id|xargs cp -t vc/ref
find ../ssl/res_same/ -type f|grep $id|xargs cp -t vc/res1/
find ../ssl/res_1shotVC_libritts_ecapa_f0/ -type f|grep $id|xargs cp -t vc/res2
find ../ssl/res_1shotVC_libritts_salnNoBN/ -type f|grep $id|xargs cp -t vc/res3
