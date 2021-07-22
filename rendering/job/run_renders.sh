set -eu

LEVEL=$1
MODE=$2

if [ -z "$LEVEL" ] || [ -z "$MODE" ]; then
  echo "Usage: ./run_render.sh LEVEL MODE"
  echo "- LEVEL: int, choices=[1,2,3,4]"
  echo "- MODE: train or val"
  exit
fi


if [ $MODE = "train" ]; then
  NAME=bop-64k-lv$LEVEL
  N_IMG=64000
  N_IMG_PER_JOB=20
  N_IMG_PER_SCN=10
elif [ $MODE = "val" ]; then
  NAME=bop-1000-lv$LEVEL
  N_IMG=1000
  N_IMG_PER_JOB=20
  N_IMG_PER_SCN=10
else
  echo "Usage: ./run_render.sh LEVEL MODE"
  echo "- LEVEL: int, choices=[1,2,3,4]"
  echo "- MODE: train or val"
  exit
fi


N_OBJ_PER_SCENE=10
OBJ_SET=""  # default: all


if [ $LEVEL = "7" ]; then  # Same as run_render_64k.sh
  CONFIG=/renderer/config.yaml
elif [ $LEVEL = "6" ]; then
  CONFIG=/renderer/config.yaml
  OBJ_SET="--dataset tless:itodd"
elif [ $LEVEL = "5" ]; then
  CONFIG=/renderer/config_lv4.yaml
elif [ $LEVEL = "4" ]; then
  CONFIG=/renderer/config_lv3.yaml
elif [ $LEVEL = "3" ]; then
  CONFIG=/renderer/config_lv4.yaml
  OBJ_SET="--dataset tless:itodd"
elif [ $LEVEL = "2" ]; then
  CONFIG=/renderer/config_lv3.yaml
  OBJ_SET="--dataset tless:itodd"
  #N_OBJ_PER_SCENE=1
elif [ $LEVEL = "1" ]; then
  CONFIG=/renderer/config_lv3.yaml
  N_OBJ_PER_SCENE=1
elif [ $LEVEL = "0" ]; then
  CONFIG=/renderer/config_lv3.yaml
  OBJ_SET="--dataset tless:itodd"
  N_OBJ_PER_SCENE=1
fi


python3 ./render_bop.py \
--n-image $N_IMG --n-image-per-job $N_IMG_PER_JOB --n-image-per-scene $N_IMG_PER_SCN \
--queue-name $NAME \
--out $NAME \
--config $CONFIG \
--n-object-per-scene $N_OBJ_PER_SCENE $OBJ_SET
