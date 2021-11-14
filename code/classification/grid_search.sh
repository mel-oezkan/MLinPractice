#!/bin/bash

<<<<<<< HEAD
mkdir -p data/classification

# specify hyperparameter values
values_of_k=("1 2 3 4 5 6 7 8 9 10")


# different execution modes
=======
# create directory if not yet existing
mkdir -p data/classification/

values_of_k=("1 2 3 4 5 6 7 8 9 10")

>>>>>>> upstream/hyperparams
if [ $1 = local ]
then
    echo "[local execution]"
    cmd="code/classification/classifier.sge"
elif [ $1 = grid ]
then
    echo "[grid execution]"
    cmd="qsub code/classification/classifier.sge"
else
<<<<<<< HEAD
    echo "[ERROR! Argument not supported!]"
    exit 1
fi

# do the grid search
=======
    echo "[ERROR: argument not supported!]"
    exit 1
fi

>>>>>>> upstream/hyperparams
for k in $values_of_k
do
    echo $k
    $cmd 'data/classification/clf_'"$k"'.pickle' --knn $k -s 42 --accuracy --kappa
<<<<<<< HEAD
done
=======
done

>>>>>>> upstream/hyperparams
