# Try to find tiny-dnn
# Once done, this will define
#
# tiny-dnn_FOUND        - system has tiny-dnn
# tiny-dnn_INCLUDE_DIRS - tiny-dnn include directories

find_path(
	tiny-dnn_INCLUDE_DIR
	NAMES tiny_dnn/tiny_dnn.h
	PATHS ${CONAN_INCLUDE_DIRS_TINY-DNN}
)

set(tiny-dnn_FOUND TRUE)
set(tiny-dnn_INCLUDE_DIRS ${tiny-dnn_INCLUDE_DIR})

mark_as_advanced(tiny-dnn_INCLUDE_DIR)
