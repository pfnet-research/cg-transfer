set -eu

LEVEL=$1
if [ -z "$LEVEL" ]; then
  echo "Usage: ./run_render_64k.sh "
fi

N_IMG=1280000
N_IMG_PER_JOB=20
N_IMG_PER_SCN=10
N_OBJ_PER_SCENE=10
CONFIG=/renderer/config.yaml

NAME=bop-1280k
echo $NAME

#NAME=test

python3 ./render_bop.py \
--n-image $N_IMG --n-image-per-job $N_IMG_PER_JOB --n-image-per-scene $N_IMG_PER_SCN \
--queue-name $NAME \
--out $NAME \
--config $CONFIG \
--n-object-per-scene $N_OBJ_PER_SCENE
