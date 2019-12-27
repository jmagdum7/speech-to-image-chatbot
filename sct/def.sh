#!/bin/sh
# python2 /media/jmagdum7/STUDIES\ AND\ WORK/BE/BE\ Project/attngan/coco_chatbot/sct/run.py

python2 /media/jmagdum7/STUDIES\ AND\ WORK/BE/BE\ Project/attngan/AttnGAN-master/code/main.py --cfg /media/jmagdum7/STUDIES\ AND\ WORK/BE/BE\ Project/attngan/AttnGAN-master/code/cfg/eval_coco.yml --gpu 0
mv /media/jmagdum7/STUDIES\ AND\ WORK/BE/BE\ Project/attngan/AttnGAN-master/models/coco_AttnGAN2/example_captions/0_s_0_g2.png /media/jmagdum7/STUDIES\ AND\ WORK/BE/BE\ Project/attngan/coco_chatbot/static/images/0_s_0_g2.png