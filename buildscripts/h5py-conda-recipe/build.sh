MACOSX_DEPLOYMENT_TARGET=10.9 $PYTHON setup.py configure --hdf5="${PREFIX}"
MACOSX_DEPLOYMENT_TARGET=10.9 $PYTHON setup.py build install --single-version-externally-managed --record=record.txt
